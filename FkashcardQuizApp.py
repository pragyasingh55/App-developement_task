import tkinter as tk
from tkinter import messagebox

flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Who wrote 'Hamlet'?", "answer": "William Shakespeare"}
]

current_index = 0
showing_answer = False

def show_card():
    global showing_answer
    showing_answer = False
    question_label.config(text=flashcards[current_index]["question"])
    answer_label.config(text="")

def show_answer():
    global showing_answer
    showing_answer = True
    answer_label.config(text=flashcards[current_index]["answer"])

def next_card():
    global current_index
    if current_index < len(flashcards) - 1:
        current_index += 1
        show_card()

def prev_card():
    global current_index
    if current_index > 0:
        current_index -= 1
        show_card()

def add_card():
    q = question_entry.get()
    a = answer_entry.get()
    if q and a:
        flashcards.append({"question": q, "answer": a})
        question_entry.delete(0, tk.END)
        answer_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Flashcard added!")
    else:
        messagebox.showwarning("Input Error", "Please enter both question and answer.")

def delete_card():
    global current_index
    if flashcards:
        flashcards.pop(current_index)
        if current_index >= len(flashcards):
            current_index = max(0, len(flashcards) - 1)
        show_card()

root = tk.Tk()
root.title("Flashcard Quiz App")

question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=300)
question_label.pack(pady=10)

answer_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
answer_label.pack(pady=5)

tk.Button(root, text="Show Answer", command=show_answer).pack()
tk.Button(root, text="Previous", command=prev_card).pack(side=tk.LEFT, padx=20, pady=10)
tk.Button(root, text="Next", command=next_card).pack(side=tk.RIGHT, padx=20, pady=10)
tk.Button(root, text="Delete Flashcard", command=delete_card).pack(pady=10)

# Add flashcard section
tk.Label(root, text="Add New Flashcard").pack(pady=10)
question_entry = tk.Entry(root, width=40)
question_entry.pack(pady=5)
question_entry.insert(0, "Enter question")

answer_entry = tk.Entry(root, width=40)
answer_entry.pack(pady=5)
answer_entry.insert(0, "Enter answer")

tk.Button(root, text="Add Flashcard", command=add_card).pack(pady=10)

show_card()
root.mainloop()78
--