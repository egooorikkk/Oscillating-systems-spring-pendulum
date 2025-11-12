import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from UserGuideAnimation import UserGuideAnimation

class Animation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Параметры пружинного маятника")
        self.root.geometry("400x380")
        self.root.resizable(False, False)
        self.setup_main_window()

    def setup_main_window(self):
        # Настройка стиля для элементов интерфейса
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12), padding=5)
        style.configure("TEntry", font=("Arial", 12))

        # Заголовок окна
        ttk.Label(self.root, text="Параметры пружинного маятника", font=("Arial", 14, "bold")).pack(pady=10)

        # Поле для ввода жёсткости пружины
        ttk.Label(self.root, text="Жёсткость пружины (Н/м):").pack(pady=5)
        self.entry_k = ttk.Entry(self.root, justify="center")
        self.entry_k.pack(pady=5)

        # Создание меню с пунктом "Справка"
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="Руководство пользователя", command=self.show_guide_animation)

        # Поле для ввода массы груза
        ttk.Label(self.root, text="Масса груза (кг):").pack(pady=5)
        self.entry_m = ttk.Entry(self.root, justify="center")
        self.entry_m.pack(pady=5)

        # Кнопка для запуска анимации
        start_button = ttk.Button(self.root, text="Запуск анимации", command=self.start_animation)
        start_button.pack(pady=20)

        # Инструкция по вводу данных
        ttk.Label(self.root, text="Введите параметры и нажмите 'Запуск анимации'.", font=("Arial", 10, "italic")).pack(pady=10)

        # Кнопка для выхода
        back_button = ttk.Button(self.root, text="Назад", command=self.root.destroy)    
        back_button.pack(pady=20)

    def show_guide_animation(self):
        # Показывает руководство пользователя
        UserGuideAnimation(self.root)

    def start_animation(self):
        try:
            # Получаем значения для жёсткости и массы
            k = float(self.entry_k.get())
            m = float(self.entry_m.get())
            if k > 0 and m > 0:
                self.root.withdraw()  # Скрываем основное окно
                AnimationWindow(k, m, self).run()  # Запускаем окно анимации
            else:
                messagebox.showerror("Ошибка", "Жёсткость и масса должны быть положительными числами.")
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения.")

    def back(self):
        self.root.quit()  # Закрыть приложение

    def run(self):
        self.root.mainloop()


class AnimationWindow:
    def __init__(self, k, m, main_window):
        self.k = k
        self.m = m
        self.main_window = main_window  # Ссылка на основное окно
        self.t = 0
        self.max_time = 50
        self.amplitude = 100
        self.omega = np.sqrt(self.k / self.m)
        self.dt = 0.05
        self.damping = 0.01
        self.running = True

        # Интерфейс анимации
        self.root = tk.Tk()
        self.root.title("Анимация пружинного маятника")
        self.root.geometry("520x520")
        self.root.resizable(False, False)

        # Настройка области для рисования (канвас)
        self.canvas = tk.Canvas(self.root, width=500, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.origin_x = 250
        self.origin_y = 100
        self.length = 150
        self.mass_radius = 15

        # Рисуем маятник (линия и масса)
        self.line = self.canvas.create_line(
            self.origin_x, self.origin_y, 
            self.origin_x, self.origin_y + self.length, 
            width=2, fill="black"
        )
        self.mass = self.canvas.create_oval(
            self.origin_x - self.mass_radius, self.origin_y + self.length - self.mass_radius,
            self.origin_x + self.mass_radius, self.origin_y + self.length + self.mass_radius,
            fill="blue"
        )

        # Кнопки управления (остановить, продолжить, назад)
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(pady=10)

        stop_button = ttk.Button(controls_frame, text="Остановить", command=self.stop)
        stop_button.grid(row=0, column=0, padx=5)

        resume_button = ttk.Button(controls_frame, text="Продолжить", command=self.resume)
        resume_button.grid(row=0, column=1, padx=5)

        back_button = ttk.Button(controls_frame, text="Назад", command=self.back)
        back_button.grid(row=1, column=0, columnspan=2, pady=10)

    def calculate_position(self):
        # Расчёт вертикального смещения массы
        y_offset = self.amplitude * np.exp(-self.damping * self.t) * np.cos(self.omega * self.t)
        return y_offset

    def animate(self):
        if self.running:
            # Анимация движения маятника
            y_offset = self.calculate_position()
            new_y = self.origin_y + self.length + y_offset

            # Обновляем координаты маятника
            self.canvas.coords(self.line, self.origin_x, self.origin_y, self.origin_x, new_y)
            self.canvas.coords(
                self.mass,
                self.origin_x - self.mass_radius, new_y - self.mass_radius,
                self.origin_x + self.mass_radius, new_y + self.mass_radius
            )

            self.t += self.dt
            # Если амплитуда мала, останавливаем анимацию
            if np.abs(self.amplitude * np.exp(-self.damping * self.t)) < 0.5:
                self.running = False
                messagebox.showinfo("Завершение", "Маятник остановился.")
            else:
                self.root.after(int(self.dt * 1000), self.animate)

    def stop(self):
        # Останавливаем анимацию
        self.running = False

    def resume(self):
        # Продолжаем анимацию
        if not self.running:
            self.running = True
            self.animate()

    def back(self):
        # Закрытие окна анимации и возврат в основное окно
        self.root.destroy()
        if self.main_window.root.winfo_exists():
            self.main_window.root.deiconify()  # Показываем главное окно
        else:
            self.main_window.run()  # Если главное окно закрыто, перезапускаем его

    def run(self):
        # Запуск анимации
        self.animate()
        self.root.mainloop()