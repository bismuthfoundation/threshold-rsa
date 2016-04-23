import random
import gmpy2


########################
# General Math Helpers
########################

'''
Returns a random prime number in the range [start, end)
'''
def get_random_prime(start,end):
    i = random.randint(start,end) # better random nunber generator
    while not gmpy2.is_prime(i):
        i +=1
    return i

def get_random_safe_prime(start,end):
    i = random.randint(start,end) # better random nunber generator
    while not (gmpy2.is_prime(i) and gmpy2.is_prime(gmpy2.t_div((i-1),2))):
        i +=1
    return i

'''
Returns a random integer between 0 and n-1.
'''
def get_random_int(n):
    i = random.randint(0,2**30) # better random nunber generator
    return gmpy2.mpz_random(gmpy2.random_state(i), n)

'''
Returns (x^y) mod m
'''
def powmod(x, y, m):
    return gmpy2.powmod(gmpy2.mpz(x), gmpy2.mpz(y), gmpy2.mpz(m))

'''
Multiply x * y
'''
def multiply(x, y):
    return gmpy2.mul(gmpy2.mpz(x), gmpy2.mpz(y))


'''
Divide x / y
'''
def divide(x, y):
    return gmpy2.t_div(gmpy2.mpz(x), gmpy2.mpz(y))

'''
Subtract x - y
'''
def subtract(x, y):
    return gmpy2.sub(gmpy2.mpz(x), gmpy2.mpz(y))


'''
Calcaulte x mod m
'''
def mod(x, m):
    remainder = gmpy2.t_mod(gmpy2.mpz(x), gmpy2.mpz(m))
    # gmpy2.t_mod can return negative values, but we want positive ones.
    if remainder < 0:
        remainder = gmpy2.add(remainder, m)
    return remainder

#[d_1, d_2...d_n] such that sum [] = d
def d_i_creator(d, n):
    d_i = []
    #choose random values for first n-1
    for i in range(n-1):
        d_i.append(get_random_int(divide(d, 10)))

    #last one must make sum to d
    for i in d_i:
        d = subtract(d, i)
    d_i.append(d)
    return d_i

#########################################
# Subset Presigning Algorithm Helpers
#########################################

'''
Helper class (basically a struct) that stores the data that
a computer needs for the subset presigning algorithm.
'''
class PresigningData:
    def __init__(self):
        # All variables are named as they are in the paper pages 26 - 27.
        self.lamdba_t_i = None
        self.s_t_i = None
        self.h_t_i = None
        self.received_h_t_i = {} # maps id -> h_t_i for all k computers

        self.sigma_I_t_i = None # signature on the dummy message
        self.x_I = None
        self.received_x_I = [] # contains tuples with (id, x_I) computed by other parties, length of array = k-1

        self.D_I = None # will contain tuples of the form (x_I, [(id, h_t_i, c_prime_t_i)])
        self.S_I_t_i = None # will contain simply s_t_i

'''
Helper class for BGW Protocol data.
'''
class BGWData:
    def __init__(M, p_i, q_i, l):
        # All variables are as described in Section 4.3, pg 14-15
        self.M = M
        self.p_i = p_i
        self.q_i = q_i

        self.l = l # l = floor((n-1)/2) where n is the number of computers
        self.a = [] # array of l random coefficients
        self.b = [] # array of l random coefficients
        self.c = [] # array of 2l random coefficients

        self.f_i_j = {} # maps j -> f_i(j) where i is this computer
        self.g_i_j = {}
        self.h_i_j = {}

        self.received_fgh = [] # array that stores the (f_i(j), g_i(j), h_i(j)) from every computer i, where j is this computer
        self.received_N_j = [] # array that stores the N_j for all k computers
        self.share = None # the final share returned to this user


'''
Helper class (basically a struct) that stores the data that
a computer needs for Distributed Sieving section 5.2.1 in the paper.
'''
class PQData:
    def __init__(self, M):
        # All variables are named as they are in the paper pages 17-18
        self.M = M # M = product of all prime numbers between n and B1
        self.a_i = None # random secret integer relatively prime to self.M
        self.u = [] # 2d array where u[i][j] is u_{i,j} in the notation of the paper
        self.v = [] # 2d array where v[i][j] is v_{i,j} in the notation of the paper
        self.a = None # cummulative product of the a_i as we iterate through the protocol






