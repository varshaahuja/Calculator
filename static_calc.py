class calculator:

      #def __init__(self): check with Prof why was the initialization necessary as it does not impact the code
      #        pass
      
      #addition
      @staticmethod
      def add(num1, num2):
             return round(num1+num2,2)

      #subtraction
      @staticmethod
      def sub(num1, num2):
             return round(num1-num2,2)
      
      #division
      @staticmethod
      def div(num1, num2):
             if (num2 == 0):
               return '0 is an invalid value'
             else:
               return round(num1/num2,2)

      #multiplication
      @staticmethod
      def multiply(num1, num2):
             return round(num1*num2,2)
     
      #square
      @staticmethod        
      def square(num1):
             return round(num1*num1,2)

      #squareroot
      @staticmethod        
      def squareroot(num1):
             if (num1 == 0):
               return '0 is an invalid value'
             else:
               return round(num1**0.5,2)

if __name__ == "__main__":

    #c = Calculator()
    
    choice = ""

    while choice != "7":

        print("Select Operation:")    
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Square")
        print("6. Square Root")
        print("7. Quit")        
        choice = input("Enter choice:")
        
        if choice in ["1","2","3","4"]:            
                num1 = float(input("Enter first number:"))
                num2 = float(input("Enter second number:"))
        
        elif choice in ["5","6"]:
                num1 = float(input("Enter the number:"))
                   
        else:
                print("Quit")

        if choice == "1":
            print("Addition of numbers", num1, "&", num2, "is", calculator.add(num1, num2))

        elif choice == "2":
            print("Subtraction of numbers", num1, "&", num2, "is", calculator.sub(num1, num2))

        elif choice == "3":
            print("Division of numbers", num1, "&", num2, "is", calculator.div(num1, num2))

        elif choice == "4":
            print("Multiplication of numbers", num1, "&", num2, "is", calculator.multiply(num1, num2))
        
        elif choice == "5":
            print("Square of number", num1, "is", calculator.square(num1))
        
        elif choice == "6":
            print("Squareroot of number", num1, "is", calculator.squareroot(num1))
        
        elif choice == "7":
            break

        else:
            print("Invalid choice")