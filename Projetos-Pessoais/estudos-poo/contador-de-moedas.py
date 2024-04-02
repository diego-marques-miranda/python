from decimal import Decimal


def contador_de_moedas(valorEntrada):
    valorTrabalhado = Decimal(valorEntrada)
    moedasContadas = []
    moedasDisponiveis = [Decimal(1), Decimal(0.5), Decimal(0.25), Decimal(0.10), Decimal(0.05), Decimal(0.01)]
    for i in range(0, len(moedasDisponiveis)):
        if valorTrabalhado >= moedasDisponiveis[i]:
            moedasContadas.append(valorTrabalhado // moedasDisponiveis[i])
            valorTrabalhado = valorTrabalhado % moedasDisponiveis[i]
        else:
            moedasContadas.append(0)
    for i in range(0, len(moedasContadas)):
        moedasContadas[i] = float(moedasContadas[i])
    return moedasContadas


print(contador_de_moedas(11.83))
