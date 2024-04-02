def contador_de_moedas(valorEntrada):
    valorTrabalhado = float(valorEntrada)
    moedasContadas = []
    if valorTrabalhado >= 1:
        moedasContadas.append(valorTrabalhado // 1)
        valorTrabalhado = valorTrabalhado % 1
        if valorTrabalhado >= 0.5:
            moedasContadas.append(valorTrabalhado // 0.5)
            valorTrabalhado = valorTrabalhado % 0.5
            if valorTrabalhado >= 0.25:
                moedasContadas.append(valorTrabalhado // 0.25)
                valorTrabalhado = valorTrabalhado % 0.25
                if valorTrabalhado >= 0.1:
                    moedasContadas.append(valorTrabalhado // 0.1)
                    valorTrabalhado = valorTrabalhado % 0.1
                    if valorTrabalhado >= 0.01:
                        moedasContadas.append(valorTrabalhado // 0.01)
    return moedasContadas


print(contador_de_moedas(49.85))
