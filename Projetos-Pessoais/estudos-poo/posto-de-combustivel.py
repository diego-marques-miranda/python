def autonomia(km=100.0, litros=10.0):
    return km / litros


def alcool_ou_gasolina(valor_alcool=0.7, valor_gasolina=1.0):
    if valor_alcool / valor_gasolina > 0.7:
        return 'Alcool'
    if valor_alcool / valor_gasolina < 0.7:
        return ('Gasolina')


def input_com_ponto(frase=''):
    entrada = input(frase).strip()
    entrada = entrada.replace(',', '.')
    entrada = float(entrada)
    return entrada

def calculador_de_preco(valor_combustivel=0, quantidade_de_litros=0):
    return valor_combustivel * quantidade_de_litros



