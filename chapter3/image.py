import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Menjalankan loop acara Tkinter


from PIL import Image, ImageTk

# Memuat gambar menggunakan Pillow
image = Image.open('sho.jpg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()