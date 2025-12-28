import tkinter as tk
import random

quotes = [
    {"text": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
    {"text": "Success is not final, failure is not fatal.", "author": "Winston Churchill"},
    {"text": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"}
]

def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote["text"])
    author_label.config(text="- " + quote["author"])

root = tk.Tk()
root.title("Random Quote Generator")

quote_label = tk.Label(root, text="", font=("Arial", 14), wraplength=300, justify="center")
quote_label.pack(pady=20)

author_label = tk.Label(root, text="", font=("Arial", 12), fg="gray")
author_label.pack(pady=5)

tk.Button(root, text="New Quote", command=show_quote).pack(pady=10)

show_quote()  # Show a quote when app starts
root.mainloop()