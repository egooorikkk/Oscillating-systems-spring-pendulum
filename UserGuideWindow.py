import tkinter as tk
from tkinter import ttk

class UserGuideWindow:
    def __init__(self, parent):
        # Создаем новое окно с руководством пользователя
        self.window = tk.Toplevel(parent)
        self.window.title("Руководство пользователя")
        self.window.geometry("800x600")  # Увеличиваем размер окна
        self.create_widgets()

    def create_widgets(self):
        # Создаем фрейм для текста и кнопки
        frame = tk.Frame(self.window)
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Создаем текст с руководством пользователя
        user_guide_text = """
        Руководство пользователя

        1. Ввод данных:
        Введите массу груза (кг) и жесткость пружины (Н/м) в соответствующие поля.
        После ввода данных нажмите кнопку "Запустить расчеты", чтобы рассчитать период колебаний.

        2. Расчеты:
        Программа рассчитывает период колебаний по формуле T = 2π * sqrt(m / k), где m — масса груза, k — жесткость пружины.
        Результат отображается в виде текста и графика колебаний (смещение, скорость, ускорение).

        3. Графики:
        После расчета программы будет отображен график для смещения, скорости и ускорения.
        Вы можете сохранить график, нажав кнопку "Сохранить график".

        4. Экспорт данных:
        Для сохранения расчетов в Excel, нажмите кнопку "Экспорт данных". Все данные, включая массу, жесткость и результаты расчетов, будут сохранены в Excel.

        5. Дополнительные функции:
        - "Мультипликация движения": Запустите анимацию для просмотра движения в реальном времени.
        - "О программе": Информация о программе.
        - "Об авторе": Подробнее о разработчике программы.

        6. Ошибки:
        Если введены некорректные значения (например, отрицательные значения массы или жесткости), программа покажет сообщение об ошибке.
        """

        # Используем Text widget для длинного текста с возможностью прокрутки
        text_widget = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12), padx=10, pady=10, bg="#f7f7f7", height=20)
        text_widget.insert(tk.END, user_guide_text)
        text_widget.config(state=tk.DISABLED)  # Чтобы текст не был редактируемым

        # Добавляем Scrollbar для прокрутки
        scrollbar = tk.Scrollbar(self.window, command=text_widget.yview)
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.pack(expand=True, fill=tk.BOTH)

        # Добавляем кнопку "Назад"
        back_button = ttk.Button(self.window, text="Назад", command=self.close_window)
        back_button.pack(pady=10)

    def close_window(self):
        # Закрытие окна руководства
        self.window.destroy()