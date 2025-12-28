import tkinter as tk
from tkinter import messagebox
import random

# Sample vocabulary list (Word: Translation)
vocab_data = {
    "Hello": "Hola",
    "Thank you": "Gracias",
    "Please": "Por favor",
    "Goodbye": "Adiós",
    "Yes": "Sí",
    "No": "No",
    "Sorry": "Lo siento",
    "Water": "Agua",
    "Food": "Comida",
    "Friend": "Amigo"
}

# Create the main window
root = tk.Tk()
root.title("Language Learning App")
root.geometry("400x400")
root.resizable(False, False)

# ----------------- Flashcard Section ------------------
def show_flashcard():
    word = random.choice(list(vocab_data.keys()))
    translation = vocab_data[word]
    word_label.config(text=word)
    translation_label.config(text="")

    def show_translation():
        translation_label.config(text=translation)

    show_button.config(command=show_translation)

# ----------------- Quiz Section ------------------
def start_quiz():
    word = random.choice(list(vocab_data.keys()))
    correct_translation = vocab_data[word]
    
    def check_answer():
        user_input = answer_entry.get()
        if user_input.lower() == correct_translation.lower():
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Wrong!", f"The correct answer is: {correct_translation}")

    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quick Test")
    quiz_window.geometry("300x200")
    
    tk.Label(quiz_window, text=f"What is the translation of '{word}'?", font=("Arial", 12)).pack(pady=10)
    answer_entry = tk.Entry(quiz_window)
    answer_entry.pack(pady=5)
    
    tk.Button(quiz_window, text="Submit", command=check_answer).pack(pady=10)

# ----------------- UI Layout ------------------
title = tk.Label(root, text="📘 Language Learning", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

# Flashcard Display
word_label = tk.Label(root, text="", font=("Helvetica", 20))
word_label.pack(pady=20)

translation_label = tk.Label(root, text="", font=("Helvetica", 16), fg="blue")
translation_label.pack()

show_button = tk.Button(root, text="Show Translation", font=("Arial", 12))
show_button.pack(pady=10)

next_button = tk.Button(root, text="Next Word", font=("Arial", 12), command=show_flashcard)
next_button.pack(pady=5)

test_button = tk.Button(root, text="Take a Test", font=("Arial", 12), command=start_quiz)
test_button.pack(pady=15)

# Start with a flashcard
show_flashcard()

# Run the app
root.mainloop()