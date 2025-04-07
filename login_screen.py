import tkinter as tk
from tkinter import messagebox
from constants import students, teachers

def login():
    username = username_entry.get()
    password = password_entry.get()

    for user in students + teachers:
        if user.username == username and user.password == password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}! You are logged in as a {user.role}.")
            return

    messagebox.showerror("Login Failed", "Invalid username or password.")

# Create window
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Username
tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

# Password
tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()