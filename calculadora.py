def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def obter_operacao():
    operacoes_validas = ["+", "-", "*", "/"]
    while True:
        print("\nOperações disponíveis:")
        print("+")
        print("-")
        print("*")
        print("/")
        
        operacao = input("Escolha uma operação: ").strip()
        
        if operacao in operacoes_validas:
            return operacao
        else:
            print("Operação inválida. Escolha uma das opções acima.")


def calculadora():
    print("=== CALCULADORA ===")
    
    while True:
        a = obter_numero("Digite o primeiro número: ")
        operacao = obter_operacao()
        b = obter_numero("Digite o segundo número: ")

        try:
            if operacao == "+":
                resultado = soma(a, b)
            elif operacao == "-":
                resultado = subtracao(a, b)
            elif operacao == "*":
                resultado = multiplicacao(a, b)
            elif operacao == "/":
                resultado = divisao(a, b)

            print(f"\n Resultado: {resultado}")

        except ZeroDivisionError as erro:
            print(f"❌ Erro: {erro}")
        except Exception as erro:
            print(f"❌ Erro inesperado: {erro}")

        continuar = input("\nDeseja fazer outro cálculo? (s/n): ").lower()
        if continuar != "s":
            print("Encerrando calculadora...")
            break


if __name__ == "__main__":
    calculadora()