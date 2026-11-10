import tkinter as tk
from tkinter import messagebox
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("380x560")
        self.root.config(bg="#1e1e2f")  # Sleek deep modern dark background
        
        self.equation = tk.StringVar()
        self.is_degrees = tk.BooleanVar(value=True)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Top Mode Bar Frame
        top_frame = tk.Frame(self.root, bg="#1e1e2f")
        top_frame.pack(fill="x", padx=15, pady=(12, 5))
        
        deg_rad_btn = tk.Checkbutton(
            top_frame, 
            text="Deg Mode", 
            variable=self.is_degrees, 
            font=("Segoe UI", 10, "bold"), 
            bg="#1e1e2f", 
            fg="#a5b4fc", 
            selectcolor="#2d2d44",
            activebackground="#1e1e2f",
            activeforeground="#a5b4fc",
            bd=0
        )
        deg_rad_btn.pack(side="left")
        
        # Display Screen Container
        display_frame = tk.Frame(self.root, bg="#1e1e2f")
        display_frame.pack(fill="x", padx=15, pady=5)
        
        entry = tk.Entry(
            display_frame, 
            textvariable=self.equation, 
            font=("Segoe UI", 28, "bold"), 
            bd=0, 
            justify="right", 
            bg="#2d2d44", 
            fg="#ffffff",
            insertbackground="white"
        )
        entry.pack(fill="x", ipady=12, ipadx=10)
        
        # Buttons Grid Container
        btns_frame = tk.Frame(self.root, bg="#1e1e2f")
        btns_frame.pack(expand=True, fill="both", padx=15, pady=15)
        
        # Button layout definition: (Text, Row, Column)
        buttons = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('sqrt', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^', 5, 3),
            ('log', 6, 0), ('ln', 6, 1), ('π', 6, 2), ('e', 6, 3)
        ]
        
        # Modern color coding for button types
        for (text, row, col) in buttons:
            if text in ('=',):
                bg_color, fg_color, active_bg = "#4f46e5", "#ffffff", "#6366f1"  # Vibrant Indigo for Equals
            elif text in ('C',):
                bg_color, fg_color, active_bg = "#ef4444", "#ffffff", "#f87171"  # Soft Red for Clear
            elif text in ('/', '*', '-', '+', '^', 'sqrt', 'sin', 'cos', 'tan', 'log', 'ln', '(', ')'):
                bg_color, fg_color, active_bg = "#374151", "#93c5fd", "#4b5563"  # Slate Blue-Grey for Operators/Functions
            else:
                bg_color, fg_color, active_bg = "#252f3f", "#ffffff", "#323f56"  # Darker cards for numbers
                
            btn = tk.Button(
                btns_frame, 
                text=text, 
                font=("Segoe UI", 13, "bold"), 
                bd=0, 
                relief=tk.FLAT, 
                bg=bg_color, 
                fg=fg_color,
                activebackground=active_bg,
                activeforeground=fg_color,
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
            
        # Configure uniform grid weights
        for i in range(7):
            btns_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btns_frame.columnconfigure(j, weight=1)
            
    def on_button_click(self, char):
        current = self.equation.get()
        
        if char == 'C':
            self.equation.set("")
            
        elif char == '=':
            try:
                expr = current.replace('^', '**')
                expr = expr.replace('π', str(math.pi))
                expr = expr.replace('e', str(math.e))
                result = str(eval(expr))
                self.equation.set(result)
            except ZeroDivisionError:
                messagebox.showerror("Math Error", "Division by zero is not allowed.")
                self.equation.set("")
            except Exception:
                messagebox.showerror("Syntax Error", "Invalid mathematical expression.")
                self.equation.set("")
                
        elif char == 'sqrt':
            try:
                result = str(math.sqrt(float(eval(current))))
                self.equation.set(result)
            except Exception:
                messagebox.showerror("Error", "Invalid input for square root.")
                self.equation.set("")
                
        elif char in ('sin', 'cos', 'tan'):
            try:
                val = float(eval(current))
                rad = math.radians(val) if self.is_degrees.get() else val
                if char == 'sin': res = math.sin(rad)
                elif char == 'cos': res = math.cos(rad)
                elif char == 'tan': res = math.tan(rad)
                self.equation.set(str(round(res, 6)))
            except Exception:
                messagebox.showerror("Error", "Invalid input for trigonometric function.")
                self.equation.set("")
                
        elif char == 'log':
            try:
                val = float(eval(current))
                self.equation.set(str(round(math.log10(val), 6)))
            except Exception:
                messagebox.showerror("Error", "Invalid input for log (must be > 0).")
                self.equation.set("")
                
        elif char == 'ln':
            try:
                val = float(eval(current))
                self.equation.set(str(round(math.log(val), 6)))
            except Exception:
                messagebox.showerror("Error", "Invalid input for ln (must be > 0).")
                self.equation.set("")
                
        elif char in ('π', 'e'):
            self.equation.set(current + char)
            
        else:
            self.equation.set(current + str(char))

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()