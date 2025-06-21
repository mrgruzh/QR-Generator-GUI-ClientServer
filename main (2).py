import tkinter as tk
import subprocess
import os


def display_image():
    image_path = "client/qr.png"
    img = tk.PhotoImage(file=image_path)
    image_label.config(image=img)
    image_label.image = img


def generate_qr():
    input_text = input_field.get()
    if not input_text.strip():
        message_label.config(text="Input field cannot be empty.", fg="red")
        return

    if os.path.isfile('client/qr.png'):
        os.remove('client/qr.png')
    input_text = input_field.get()
    result = subprocess.call(["python", "client/client.py", input_text])
    if result != 0:
        message_label.config(text="QR code generating failed!", fg="red")
    else:
        display_image()
        message_label.config(text="QR code generated successfully!", fg="green")


root = tk.Tk()
root.title("Generate QR")

container = tk.Frame(root, bg="white", padx=20, pady=20, bd=1, relief=tk.SOLID)
container.pack(padx=20, pady=50)

header = tk.Label(container, text="Generate QR", font=("Arial", 18), pady=10, bg="white")
header.pack()

input_field = tk.Entry(container, width=40, font=("Arial", 12), bd=1, relief=tk.SOLID)
input_field.pack(pady=10)

generate_button = tk.Button(container, text="Generate", bg="#4CAF50", fg="white", bd=0, padx=20, pady=10,
                            font=("Arial", 12), command=generate_qr)
generate_button.pack()

message_label = tk.Label(container, text="", font=("Arial", 12), pady=10, bg="white")
message_label.pack()

image_label = tk.Label(container, bg="white")
image_label.pack(pady=10)

root.mainloop()
