import socket
import tkinter as tk
from threading import Thread

def receive_messages():
    while True:
        message = client_socket.recv(1024).decode()
        text_box.insert(tk.END, message + '\n')

def send_message(event=None):
    message = entry.get()
    entry.delete(0, tk.END)
    client_socket.send(message.encode())

def start_server():
    global client_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(1)
    client_socket, _ = server_socket.accept()
    receive_thread = Thread(target=receive_messages)
    receive_thread.start()

app = tk.Tk()
app.title("Computer B")

text_box = tk.Text(app)
text_box.pack()

entry = tk.Entry(app)
entry.pack()
entry.bind("<Return>", send_message)

send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack()

start_server()

app.mainloop()
