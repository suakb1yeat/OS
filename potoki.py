import threading
import time
import random
import tkinter as tk

class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Two Threaded App")
        self.geometry("300x200")

        self.label_time = tk.Label(self, font=("Helvetica", 24))
        self.label_time.pack(pady=20)

        # Запуск второго потока
        background_thread = threading.Thread(target=self.change_background_color, daemon=True)
        background_thread.start()

        # Запуск первого потока
        time_thread = threading.Thread(target=self.display_current_time, daemon=True)
        time_thread.start()

    def display_current_time(self):
        try:
            while True:
                current_time = time.strftime("%H:%M:%S")
                self.update_time(current_time)
                time.sleep(1)  # Пауза 1 секунда
        except Exception as e:
            print(f"Error in display_current_time: {e}")

    def change_background_color(self):
        try:
            while True:
                random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                self.update_background_color(random_color)
                time.sleep(2)  # Пауза 2 секунды
        except Exception as e:
            print(f"Error in change_background_color: {e}")

    def update_time(self, current_time):
        self.label_time.after(0, lambda: self.label_time.config(text=current_time))

    def update_background_color(self, color):
        self.after(0, lambda: self.configure(bg=color))

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
