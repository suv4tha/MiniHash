import tkinter as tk
from tkinter import scrolledtext
import hashlib

# Your custom mini hash algorithm (32 chars)
def mini_hash(text):
    h = 0x12345678ABCDEF01
    for ch in text.encode('utf-8'):
        h ^= (ch + 0x9e3779b97f4a7c15 + (h<<6) + (h>>2)) & 0xffffffffffffffff
        h &= 0xffffffffffffffff
    return f"{h:032x}"[:32]   # compress to 32 chars

def sha_256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def bit_diff(a, b):
    x = int(a, 16) ^ int(b, 16)
    return bin(x).count("1")

def compute_hash():
    input_text = entry.get("1.0", tk.END).rstrip("\n")
    mini = mini_hash(input_text)
    sha = sha_256(input_text)
    diff = bit_diff(mini, sha[:32])  # comparing 32 char range

    result.delete("1.0", tk.END)
    result.insert(tk.END, f"Input Text:\n{input_text}\n\n")
    result.insert(tk.END, f"Custom Mini Hash (32 chars):\n{mini}\n\n")
    result.insert(tk.END, f"SHA-256 Hash:\n{sha}\n\n")
    result.insert(tk.END, f"Bit Difference (Mini vs SHA256 32 chars): {diff}\n")

# GUI APP
root = tk.Tk()
root.title("Custom Hash Project - USN: 24msrdf043")

title = tk.Label(root, text="Custom Hash Project", font=("Arial", 16, "bold"))
title.pack(pady=10)

entry_label = tk.Label(root, text="Enter input text:")
entry_label.pack()

entry = scrolledtext.ScrolledText(root, height=5, width=55)
entry.pack(padx=5, pady=5)

btn = tk.Button(root, text="Compute Hash", command=compute_hash)
btn.pack(pady=10)

result_label = tk.Label(root, text="Result Output:")
result_label.pack()

result = scrolledtext.ScrolledText(root, height=15, width=55)
result.pack(padx=5, pady=5)

root.mainloop()
