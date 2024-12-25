from tkinter import Tk, Label, Entry, Button, Text, messagebox, END, Frame
from Crypto.Cipher import DES
import base64


def pad(text):
    while len(text) % 8 != 0:
        text += ' '  
    return text

def encrypt():
    plain_text = input_text.get("1.0", END).strip()
    key_input = key_entry.get()

    if len(key_input) != 8:
        messagebox.showerror("Error", "Kunci harus memiliki panjang tepat 8 karakter.")
        return

    try:
        key = key_input.encode('utf-8')
        des = DES.new(key, DES.MODE_ECB)
        padded_text = pad(plain_text)
        encrypted_text = des.encrypt(padded_text.encode('utf-8'))
        encoded_text = base64.b64encode(encrypted_text).decode('utf-8')

        output_text.delete("1.0", END)
        output_text.insert("1.0", encoded_text)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def decrypt():
    encrypted_text = input_text.get("1.0", END).strip()
    key_input = key_entry.get()

    if len(key_input) != 8:
        messagebox.showerror("Error", "Kunci harus memiliki panjang tepat 8 karakter.")
        return

    try:
        key = key_input.encode('utf-8')
        des = DES.new(key, DES.MODE_ECB)
        decoded_encrypted_text = base64.b64decode(encrypted_text)
        decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')

        output_text.delete("1.0", END)
        output_text.insert("1.0", decrypted_text.strip())
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def clear_text():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)
    key_entry.delete(0, END)

# Membuat GUI
root = Tk()
root.title("Aplikasi DES Sederhana")
root.geometry("400x350")  
root.config(bg="#2e2e2e")  

# Frame untuk elemen-elemen
frame = Frame(root, bg="#2e2e2e")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Label dan Entry untuk Key
Label(frame, text="Kunci (8 karakter):", font=("Arial", 12), bg="#2e2e2e", fg="#ffffff").grid(row=0, column=0, padx=10, pady=5)
key_entry = Entry(frame, width=30, font=("Arial", 12), bd=2, relief="solid", bg="#333333", fg="white")
key_entry.grid(row=0, column=1, padx=10, pady=5)

# Text Box untuk Input
Label(frame, text="Teks Masukan:", font=("Arial", 12), bg="#2e2e2e", fg="#ffffff").grid(row=1, column=0, padx=10, pady=5)
input_text = Text(frame, height=5, width=40, font=("Arial", 12), bd=2, relief="solid", bg="#333333", fg="white")
input_text.grid(row=1, column=1, padx=10, pady=5)

# Tombol Enkripsi dan Dekripsi
Button(frame, text="Enkripsi", command=encrypt, width=20, font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, relief="solid").grid(row=2, column=0, padx=10, pady=10)
Button(frame, text="Dekripsi", command=decrypt, width=20, font=("Arial", 12), bg="#2196F3", fg="white", bd=0, relief="solid").grid(row=2, column=1, padx=10, pady=10)

# Text Box untuk Output
Label(frame, text="Hasil:", font=("Arial", 12), bg="#2e2e2e", fg="#ffffff").grid(row=3, column=0, padx=10, pady=5)
output_text = Text(frame, height=5, width=40, font=("Arial", 12), bd=2, relief="solid", bg="#333333", fg="white")
output_text.grid(row=3, column=1, padx=10, pady=5)

# Tombol untuk Membersihkan
Button(frame, text="Bersihkan", command=clear_text, width=20, font=("Arial", 12), bg="#f44336", fg="white", bd=0, relief="solid").grid(row=4, column=0, columnspan=2, pady=20)

#jalankan gui
root.mainloop()
