import tkinter as tk
from tkinter import messagebox


class Enigma:
    def __init__(self, rotor1_pos=0, rotor2_pos=0, rotor3_pos=0):
        self.rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        self.rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        self.rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        self.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

        self.rotor1_pos = rotor1_pos
        self.rotor2_pos = rotor2_pos
        self.rotor3_pos = rotor3_pos

        self.inverse_rotor1 = self.inverse(self.rotor1)
        self.inverse_rotor2 = self.inverse(self.rotor2)
        self.inverse_rotor3 = self.inverse(self.rotor3)

    def inverse(self, rotor):
        inverse_rotor = [0] * 26
        for i in range(26):
            inverse_rotor[rotor[i]] = i
        return inverse_rotor

    def encrypt_decrypt_char(self, ch):
        if ch.isalpha():
            is_lower = ch.islower()
            ch = ch.upper()

            offset = ord(ch) - ord('A')
            offset = (self.rotor1[(offset + self.rotor1_pos) % 26] - self.rotor1_pos) % 26
            offset = (self.rotor2[(offset + self.rotor2_pos) % 26] - self.rotor2_pos) % 26
            offset = (self.rotor3[(offset + self.rotor3_pos) % 26] - self.rotor3_pos) % 26
            offset = self.reflector[offset]
            offset = (self.inverse_rotor3[(offset + self.rotor3_pos) % 26] - self.rotor3_pos) % 26
            offset = (self.inverse_rotor2[(offset + self.rotor2_pos) % 26] - self.rotor2_pos) % 26
            offset = (self.inverse_rotor1[(offset + self.rotor1_pos) % 26] - self.rotor1_pos) % 26

            self.rotor1_pos = (self.rotor1_pos + 1) % 26
            if self.rotor1_pos == 0:
                self.rotor2_pos = (self.rotor2_pos + 1) % 26
                if self.rotor2_pos == 0:
                    self.rotor3_pos = (self.rotor3_pos + 1) % 26

            result = chr(offset + ord('A'))
            return result.lower() if is_lower else result
        else:
            return ch

    def process(self, text):
        return ''.join(self.encrypt_decrypt_char(ch) for ch in text)


class EnigmaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Cipher")
        self.root.geometry("400x400")
        self.root.configure(bg="#2B2B2B")

        # Title
        title = tk.Label(root, text="Enigma Cipher", font=("Arial", 16, "bold"), bg="#2B2B2B", fg="white")
        title.pack(pady=10)

        # Input
        self.input_label = tk.Label(root, text="Input Text:", bg="#2B2B2B", fg="white")
        self.input_label.pack()
        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.pack(pady=5)

        # Rotor positions
        self.rotor1_label = tk.Label(root, text="Rotor 1 Position:", bg="#2B2B2B", fg="white")
        self.rotor1_label.pack()
        self.rotor1_entry = tk.Entry(root, width=5)
        self.rotor1_entry.pack(pady=5)

        self.rotor2_label = tk.Label(root, text="Rotor 2 Position:", bg="#2B2B2B", fg="white")
        self.rotor2_label.pack()
        self.rotor2_entry = tk.Entry(root, width=5)
        self.rotor2_entry.pack(pady=5)

        self.rotor3_label = tk.Label(root, text="Rotor 3 Position:", bg="#2B2B2B", fg="white")
        self.rotor3_label.pack()
        self.rotor3_entry = tk.Entry(root, width=5)
        self.rotor3_entry.pack(pady=5)

        # Buttons
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt, bg="#6A5ACD", fg="white", width=10)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt, bg="#6A5ACD", fg="white", width=10)
        self.decrypt_button.pack(pady=5)

        # Output
        self.output_label = tk.Label(root, text="Output:", bg="#2B2B2B", fg="white")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=5, width=40, bg="#333333", fg="white")
        self.output_text.pack(pady=10)

    def encrypt(self):
        text = self.input_entry.get()
        rotor1 = int(self.rotor1_entry.get() or 0)
        rotor2 = int(self.rotor2_entry.get() or 0)
        rotor3 = int(self.rotor3_entry.get() or 0)
        enigma = Enigma(rotor1, rotor2, rotor3)
        encrypted_text = enigma.process(text)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, encrypted_text)

    def decrypt(self):
        text = self.input_entry.get()
        rotor1 = int(self.rotor1_entry.get() or 0)
        rotor2 = int(self.rotor2_entry.get() or 0)
        rotor3 = int(self.rotor3_entry.get() or 0)
        enigma = Enigma(rotor1, rotor2, rotor3)
        decrypted_text = enigma.process(text)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, decrypted_text)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaApp(root)
    root.mainloop()
