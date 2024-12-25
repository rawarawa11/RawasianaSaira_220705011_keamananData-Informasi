import tkinter as tk
from tkinter import messagebox

def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def process_text():
    try:
        shift = int(shift_entry.get())
        text = text_entry.get("1.0", "end-1c")
        if shift_mode.get() == "Encrypt":
            result = enkripsi(text, shift)
        else:
            result = dekripsi(text, shift)
        output_text.delete("1.0", "end")
        output_text.insert("1.0", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

# Set up the main application window
root = tk.Tk()
root.title("Caesar Cipher Encryption Machine")
root.state("zoomed")  # Maximize the window on Windows

# Set background color for the main window
root.configure(bg="#2b2b2b")  # Dark background color

# Styles
label_font = ("Arial", 12, "bold")
text_font = ("Arial", 10)
bg_color = "#2b2b2b"  # Main background color
fg_color = "#ffffff"  # White text color
entry_bg = "#333333"  # Entry field background
entry_fg = "#00ff00"  # Light green text color for entries

# Shift Value Entry
tk.Label(root, text="Set Shift Value:", font=label_font, bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10, pady=10, sticky="w")
shift_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=text_font)
shift_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Text Entry for Encryption/Decryption
tk.Label(root, text="Input Text to Encrypt/Decrypt:", font=label_font, bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=10, pady=10, sticky="w")
text_entry = tk.Text(root, height=10, width=80, bg=entry_bg, fg=entry_fg, font=text_font)
text_entry.grid(row=1, column=1, padx=10, pady=10)

# Output Section
tk.Label(root, text="Output:", font=label_font, bg=bg_color, fg=fg_color).grid(row=3, column=0, padx=10, pady=10, sticky="w")
output_text = tk.Text(root, height=10, width=80, bg=entry_bg, fg=entry_fg, font=text_font)
output_text.grid(row=3, column=1, padx=10, pady=10)

# Radio Buttons for Encrypt/Decrypt Mode
shift_mode = tk.StringVar()
shift_mode.set("Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=shift_mode, value="Encrypt", font=label_font, bg=bg_color, fg=fg_color, selectcolor=entry_bg).grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Decrypt", variable=shift_mode, value="Decrypt", font=label_font, bg=bg_color, fg=fg_color, selectcolor=entry_bg).grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Process Button
process_button = tk.Button(root, text="Process Text", command=process_text, font=label_font, bg="#4CAF50", fg=fg_color)
process_button.grid(row=4, column=1, padx=10, pady=10)

# Start the application
root.mainloop()
