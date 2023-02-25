from utils import *
from matplotlib import pyplot as plt

timeunit = "Years"
capital = [
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
    10000,
]
tax = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
times = len(capital)
final_amount, invested, timestamps = total(
    times, capital_vector=capital, taxation_vector=tax
)

sum, not_invested = cumulative_capital(capital)
graphInvestment(timestamps, invested, not_invested, timeunit)
