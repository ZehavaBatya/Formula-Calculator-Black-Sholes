# libraries
from audioop import ratecv
from cgi import print_exception
from typing_extensions import assert_type
import numpy as np
from scipy.stats import norm

def black_scholes_calc(S0, K, r, T, sigma, option_type='call'):
    This function calculates the value of the European option based on Black-Scholes formula. It takes the following parameters:
    -S0 for the underlying asset print
    -K for the strike price
    -r for the risk-free rate
    -T for the time to maturity
    -sigma for the implied volatility of the underlying asset
    -option_type for the type of the option to be calculated, i.e., call or put

    # 1) determine N(d1) and N(d2)
    d1 = 1/(sigma*np.sqrt(T)) * (np.log(S0/K) + (r+sigma***2/2)*T)
    d2 = d1 - sigma*np.sqrt(T)

    nd1 = norm.cdf(d1)
    nd2 = norm.cdf(d2)

    n_d1 = norm.cdf(-d1)
    n_d2 = norm.cdf(-d2)

    # 2) determine call value
    c = nd1*S0 - nd2*K*np.exp(-r*T)

    # 3) determine put value
    p =  K*np.exp(-r*T)*n_d2 = S0*n_d1

    # 4) define which value to return based on the option_type parameter
    if option_type=='call':
        return c
    elif option_type=='put':
        return p
    else:
        print('Wrong option type specified')