import tkinter as tk
from tkinter import *
import random

response_list = [
    "It is certain", "It is decidedly so", "Without a doubt", 
    "Yes! Definitely!", "You may rely on it", "As I see it, yes",
    "Most likely", "Outlook good", "Yes", "Signs point to yes",
    "Don't count on it", "My reply is no", "My sources say no",
    "Outlook not so good", "Very doubtful", "Reply hazy, try again",
    "Ask again later", "Better not tell you now", 
    "Cannot predict now", "Concentrate and ask again"
]

root = tk.Tk()
root.title("Magic ⓼ Ball")
root.geometry("600x600")
root.configure(bg="black")
root.resizable(False, False)

def show_goodbye():
    for widget in root.winfo_children():
        widget.destroy()
    
    goodbye_frame = tk.Frame(root, bg="black")
    goodbye_frame.pack(pady=10)

    goodbye_label = tk.Label(goodbye_frame, text="Goodbye", height=5, fg="white", bg="black", font=("Harmond", 40, "italic"))
    goodbye_label.pack(pady=10)

    thank_label = tk.Label(goodbye_frame, text="Thanks for playing with the Magic ⓼ Ball!", height=6, fg="white", bg="black", font=("Harmond", 20,"italic"))
    thank_label.pack(pady=10)
    
    root.after(1200, root.destroy)

def shake():
    question = entry.get().strip()
    if not question:
        response_label.config(text="Type a question to get a response", font=("Harmond", 18, "normal"))
    elif question.lower() == "exit":
        show_goodbye()
    else:
        response_label.config(text="Shaking...", font=("Harmond", 18, "italic"))
        root.after(800, lambda: display_response(question))

def display_response(question):
    response = random.choice(response_list)
    response_label.config(text=response, font=("Harmond", 20, "bold"))
    
    entry.delete(0, tk.END)

def clear_response(event):
    response_label.config(text="")


main_frame = tk.Frame(root, bg="black")
main_frame.pack(pady=10)

greeting = tk.Label(main_frame, text="""Welcome to Magic ⓼ Ball\nEnter your question, and press to get your response\nType 'exit' to leave\n""", fg="white", bg="black", font=("Harmond", 18, "italic"))
greeting.pack(pady=5)

ball = tk.Label(main_frame, text="⓼", fg="white", bg="black", font=("Harmond", 100))
ball.pack(pady=10)

question_label = tk.Label(main_frame, text="Type your question: ", fg="white", bg="black", font=("Harmond", 18, "bold"))
question_label.pack()

entry = tk.Entry(main_frame, fg="white", bg="black", font=("Harmond", 18))
entry.pack(pady=15)

response_label = tk.Label(main_frame, text="", fg="white", bg="black", font=("Harmond", 25, "bold"))
response_label.pack(pady=30)

button_frame = tk.Frame(main_frame, bg="black")
button_frame.pack()

button = tk.Button(button_frame, text="SHAKE", width=10, height=2, bg="white", fg="black", command=shake, font=("Harmond", 14))
button.pack(pady=10)

entry.bind('<Return>', lambda event: shake())
entry.bind('<KeyPress>', clear_response)

root.mainloop()

