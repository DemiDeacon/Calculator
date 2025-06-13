import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")


def click():
    pass


# Создаем кнопки
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    btn = tk.Button(root, text=button, font=('Arial', 18), width=4, height=2)
    btn.grid(row=row_val, column=col_val)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Запускаем главный цикл
root.mainloop()

