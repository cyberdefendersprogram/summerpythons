from types import NotImplementedType
class Calculator:
    def __init__(self, a: float):
        self.result = a

    def calculate(self, op: str, b: float):
        if op == '+':
            self.result += b
        elif op == '-':
            self.result -= b
        elif op == '*':
            self.result *= b
        elif op == '/':
            if b != 0:
                self.result /= b
            else:
                return "Cannot divide by zero"
        elif op == '**':
            self.result **= b
        else:
            return f'Op "{op}" is not a valid operation'
        return None  # Return None after successful calculation

    def get_result(self):
        return self.result


def user_input_loop():
    tryagain = 'y'
    while tryagain == 'y':
        print("Basic calculator does +, -, /, *, ** on a running total!")
        a_str = input("Please input the starting number: ")
        try:
            a = float(a_str)
        except ValueError:
            print("That's a strange looking number...")
            continue
        calculator = Calculator(a)
        while True:
            op = input("Please enter the operation (+, -, /, *, **) or 'q' to quit: ")
            if op == 'q':
                break
            b_str = input(f"Please enter the number for operation '{op}': ")
            try:
                b = float(b_str)
            except ValueError:
                print("Something doesn't look right...")
                continue
            try:
                error_message = calculator.calculate(op, b)
                if error_message is not None:
                    print(error_message)
                else:
                    print("Current Result:", calculator.get_result())
            except ZeroDivisionError:
                print("Cannot divide by zero")
            except Exception as e:
                print("An error occurred:", str(e))
                print("Your calculation seems off, let's try again.")
        tryagain = input("Do you want to continue? (y/n): ")


def test_calculate(name: str, condition: bool):
    if condition:
        print(name + " passed!")
    else:
        print(name + " failed!")


def test_calculator_class():
    test = Calculator(2)
    test_calculate("Addition test", test.calculate("+", 2) == None)
    test_calculate("Subtraction test", test.calculate("-", 2) == None)
    test_calculate("Multiplication test", test.calculate("*", 2) == None)
    test_calculate("Division test", test.calculate("/", 2) == None)
    test_calculate("Exponents test", test.calculate("**", 2) == None)

    # Additional test case for third arithmetic operation
    test.calculate("+", 3)
    test_calculate("Addition test", test.get_result() == 2 + 2 + 3)



if __name__ == "__main__":
    test_calculator_class()
    user_input_loop()
