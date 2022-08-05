cod_1, quant_1, valor_1 = input().split()
cod_1 = int(cod_1)
quant_1 = int(quant_1)
valor_1 = float(valor_1)


cod_2, quant_2, valor_2 = input().split()
cod_2 = int(cod_2)
quant_2 = int(quant_2)
valor_2 = float(valor_2)

def calcular (quant_1, valor_1, quant_2, valor_2):
    soma = float( quant_1 * valor_1 + quant_2 * valor_2)
    print(f"VALOR A PAGAR: R$ {soma:.2f}")

calcular(quant_1, valor_1, quant_2, valor_2)