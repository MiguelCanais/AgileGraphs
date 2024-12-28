from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings

from obtem_valor import obtemDados
from calcula_info import processaExpressao, ehVariavel

kb = KeyBindings()


def maiorPrefixoComum(strigs: list[str]) -> str:
    """
    Dado uma lista de strings encontra o maior prefixo comum a todas
    as strings.

    Por exemplo:
    strings = ["produto1", "produto2", "produto3"]
    O maior prefixo comum é "produto".
    """
    if len(strigs) == 0:
        return ""

    i = 0
    while True:
        letra = 0
        for s in strigs:
            if len(s) == i:
                return s

            if letra == 0:
                letra = s[i]
            elif s[i] != letra:
                return s[:i]

        i += 1


def obtemChaves(dados: dict):
    """
    Dados um dicionario e devolve uma lista com todas as suas chaves
    e as de qualquer dicionario que ele contenha.
    """
    chaves = list(dados.keys())

    for v in dados.values():
        if type(v) is dict:
            chaves += obtemChaves(v)

    return list(set(chaves))


def obtemAutocomplete(expressao_raw: str):
    """ Recebe a expressao que o utilizador está a escrever e determina o autocomplete se existir."""
    if expressao_raw == "":
        return ""

    expressao = processaExpressao(expressao_raw)[0]
    variavel = expressao[-1]

    if not ehVariavel(variavel):
        return ""

    chaves = variavel.split(":")
    chaves, prefix = chaves[:-1], chaves[-1]

    # obtem o dicionario que contêm uma chave começada por prefix
    dados, failure_index = obtemDados(chaves)
    while not any(opcao.startswith(prefix) for opcao in dados) and type(dados) is dict:
        primeira_opcao = list(dados.keys())[0]
        chaves = chaves[:failure_index] + [primeira_opcao] + chaves[failure_index:]

        dados, failure_index = obtemDados(chaves)

    # se a última chave está mal escrita em vez de devolver um dicionário vai devolver uma string, uma célula
    if type(dados) is str:
        return ""

    if prefix in dados and type(dados[prefix]) is dict:
        return ':'

    # Todas as possiveis strings para autocomplete
    possiveis = obtemChaves(dados)

    valid = []
    for k in possiveis:
        if k.startswith(prefix):
            valid.append(k[len(prefix):])

    if len(valid) == 0:
        return ""
    else:
        return maiorPrefixoComum(valid)


@kb.add("tab")
def _(event):
    buffer = event.app.current_buffer
    autocomplete = obtemAutocomplete(buffer.text[:buffer.cursor_position])
    buffer.insert_text(autocomplete)


session = PromptSession(key_bindings=kb)


def obtemInputExpressao():
    """ Obtem uma expressao utilizando uma prompt."""
    try:
        user_input = session.prompt("> ")
        return user_input
    except KeyboardInterrupt:
        return "q"
