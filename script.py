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
tax = [
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
    12.68,
]
times = len(capital)
final_amount, invested, timestamps = total(
    times, capital_vector=capital, taxation_vector=tax
)

sum, not_invested = cumulative_capital(capital)
graphInvestment(timestamps, invested, not_invested, timeunit)
