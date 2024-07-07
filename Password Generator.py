import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length should be greater than zero")
        
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack()

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display generated password
password_label = tk.Label(root, text="Generated Password:")
password_label.pack()
password_entry = tk.Entry(root, width=50, justify='center')
password_entry.pack(pady=10)

# Run the main tkinter event loop
root.mainloop()
