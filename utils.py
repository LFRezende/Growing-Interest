from matplotlib import pyplot as plt


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
    vector_sum = []
    for x in range(0, len(installments)):
        sum = sum + installments[x]
        vector_sum.append(sum)
    return sum, vector_sum


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
        timestamps.append(k + 1)
    print(
        f"The total value of the investment after {times} successive instalments is US$ {total_value:.2f}."
    )
    return total_value, capital_amount, timestamps


def graphInvestment(timestamps, invested, not_invested, timeunit):
    gains = diff(invested, not_invested)
    plt.plot(timestamps, invested, "-bo", label="Invested Sum")
    plt.plot(timestamps, not_invested, "-ro", label="Not-Invested Sum")
    plt.plot(timestamps, gains, "-go", label="Gains")
    plt.title("Investment x Time")
    plt.xlabel(timeunit)
    plt.ylabel("Capital")
    plt.grid()
    plt.legend(loc="upper left")
    plt.show()


def diff(l1, l2):
    d = []
    for x in range(0, len(l1)):
        d.append(l1[x] - l2[x])
    return d
