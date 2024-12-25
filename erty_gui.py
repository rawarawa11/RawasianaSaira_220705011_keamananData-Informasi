import os
from stegano import lsb
import tkinter as tk
from tkinter import filedialog, messagebox


def get_image_path():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
    return file_path

def save_image():
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    return save_path

def hide_message_gui():
    img_path = get_image_path()
    if not img_path:
        messagebox.showwarning("Error", "Path gambar tidak valid.")
        return

    message = message_entry.get()
    if not message:
        messagebox.showwarning("Error", "Pesan tidak boleh kosong.")
        return

    try:
        secret = lsb.hide(img_path, message)
        save_path = save_image()
        if save_path:
            secret.save(save_path)
            messagebox.showinfo("Sukses", f"Pesan berhasil disembunyikan di: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyembunyikan pesan: {e}")

def show_message_gui():
    img_path = get_image_path()
    if not img_path:
        messagebox.showwarning("Error", "Path gambar tidak valid.")
        return

    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {clear_message}")
        else:
            messagebox.showinfo("Tidak Ada Pesan", "Tidak ada pesan tersembunyi dalam gambar.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menampilkan pesan dari gambar: {e}")

def create_gui():
    global message_entry

    # Setup Window
    window = tk.Tk()
    window.title("Steganography Tool - GUI Version")
    window.geometry("400x300")

    # Label Title
    title_label = tk.Label(window, text="Steganography Tool", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Message Input
    message_label = tk.Label(window, text="Pesan untuk Disembunyikan:", font=("Arial", 12))
    message_label.pack(pady=5)

    message_entry = tk.Entry(window, width=50, font=("Arial", 12))
    message_entry.pack(pady=5)

    # Buttons
    hide_button = tk.Button(window, text="Sembunyikan Pesan", font=("Arial", 12), bg="lightblue", command=hide_message_gui)
    hide_button.pack(pady=10)

    reveal_button = tk.Button(window, text="Tampilkan Pesan", font=("Arial", 12), bg="lightgreen", command=show_message_gui)
    reveal_button.pack(pady=10)

    exit_button = tk.Button(window, text="Keluar", font=("Arial", 12), bg="lightcoral", command=window.quit)
    exit_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
