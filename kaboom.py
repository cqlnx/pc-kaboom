import webbrowser
import tkinter as tk
from tkinter import messagebox

class WebsiteOpenerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ARVUTI KABOOMER")
        self.url = 'https://www.google.com/'
        self.opened_count = 0
        self.cooldown = 1.0  # Default cooldown in seconds
        self.is_running = False

        self.label = tk.Label(root, text="ARVUTI KABOOMER")
        self.label.pack(pady=10)

        self.cooldown_label = tk.Label(root, text="Cooldown (seconds):")
        self.cooldown_label.pack()

        self.cooldown_entry = tk.Entry(root)
        self.cooldown_entry.insert(0, "1.0")
        self.cooldown_entry.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_opening)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_opening)
        self.stop_button.pack(pady=10)

        self.counter_label = tk.Label(root, text="Websites opened: 0")
        self.counter_label.pack(pady=10)

        self.root.bind('<Escape>', self.stop_opening)

    def start_opening(self):
        if not self.is_running:
            try:
                self.cooldown = float(self.cooldown_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid cooldown value. Please enter a valid number.")
                return

            self.is_running = True
            self.open_website()

    def open_website(self):
        self.root.attributes("-topmost", 1)  # Set topmost attribute
        webbrowser.open(self.url)
        self.opened_count += 1
        self.counter_label.config(text=f"Websites opened: {self.opened_count}")

        if self.is_running:  # Check if still running
            self.root.after(int(self.cooldown * 1000), self.open_website)

    def stop_opening(self, event=None):
        self.is_running = False
        self.root.attributes("-topmost", 0)  # Clear topmost attribute

if __name__ == "__main__":
    root = tk.Tk()
    gui = WebsiteOpenerGUI(root)
    root.mainloop()
