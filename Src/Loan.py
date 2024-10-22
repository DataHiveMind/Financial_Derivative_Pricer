import math as m
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

class Loan:
  def __init__(self, notional, redemption, interest_rate):
    """
    Initializes a Loan object with the given parameters.
    """
    self.notional = notional
    self.redemption = redemption
    self.interest_rate = interest_rate

  def Future_Value(self)-> float:
    """
    Returns the future value of the loan.
    """
    return self.redemption - self.notional * (1 + self.interest_rate)

  def Present_Value(self)-> float:
    """
    Returns the present value of the loan.
    """
    return self.redemption/(1 + self.interest_rate) - self.notional

  def Yield_to_Maturity(self)-> float:
    """
    Returns the yield to maturity of the loan.
    """
    return self.interest_rate

  def Duration(self)-> float:
    """
    Returns the duration of the loan.
    """
    return 1 / (1 + self.interest_rate)

  def Convexity(self)-> float:
    """
    Returns the convexity of the loan.
    """
    return 1 / (1 + self.interest_rate) ** 2
  
class zero:
  def __init__(self, maturity):

    """
    Initializes a zero object with the given parameters.
    """
    self.maturity = maturity

  def YTM(self, price)-> float:
    """
    Returns the yield to maturity of the zero.
    """
    return m.pow(100/price, 1/self.maturity) - 1

  def Price(self, ytm)-> float:
    """
    Returns the price of the zero.
    """
    return 100/m.pow(1 + ytm, self.maturity)

class bond:
  def __init__(self, maturity, coupon):
    self.maturity = maturity
    self.coupon = coupon

  def pv(self, rate):
    sum = 100 * m.pow(1+rate, -self.maturity)
    for i in range(1, self.maturity + 1):
      sum += self.coupon * m.pow(1+rate, -i)
    return round(sum, 2)
  
def monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    n = years * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -n)

def find_rate_for_payment(target_payment, principal, years):
    def equation(rate):
        return monthly_payment(principal, rate, years) - target_payment

    # Initial guess for the annual rate
    initial_guess = 0.05  # 5%
    return fsolve(equation, initial_guess)[0]