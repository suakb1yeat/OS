import tkinter as tk
import keyboard
import mouse

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("lab7")
        self.geometry("550x150")
        self.resizable(False, False)

        self.label = tk.Label(self, text="Отслеживание событий клавиатуры и мыши", font=("Arial", 14))
        self.label.pack(pady=20)

        self.tracking = False

        self.start_stop_button = tk.Button(self, text="Начать отслеживание", command=self.toggle_tracking)
        self.start_stop_button.pack(pady=10)

    def toggle_tracking(self):
        if not self.tracking:
            self.tracking = True
            self.start_stop_button.config(text="Остановить отслеживание")
            keyboard.on_press(self.key_pressed)
            mouse.hook(self.mouse_button_pressed)
            self.label.config(text="Отслеживание начато")
        else:
            self.tracking = False
            self.start_stop_button.config(text="Начать отслеживание")
            keyboard.unhook_all()
            mouse.unhook_all()
            self.label.config(text="Отслеживание остановлено")

    def key_pressed(self, event):
        key = event.name
        self.label.config(text=f"Клавиша '{key}' нажата")

    def mouse_button_pressed(self, event):
        button = event.button
        self.label.config(text=f"Кнопка мыши '{button}' нажата")

if __name__ == "__main__":
    app = Application()
    app.mainloop()