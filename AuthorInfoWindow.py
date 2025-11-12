import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Не забудьте импортировать эти модули

class AuthorInfoWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.author_window = tk.Toplevel()
        self.author_window.grab_set()
        self.author_window.title("Об авторе")
        self.author_window.geometry("400x650")
        self.author_window.configure(bg="#f7f7f7")

        # Загружаем изображение автора
        img_path = r"E:\программирование\new\pictures\author.jpg" 
        img = Image.open(img_path)
        img = img.resize((300, 400), Image.LANCZOS) 
        img_photo = ImageTk.PhotoImage(img)

        # Отображение изображения
        img_label = tk.Label(self.author_window, image=img_photo, bg="#f7f7f7")
        img_label.image = img_photo  # Сохраняем ссылку на изображение
        img_label.pack(pady=10)

        author_text = """Автор
        студент группы 10701323
        Кардович Егор Андреевич
        egrosius0601@gmail.com
        """
        info_label = tk.Label(self.author_window, text=author_text, font=("Arial", 12, "bold"), bg="#f7f7f7", justify="center")
        info_label.pack(pady=5)

        # Кнопка "Назад"
        back_button = ttk.Button(self.author_window, text="Назад", command=self.author_window.destroy)
        back_button.pack(pady=10)