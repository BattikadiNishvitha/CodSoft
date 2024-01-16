class AdvancedCalculator:
    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero")

    def modulus(self, x, y):
        if y != 0:
            return x % y
        else:
            raise ValueError("Cannot perform modulus with zero divisor")

    def power(self, x, y):
        return x ** y

    def memory_add(self, x):
        self.memory += x

    def memory_subtract(self, x):
        self.memory -= x

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

    def calculator(self):
        print("Advanced Calculator with Modulus")

        while True:
            try:
                print("\nSelect operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Modulus")
                print("6. Power")
                print("7. Memory Add (M+)")
                print("8. Memory Subtract (M-)")
                print("9. Memory Recall (MR)")
                print("10. Memory Clear (MC)")
                print("11. Exit")

                choice = input("Enter choice (1-11): ")

                if choice == '11':
                    print("Exiting the calculator. Goodbye!")
                    break

                if choice in ('1', '2', '3', '4', '5', '6'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(f"{num1} + {num2} = {self.add(num1, num2)}")
                    elif choice == '2':
                        print(f"{num1} - {num2} = {self.subtract(num1, num2)}")
                    elif choice == '3':
                        print(f"{num1} * {num2} = {self.multiply(num1, num2)}")
                    elif choice == '4':
                        result = self.divide(num1, num2)
                        print(f"{num1} / {num2} = {result}")
                    elif choice == '5':
                        result = self.modulus(num1, num2)
                        print(f"{num1} % {num2} = {result}")
                    elif choice == '6':
                        print(f"{num1} ^ {num2} = {self.power(num1, num2)}")

                elif choice in ('7', '8', '9', '10'):
                    if choice == '7':
                        num = float(input("Enter a number to add to memory (M+): "))
                        self.memory_add(num)
                        print(f"{num} added to memory.")
                    elif choice == '8':
                        num = float(input("Enter a number to subtract from memory (M-): "))
                        self.memory_subtract(num)
                        print(f"{num} subtracted from memory.")
                    elif choice == '9':
                        print(f"Memory Recall (MR): {self.memory_recall()}")
                    elif choice == '10':
                        self.memory_clear()
                        print("Memory cleared.")

                else:
                    print("Invalid input. Please enter a valid choice.")

                another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
                if another_calculation != 'yes':
                    print("Exiting the calculator. Goodbye!")
                    break

            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calc = AdvancedCalculator()
    calc.calculator()
