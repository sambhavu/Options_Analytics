import math
import scipy
from math import log, sqrt, exp
from scipy import stats
import matplotlib.pyplot as plt


def bsm_call_value(S0, K, T, r, sigma):
    S0 = float(S0)
    d1 = (log(S0/K) + (r + 0.5 * sigma ** 2) *T) /(sigma*sqrt(T))
    d2 = d1 - sigma *sqrt(T)
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0)) - K * exp(-r*T) * stats.norm.cdf(d2, 0.0, 1.0)

    return value

def bsm_put_value(S0, K, T, r, sigma):
    S0 = float(S0)
    d1 = (log(S0/K) + (r + 0.5 * sigma ** 2) * T) / (sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    value = (-S0 * stats.norm.cdf(-d1, 0.0,1.0)) + K*exp(-r*T) * stats.norm.cdf(-d2, 0.0, 1.0)

    return value

def bsm_vega(S0, K, T, r, sigma):
    S0 = float(S0)
    d1 = (log(S0/K) + (r + 0.5 * sigma ** 2) * T) / (sigma*sqrt(T))
    vega = S0 * stasts.norm.cdf(d1, 0.0, 1.0) * sqrt(T)

    return vega

def bsm_call_implied_vol(S0, K, T, r, C0, sigma_est, it=100):
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est)- C0)/bsm_vega(S0,K,T,r,simga_est))

    return sigma_est



def main():
    stock_price = 100.0
    r = 0.03
    days = 30.0
    t = [.1,.2,.3,.4,.5,.6,.7,.8,.9,1,1.2,1.5,1.8,2.5]
    strike = 60
    sigma = 1


    value1 = 0
    value2 = 0

    print("\tC\tA\tL\tL\tS")
    print("___________________________")
    print(" STRIKE\t\t BSM VALUE")
    print("___________________________")


    for times in t:
        callprices = []
        putprices = []

        for i in range(100):
            value1 = bsm_call_value(stock_price, strike+i, times, r, sigma)
            value2 = bsm_put_value(stock_price, strike+i, times, r, sigma)
           # print(" ", strike + i, "\t", value)
            callprices.append(value1)
            putprices.append(value2)



        plt.plot(callprices)
        plt.plot(putprices)

    plt.show()


main()

