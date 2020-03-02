class calculator:
      def add(self, num1, num2):
             return num1+num2

      def sub(self, num1, num2):
             return num1-num2

      def division(self, num1, num2):
             return num1/num2

      def multiply(self, num1, num2):
             return num1*num2
        
      def square(self, num1):
             return num1*num1
        
      def squareroot(self, num1):
             return num1**0.5

if __name__ == "__main__":
     c = calculator()
     print (c.add(1,2))
     print (c.sub(3,1))
     print (c.division(4,2))
     print (c.multiply(2,3))
     print (c.square(5))
     print (c.squareroot(100))

     
def test_calc_add():
     c = calculator()
     assert c.add(2,3) == 5

def test_calc_sub():
     c = calculator()
     assert c.sub(3,1) == 2

def test_calc_division():
     c = calculator()
     assert c.division(4,1) == 4

def test_calc_multiply():
     c = calculator()
     assert c.multiply(2,3) == 6