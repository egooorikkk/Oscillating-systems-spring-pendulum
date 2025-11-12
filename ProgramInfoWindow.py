import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 

class ProgramInfoWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.program_window = tk.Toplevel()
        self.program_window.grab_set()
        self.program_window.title("Об программе")
        self.program_window.geometry("1150x450") 
        self.program_window.configure(bg="#f7f7f7")

        # Заголовок
        title_label = tk.Label(self.program_window, text="Колебательные системы:\nпружинный маятник", font=("Arial", 16, "bold"), bg="#f7f7f7")
        title_label.pack(pady=10)

        # Фрейм для изображения и текста
        info_frame = tk.Frame(self.program_window, bg="#f7f7f7")
        info_frame.pack(pady=10)

        # Фрейм для изображения и версии
        img_and_version_frame = tk.Frame(info_frame, bg="#f7f7f7")
        img_and_version_frame.pack(side="left", padx=10)

        # Загрузка изображения
        img_path = r"E:\программирование\new\pictures\prug.bmp"  
        img = Image.open(img_path)
        img = img.resize((200, 200), Image.LANCZOS)  
        img_photo = ImageTk.PhotoImage(img)

        # Отображение изображения
        img_label = tk.Label(img_and_version_frame, image=img_photo, bg="#f7f7f7")
        img_label.image = img_photo  
        img_label.pack()

        # Метка версии под фото
        version_label = tk.Label(img_and_version_frame, text="Версия: ver 1.0.0.2024", font=("Arial", 12, "bold"), bg="#f7f7f7", fg="#333")
        version_label.pack(pady=5)

        # Текст о программе
        program_text = """
            Программа предназначена для исследования колебательных систем, а именно пружинного маятника. 
            Основные функциональные возможности включают:

            - Ввод параметров системы, таких как масса груза и жесткость пружины;
            - Расчет характеристик колебаний: период, частота, амплитуда, максимальное ускорение и механическая энергия;
            - Построение графиков зависимости смещения, скорости и ускорения от времени;
            - Сохранение графиков и экспорт расчетных данных в формате Excel;
            - Визуализация движения маятника с помощью анимации.

            Программа позволяет наглядно изучить влияние параметров системы на характер ее колебаний 
            и служит полезным инструментом для анализа динамических процессов в механике.
        """

        info_label = tk.Label(info_frame, text=program_text, font=("Arial", 12), bg="#f7f7f7", justify="left")
        info_label.pack(side="right", padx=5) 

        # Кнопка "Назад"
        back_button = ttk.Button(self.program_window, text="Назад", command=self.program_window.destroy)
        back_button.pack(pady=10)
