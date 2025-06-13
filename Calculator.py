class Calculator:

    def __init__(self):
        pass

    # standard operations
    def addition(self, first_number, second_number):
        return first_number + second_number
    
    def multiplication(self, first_number, second_number):
        return first_number * second_number
    
    def subtraction(self, first_number, second_number):
        return first_number - second_number
    
    def division(self, first_number, second_number):
        return first_number / second_number
    
calc = Calculator.addition(4,5)
print(calc)




# class Calculator:

#     def __init__(self):
#         pass

#     # standard operations
#     def addition(self, first_number, second_number):
#         return first_number + second_number
    
#     def multiplication(self, first_number, second_number):
#         return first_number * second_number
    
#     def subtraction(self, first_number, second_number):
#         return first_number - second_number  # Corrected from division to subtraction
    
#     def division(self, first_number, second_number):
#         if second_number == 0:
#             return "Error: Division by zero"  # Handle division by zero
#         return first_number / second_number  # Corrected from subtraction to division

# # Create an instance of the Calculator class
# calc = Calculator()

# # Perform addition
# summ = calc.addition(4, 5)
# print(summ)  # Output: 9
