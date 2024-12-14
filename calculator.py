import tkinter as tk
from tkinter import messagebox

# Backend: Calculator Logic
def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return "Error"

# Frontend: GUI Application
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        # Entry Widget for Display
        self.display = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Button Layout
        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        # Create Buttons
        for text, row, col, colspan in [(btn[0], btn[1], btn[2], btn[3] if len(btn) > 3 else 1) for btn in button_texts]:
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            self.expression = evaluate_expression(self.expression)
        else:
            self.expression += str(char)

        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
