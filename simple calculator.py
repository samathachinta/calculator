import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")

        self.result_var = tk.StringVar()
        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '^', 'M+',
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                btn = tk.Button(self.root, text=button, padx=20, pady=20, bd=8, font=('Arial', 18),
                                command=self.evaluate)
            elif button == 'C':
                btn = tk.Button(self.root, text=button, padx=20, pady=20, bd=8, font=('Arial', 18),
                                command=self.clear)
            elif button == '√':
                btn = tk.Button(self.root, text=button, padx=20, pady=20, bd=8, font=('Arial', 18),
                                command=self.sqrt)
            elif button == '^':
                btn = tk.Button(self.root, text=button, padx=20, pady=20, bd=8, font=('Arial', 18),
                                command=lambda: self.button_click('**'))
            elif button == 'M+':
                btn = tk.Button(self.root, text=button, padx=20, pady=20, bd=8, font=('Arial', 18),
                                command=self.memory_add)
            else:
                btn = tk.Button(self.root, text=button, padx=20, pady=20, bd=8, font=('Arial', 18),
                                command=lambda b=button: self.button_click(b))

            btn.grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        self.expression += str(value)
        self.result_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.result_var.set("")

    def sqrt(self):
        try:
            result = str(math.sqrt(float(self.expression)))
            self.result_var.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")
            self.clear()

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.result_var.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")
            self.clear()

    def memory_add(self):
        try:
            result = str(eval(self.expression))
            self.result_var.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
