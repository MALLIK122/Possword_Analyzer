import tkinter as tk
from tkinter import messagebox
import re
import math

# Password strength checking function
def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) < 6:
        feedback.append("Too short: use at least 8 characters.")
    elif len(password) >= 12:
        strength += 2
    else:
        strength += 1

    # Character checks
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("Add special characters.")

    # Entropy calculation
    entropy = math.log2(len(set(password)) ** len(password)) if password else 0

    # Strength category
    if strength <= 2:
        status = "Weak"
        color = "red"
    elif 3 <= strength <= 4:
        status = "Medium"
        color = "orange"
    else:
        status = "Strong"
        color = "green"

    return status, strength, entropy, feedback, color

# Function when button is clicked
def analyze_password():
    password = entry.get()
    status, score, entropy, feedback, color = check_password_strength(password)

    result_label.config(text=f"Status: {status}", fg=color)
    score_label.config(text=f"Score: {score}/6")
    entropy_label.config(text=f"Entropy: {round(entropy, 2)} bits")

    if feedback:
        suggestions = "\n".join(feedback)
        messagebox.showinfo("Suggestions", suggestions)
    else:
        messagebox.showinfo("Suggestions", "Your password looks strong!")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Strength Analyzer")
root.geometry("400x300")

tk.Label(root, text="Enter a Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Analyze", command=analyze_password, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

result_label = tk.Label(root, text="Status: ", font=("Arial", 12))
result_label.pack()

score_label = tk.Label(root, text="Score: ", font=("Arial", 12))
score_label.pack()

entropy_label = tk.Label(root, text="Entropy: ", font=("Arial", 12))
entropy_label.pack()

root.mainloop()
