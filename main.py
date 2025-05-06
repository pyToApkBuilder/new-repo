import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        height_m = height_cm / 100 
        bmi = weight / (height_m ** 2)
        upper = (height_m ** 2) * 24.9 
        lower = (height_m ** 2) * 18.5 
        category,range = get_bmi_category(bmi)
        result_label.config(text=f"\nBMI: {bmi:.2f} ({range})\n")
        if category != "Normal weight":
            category_label.config(text=f"Category: {category} \nShould be between {lower:.1f} and {upper:.1f}")
        else:
            category_label.config(text=f"Category: {category}")
            
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def get_bmi_category(bmi):
    if bmi < 18.5:
        category_label.config(fg="#ff4321")
        return "Underweight","Bellow 18.5"
        
    elif bmi < 24.9:
        category_label.config(fg="green")
        return "Normal weight","18.6 To 24.9"
        
    elif bmi < 29.9:
        category_label.config(fg="#ff9900")
        return "Overweight", "25.0 to 29.9"
    else:
        category_label.config(fg="red")
        return "Obese","30 or higher"

root = tk.Tk()
root.title("BMI Calculator")
root.configure(bg="#1e1e1e")  # dark background

style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#1e1e1e", foreground="white")
style.configure("TButton", background="#333", foreground="white")
style.configure("TEntry", fieldbackground="#333", foreground="white")

ttk.Label(root, text="Height (cm):").pack(pady=5)
height_entry = ttk.Entry(root)
height_entry.pack()

ttk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = ttk.Entry(root)
weight_entry.pack()

ttk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="\n Healthy BMI range\n 18.5 and 24.9", font=('Arial', 12), bg="#1e1e1e", fg="white")
result_label.pack()

category_label = tk.Label(root, text="", font=('Arial', 12), bg="#1e1e1e", fg="white")
category_label.pack()

root.mainloop()
