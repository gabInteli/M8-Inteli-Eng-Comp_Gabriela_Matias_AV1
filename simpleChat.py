import re
from . import actions

intent_dict = {
        r"\b[Aa][tatus](?:\spedido)?\s?[oa]?\s(?:\srastrear)?\s?[oa]?\s(.+)(?:\sonde)?\s?[oa]?\s": actions.status,
        r"\b[Aa](?:\smudar)?\s?[oa]?\s(.+)\b[Aa](?:\spagamento)?\s?[oa]?\s(.+)": actions.payment
        }

def main():
    command = input("Digite o sua pergunta: ")
    for key, function in intent_dict.items():
        pattern = re.compile(key)
        resolution_user = pattern.findall(command)
        if resolution_user:
            print("Encontrei uma intenção! Computando...")
            function(point[0])
            break

if __name__ == "__main__":
    main()