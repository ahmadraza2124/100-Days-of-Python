import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path
from datetime import datetime

# Character sets
alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ['!', '@', '$', '%', '^', '&', '*', '(', ')']

# Track last generated password
last_password = ""

# Generate password function
def generate_password():
    global last_password

    try:
        num_letters = int(entry_letters.get())
        num_symbols = int(entry_symbols.get())
        num_numbers = int(entry_numbers.get())

        password = []

        for _ in range(num_letters):
            password.append(random.choice(alphabet))
        for _ in range(num_symbols):
            password.append(random.choice(symbols))
        for _ in range(num_numbers):
            password.append(random.choice(numbers))

        random.shuffle(password)
        final_password = ''.join(password)
        last_password = final_password

        entry_result.config(state='normal')
        entry_result.delete(0, tk.END)
        entry_result.insert(0, final_password)
        entry_result.config(state='readonly')

        password_length_label.config(text=f"Length: {len(final_password)}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")

# Copy password to clipboard
def copy_to_clipboard():
    if not last_password:
        messagebox.showwarning("No Password", "Please generate a password first.")
        return
    root.clipboard_clear()
    root.clipboard_append(last_password)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Save password to file on Desktop
def save_to_file():
    if not last_password:
        messagebox.showwarning("No Password", "Please generate a password first.")
        return

    try:
        desktop_path = Path.home() / "Desktop"
        file_path = desktop_path / "saved_passwords.txt"

        with open(file_path, "a") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {last_password}\n")

        messagebox.showinfo("Saved", f"Password saved to:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save password:\n{e}")

# GUI setup
root = tk.Tk()
root.title("🔐 PyPassword Generator by Ahmad Raza")
root.geometry("440x360")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

# Style
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10), padding=6)

# Main frame
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Entry labels & fields
ttk.Label(frame, text="How many letters?").grid(column=0, row=0, sticky="w", pady=5)
entry_letters = ttk.Entry(frame, width=10, justify="center")
entry_letters.grid(column=1, row=0)

ttk.Label(frame, text="How many symbols?").grid(column=0, row=1, sticky="w", pady=5)
entry_symbols = ttk.Entry(frame, width=10, justify="center")
entry_symbols.grid(column=1, row=1)

ttk.Label(frame, text="How many numbers?").grid(column=0, row=2, sticky="w", pady=5)
entry_numbers = ttk.Entry(frame, width=10, justify="center")
entry_numbers.grid(column=1, row=2)

# Buttons
ttk.Button(frame, text="Generate Password", command=generate_password).grid(column=0, row=3, columnspan=2, pady=15)
entry_result = ttk.Entry(frame, font=("Segoe UI", 12), width=35, justify="center", state='readonly')
entry_result.grid(column=0, row=4, columnspan=2, pady=(0, 10))

ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard).grid(column=0, row=5, columnspan=2, pady=(0, 5))
ttk.Button(frame, text="Save to Desktop", command=save_to_file).grid(column=0, row=6, columnspan=2)

password_length_label = ttk.Label(frame, text="Length: 0", font=("Segoe UI", 9, "italic"))
password_length_label.grid(column=0, row=7, columnspan=2, pady=(10, 0))

# Run app
root.mainloop()
