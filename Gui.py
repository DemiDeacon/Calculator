import tkinter as tk

def click(event):
    current = entry.get()
    
    if event.widget.cget("text") == "=":
        try:
            # Используем eval с ограничениями
            result = eval(current, {"__builtins__": None}, {})
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка: Деление на ноль")
        except SyntaxError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка: Неверный синтаксис")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif event.widget.cget("text") == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, event.widget.cget("text"))

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")

# Создаем поле ввода
entry = tk.Entry(root, font=('Arial', 18), width=15)
entry.grid(row=0, column=0, columnspan=4, pady=10)  # Используем grid для поля ввода

# Определяем кнопки
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Инициализация переменных для размещения кнопок
row_val = 1
col_val = 0

# Создаем кнопки и размещаем их в сетке
for button in buttons:
    btn = tk.Button(root, text=button, font=('Arial', 18), width=4, height=2)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Запускаем главный цикл
root.mainloop()
