
def daily_temperatures(temps):
    output = []
    for i in range(len(temps)):
        found = False
        for j in range(i+1, len(temps)):
            if temps[j] > temps[i]:
                output.append(j - i)
                found = True
                break
        if found is False:
            output.append(0)
    return output


print(daily_temperatures([72, 70, 71, 69, 70]))
