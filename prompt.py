from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings

from dados_celulas import dados_relatorio

kb = KeyBindings()


def obtemChaves(dados):
    chaves = list(dados.keys())

    for v in dados.values():
        if type(v) == dict:
            chaves += list(obtemChaves(v))

    return list(set(chaves))


def maiorPrefixoComum(l):
    '''
    Dado uma lista de strings encontra o maior prefix comum a todas
    as strings

    Por exemplo:
    l = ["prod1", "prod2", "prod3"]
    O maior prefixo comum é "prod"
    '''
    i = 0
    while True:
        letra = 0
        for s in l:
            if len(s) == i:
                return s

            if letra == 0:
                letra = s[i]
            elif s[i] != letra:
                return s[:i]

        i += 1

def obtemAutocomplete(expressao):
    if expressao == "": return ""
    ultimo = expressao.split(' ')[-1]
    args = ultimo.split(':')

    dados = dados_relatorio

    possiveis = []

    for arg in args[:-1]:
        if type(dados[arg]) != dict: 
            return ""
        
        if not arg in dados:
            return ""
        
        dados = dados[arg]

    possiveis = obtemChaves(dados)
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
    autocomplete = obtemAutocomplete(buffer.text[:buffer.cursor_position])
    buffer.insert_text(autocomplete)

session = PromptSession(key_bindings=kb)

def obtemInputExpressao():
    try:
        user_input = session.prompt("> ")
        return user_input
    except KeyboardInterrupt:
        return "q"
