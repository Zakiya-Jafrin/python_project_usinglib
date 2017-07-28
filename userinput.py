class Input:

    # creating a method to take the radius of the circle as an input provided by the user
    def inputradius(self):
        while True:
                n = raw_input("Enter the radius: R = ")  # takes the radius as an input form the user
                try:
                    self.radius = float(n)
                    if self.radius <= 0:
                        raise Exception
                except ValueError:
                    print('You must put an interger, not a charecter! Try again...')
                except Exception:
                    print('Invalid input! Radius can not be negative. Please put a postive value. Try again...')
                else:
                    break

        return self.radius
radius = Input()                    # creating object of the class Input
# radius.inputradius()
