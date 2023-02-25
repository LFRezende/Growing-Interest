def isPositive(initialValue):
    while True:
        if initialValue <= 0:
            initialValue = float(input("Please, type in a positive value."))
        else:
            break
    return initialValue


def initialValues(initialValue=None, interest=None):
    if initialValue:
        isPositive(initialValue)
    else:
        isPositive(float(input("Type in the first installment.")))
    if interest:
        isPositive(interest)
    else:
        isPositive(float(input("Type in the interest.")))


def iteration(new_amount, current, tax):
    amount = (current + new_amount) * (1 + tax / 100)
    return amount


def cumulative_capital(installments):
    sum = 0
    for x in range(0, len(installments)):
        sum = sum + installments[x]
    return sum


def total(times, capital_vector, taxation_vector):
    capital_amount = []
    timestamps = []
    total_value = 0
    if len(capital_vector) != times or len(taxation_vector) != times:
        print("Vectors must length the same, and equal to the number of installments.")
        return 0
    for k, v in enumerate(taxation_vector):
        if k == 0:
            total_value = iteration(capital_vector[k], 0, v)
        else:
            total_value = iteration(capital_vector[k], total_value, v)
        capital_amount.append(total_value)
        timestamps.append(k)
    print(
        f"The total value of the investment after {times} successive instalments is US$ {total_value:.2f}."
    )
    return total_value, capital_amount, timestamps
