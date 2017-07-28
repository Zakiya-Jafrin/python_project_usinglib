from sympy import cos                       # import trigonometric function from the sympy library
import findalpha, userinput                         # import classes to use data from those classes

alpha = findalpha.AlphaFind()                   # creating object of the class test3
radius = userinput.Input()                      # creating object of the class test4

class Length:

    #  creating method to calculate 'length' the degree of overlap between the two coasters
    def lengthcalculate(self):
            self.beta = cos(alpha.alphacalculate()/ 2)
            self.length = 2 * radius.inputradius() * (1 - self.beta)    # length calculation done in two line for simplicity

    # creating method to print the result of the degree of overlap
    def lengthdisplay(self):
        print self.length

length = Length()                           # creating object of the class Length
length.lengthcalculate()                    # calling the method to calculate the length
length.lengthdisplay()                      # displays the result
