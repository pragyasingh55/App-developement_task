import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# --- Setup SQLite Database ---
conn = sqlite3.connect('fitness_tracker.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS fitness (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity TEXT,
        duration INTEGER,
        calories INTEGER
    )
''')
conn.commit()

# --- GUI Setup ---
root = tk.Tk()
root.title("Fitness Tracker App")
root.geometry("500x600")
root.config(bg="#f5f5f5")

title_label = tk.Label(root, text="Fitness Tracker", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

# --- Entry Section ---
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

tk.Label(frame, text="Activity:", bg="#f5f5f5").grid(row=0, column=0, sticky='e')
activity_entry = tk.Entry(frame, width=30)
activity_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Duration (min):", bg="#f5f5f5").grid(row=1, column=0, sticky='e')
duration_entry = tk.Entry(frame, width=30)
duration_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Calories Burned:", bg="#f5f5f5").grid(row=2, column=0, sticky='e')
calories_entry = tk.Entry(frame, width=30)
calories_entry.grid(row=2, column=1, padx=10, pady=5)

# --- Functions ---
def add_entry():
    activity = activity_entry.get()
    duration = duration_entry.get()
    calories = calories_entry.get()

    if not activity or not duration.isdigit() or not calories.isdigit():
        messagebox.showerror("Invalid Input", "Please enter valid data.")
        return

    c.execute("INSERT INTO fitness (activity, duration, calories) VALUES (?, ?, ?)",
              (activity, int(duration), int(calories)))
    conn.commit()

    activity_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)
    calories_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Entry added successfully!")

def view_entries():
    view_win = tk.Toplevel(root)
    view_win.title("Fitness Log")
    view_win.geometry("400x300")

    tree = ttk.Treeview(view_win, columns=("Activity", "Duration", "Calories"), show='headings')
    tree.heading("Activity", text="Activity")
    tree.heading("Duration", text="Duration (min)")
    tree.heading("Calories", text="Calories")
    tree.pack(expand=True, fill='both')

    c.execute("SELECT activity, duration, calories FROM fitness")
    for row in c.fetchall():
        tree.insert('', tk.END, values=row)

def show_summary():
    c.execute("SELECT SUM(duration), SUM(calories) FROM fitness")
    total_duration, total_calories = c.fetchone()
    total_duration = total_duration if total_duration else 0
    total_calories = total_calories if total_calories else 0

    messagebox.showinfo("Summary",
        f"Total Duration: {total_duration} minutes\nTotal Calories Burned: {total_calories} kcal")

# --- Buttons ---
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Add Entry", width=20, command=add_entry, bg="#4CAF50", fg="white").grid(row=0, column=0, pady=5)
tk.Button(btn_frame, text="View All Entries", width=20, command=view_entries, bg="#2196F3", fg="white").grid(row=1, column=0, pady=5)
tk.Button(btn_frame, text="Show Summary", width=20, command=show_summary, bg="#FF9800", fg="white").grid(row=2, column=0, pady=5)

# --- Run App ---
root.mainloop()
conn.close()