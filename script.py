from utils import *
from matplotlib import pyplot as plt

timeunit = "Years"
capital = [
    500000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
]
tax = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
times = len(capital)
final_amount, invested, timestamps = total(
    times, capital_vector=capital, taxation_vector=tax
)

sum, not_invested = cumulative_capital(capital)
graphInvestment(timestamps, invested, not_invested, timeunit)
