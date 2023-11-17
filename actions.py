resolution = {
        "Atualizar método de pagamento": "",
        "Acompanhar Status do meu Pedido":"", 
        }

def payment(resolution):
    if resolution == "Atualizar método de pagamento":
        print(f"Para atualizar seu método de pagamento basta acessar: www.abc.com e entrar na aba 'ABC' ")
    else: 
        print("Não encontramos uma resposta para sua pergunta. Pode tentar reescreve-la, por favor")

def status(resolution):
    if resolution == "Atualizar método de pagamento":
        print(f"Para atualizar seu método de pagamento basta acessar: www.abc.com e entrar na aba 'ABC' ")
    else: 
        print("Não encontramos uma resposta para sua pergunta. Pode tentar reescreve-la, por favor")