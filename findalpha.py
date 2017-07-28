from sympy.solvers import nsolve     # import sympy solver 'nsolve' for numerical solution
from sympy import sin                # import trigonometric function from the sympy library
from sympy.abc import x
import math                          # import math library for using constants


class AlphaFind:

    # method to calculate pi:
    def picalculate(self, length, n):
        radius = float((length) / (math.sqrt(2 - (2 * (math.cos((math.radians(360) / n)))))))
        diameter = 2 * radius
        circumference = (length * n)
        return (float(circumference / diameter))

    # method to calculate the alpha, the angle e the angle with vertex at the center of the left circle
    def alphacalculate(self):
        pi = self.picalculate(1, 500)
        self.alpha = nsolve(-sin(x) + x - pi/2, 0)                    # alpha found in radian
        #print pi
        return self.alpha

        # method to print the data calculated in 'alphacalulate' method
    def displayalpha(self):
        print "The value of alpha is: " + str(self.alpha)
        # print self.alpha

alphafind = AlphaFind()               # creating object of the class AlphaFind
alphafind.alphacalculate()            # calling the 'alphacalculate' method
alphafind.displayalpha()              # calling the 'displayalpha' method
