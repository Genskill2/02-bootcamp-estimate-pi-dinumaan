import math
import unittest
import random
from math import sqrt
def monte_carlo(n):
    #I define a variable to store the number of points inside the circle
    circle = 0

    #loop to calculate the points we need for our estimation
    for i in range(1,n+1):
        x = random.random()
        y = random.random()
        
        #Checking to see if the produced number falls into the circle
        if sqrt(x**2 + y**2) <= 1:
            circle += 1

    #I calculate Pi for this iteration
    Pi = 4 * (circle/n)

    #returning the result
    return Pi
def wallis(itr):
    res = 1;
    for i  in range(1,itr):
        res*=(4*i*i/(4*i*i - 1));
    return 2*res;
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
