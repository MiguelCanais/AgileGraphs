from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings

from dados_celulas import dados_relatorio
from utils import maiorPrefixoComum, ALIASES

kb = KeyBindings()

def obtemChaves(dados):
    chaves = list(dados.keys())

    for v in dados.values():
        if type(v) is dict:
            chaves += obtemChaves(v)

    return list(set(chaves))


def obtemAutocomplete(expressao):
    if expressao == "":
        return ""
    ultimo = expressao.split(" ")[-1]
    args = ultimo.split(":")

    dados = dados_relatorio

    possiveis = ["ALL"]

    for arg in args[:-1]:
        if arg in ALIASES:
            arg = ALIASES[arg]

        if arg not in dados:
            return ""

        if type(dados[arg]) is not dict:
            return ""

        dados = dados[arg]

    possiveis += obtemChaves(dados)
    prefix = args[-1]
    valid = []

    for k in possiveis:
        if k.startswith(prefix):
            valid.append(k[len(prefix):])

    if len(valid) == 0:
        return ""
    elif len(valid) == 1:
        return valid[0]
    else:
        return maiorPrefixoComum(valid)


@kb.add("tab")
def _(event):
    buffer = event.app.current_buffer
    autocomplete = obtemAutocomplete(buffer.text[: buffer.cursor_position])
    buffer.insert_text(autocomplete)


session = PromptSession(key_bindings=kb)


def obtemInputExpressao():
    try:
        user_input = session.prompt("> ")
        return user_input
    except KeyboardInterrupt:
        return "q"
