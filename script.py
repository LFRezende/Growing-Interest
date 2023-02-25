from utils import *
import numpy
from matplotlib import pyplot as plt

unit = "Years"
capital = [1200, 1200, 1200, 1200, 1200]
tax = [12.68, 12.68, 12.68, 12.68, 12.68]
times = len(capital)
final_amount, gains, timestamps = total(
    times, capital_vector=capital, taxation_vector=tax
)


plt.plot(timestamps, gains, "-b")
plt.plot(timestamps, capital, "-o")
plt.title("Investment x Time")
plt.xlabel(unit)
plt.ylabel("Capital")
plt.show()
