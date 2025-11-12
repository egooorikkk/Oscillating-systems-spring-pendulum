import tkinter as tk  # Импорт библиотеки для создания GUI.
from PIL import Image, ImageTk  # Модули для работы с изображениями.
from tkinter import ttk  # Расширенные виджеты для Tkinter.
from Main_window import MainWindow

class MainApp:
    def __init__(self, root):
        # Инициализация главного окна приложения.
        self.root = root
        self.root.title("Стартовое окно")  # Заголовок окна.
        self.root.geometry("700x550")  # Установка размеров окна.
        self.root.configure(bg="#f7f7f7")  # Установка фона.

        # Фрейм для центра окна.
        self.center_frame = tk.Frame(self.root, bg="#f7f7f7")
        self.center_frame.pack(expand=True, fill="both", padx=20, pady=20)

        self.create_start_window()
        self.current_fig = None 

    def create_start_window(self):
        # Создание и размещение заголовков и текста.
        title_label = tk.Label(self.center_frame, text="Белорусский национальный технический университет", font=("Arial", 12, "bold"), bg="#f7f7f7", justify="center")
        title_label.pack(pady=5)

        faculty_label = tk.Label(self.center_frame, text="Факультет информационных технологий и робототехники", font=("Arial", 11, "bold"), bg="#f7f7f7", justify="center")
        faculty_label.pack(pady=5)

        department_label = tk.Label(self.center_frame, text="Кафедра программного обеспечения информационных систем и технологий", font=("Arial", 11, "bold"), bg="#f7f7f7", justify="center")
        department_label.pack(pady=5)

        course_label = tk.Label(self.center_frame, text="Курсовая работа", font=("Arial", 16, "bold"), bg="#f7f7f7", justify="center")
        course_label.pack(pady=5)

        discipline_label = tk.Label(self.center_frame, text="Колебательные системы: пружинный маятник", font=("Arial", 15, "bold"), bg="#f7f7f7", justify="center")
        discipline_label.pack(pady=5)

        # Фрейм для изображения и информации.
        info_frame = tk.Frame(self.center_frame, bg="#f7f7f7")
        info_frame.pack(pady=10)

        # Загрузка и отображение изображения.
        img_path = r"E:\Программирование\new\pictures\images.jfif"  # Путь к изображению.
        img = Image.open(img_path)  # Открытие изображения.
        img = img.resize((150, 150))  # Изменение размера изображения.
        img_photo = ImageTk.PhotoImage(img)  # Преобразование в формат Tkinter.

        img_label = tk.Label(info_frame, image=img_photo, bg="#f7f7f7")
        img_label.image = img_photo  # Привязка изображения для предотвращения удаления.
        img_label.pack(side="left", padx=(0, 20))

        # Информация о студенте и преподавателе.
        info_label = tk.Label(info_frame,
                              text="Выполнил: студент группы 10701323\n"
                                               "Кардович Егор Андреевич\n\n"
                                               "Преподаватель: к.ф.-м.н., доц.\n"
                                               "Сидорик Валерий Владимирович",
                              font=("Arial", 11, "bold"),
                              bg="#f7f7f7",
                              justify="left")

        info_label.pack(side="left", padx=(10, 0))

        # Фрейм для текста "Минск, 2024".
        footer_frame = tk.Frame(self.center_frame, bg="#f7f7f7")
        footer_frame.pack(pady=(20, 10))  # Отступ сверху и снизу.

        footer_label = tk.Label(footer_frame, text="Минск, 2024", font=("Arial", 12, "bold"), bg="#f7f7f7")
        footer_label.pack(pady=(10, 0))  # Отступ под текстом.

        # Фрейм для кнопок.
        button_frame = tk.Frame(self.center_frame, bg="#f7f7f7")
        button_frame.pack(side="bottom", pady=(10, 20))  # Отступ снизу кнопок.

        style = ttk.Style()  # Создание стиля для кнопок.
        style.configure("TButton", font=("Arial", 14), padding=15)

        # Кнопка "Далее".
        next_button = ttk.Button(button_frame, text="Далее", command=self.open_main_window, width=20, style="TButton")
        next_button.pack(side="left", padx=(0, 10))

        style.configure("Red.TButton", foreground="red", font=("Arial", 14), padding=15)

        # Кнопка "Выход".
        exit_button = ttk.Button(button_frame, text="Выход", command=self.root.quit, width=20, style="Red.TButton")
        exit_button.pack(side="right", padx=(10, 0))

    def open_main_window(self):
        # Переход к главному окну приложения.
        self.root.withdraw()  # Скрытие стартового окна.
        self.main_window = MainWindow(self.root)  # Открытие главного окна.

if __name__ == "__main__":
    root = tk.Tk()  # Создание главного окна.
    app = MainApp(root)  # Инициализация приложения.
    root.mainloop()  # Запуск главного цикла событий.
