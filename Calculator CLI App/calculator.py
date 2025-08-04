class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        if self.num2 == 0:
            return "Error: Number cannot divided by Zero"
        else:
            return self.num1 / self.num2

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter First Number:> "))
            num2 = float(input("Enter Second Number:>"))
            return num1,num2
        except ValueError:
            print("Invalid input! Please enter numeric values..")
print("Welcome to My Calculator CLI App...")
num1, num2 = get_numbers()
Evaluate = Calculator(num1,num2)

while True:
    print("\nChoose Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    user_choice = input("Enter Your Choice(1/2/3/4/5):> ")

    if user_choice == "5":
        print("You are Exiting Calculator App..\nThanks for visting...")
        break
    if user_choice in ["1","2","3","4"]:
        if user_choice == "1":
            print("result:> ",Evaluate.add())
        elif user_choice == "2":
            print("Result:> ",Evaluate.subtract())
        elif user_choice == "3":
            print("Result:> ",Evaluate.multiply())
        elif user_choice == "4":
            print("Result:> ",Evaluate.divide())
        else:
            print("Invalid Choice...Try Again")
            continue
        # Asking user to perform another operation on given values or else want perform opertion on new values   
        continue_choice = input("\nDo you want to perform another operation? (yes/no:> )").lower()
        if continue_choice == "yes":
            reuse_choice = input("Do you want to use the same numbers? (yes/no):> ").lower()
            if reuse_choice == "no":
                num1, num2 = get_numbers()
                Evaluate = Calculator(num1,num2)
        else:
            print("Thanks for using the calculator App")
            break