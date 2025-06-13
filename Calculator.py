# class Calculator:

#     def __init__(self):
#         pass

#     # standard operations
#     def addition(self, first_number, second_number):
#         return first_number + second_number
    
#     def multiplication(self, first_number, second_number):
#         return first_number * second_number
    
#     def subtraction(self, first_number, second_number):
#         return first_number - second_number
    
#     def division(self, first_number, second_number):
#         try:
#             return first_number / second_number
#         except ZeroDivisionError:
#             return "Error: Division by zero"
        

# calc = Calculator()
# summ = calc.division(4,0)
# print(summ)






from tkinter import *
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
btn = Button(text="Hello")
btn.pack()
 
 
def print_info(widget, depth=0):
    widget_class=widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   "*depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth+1)
 
root.update()     # обновляем информацию о виджетах
 
print_info(root)
 
root.mainloop()

