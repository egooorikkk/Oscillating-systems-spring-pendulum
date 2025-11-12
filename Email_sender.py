import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from tkinter import messagebox

class EmailSender:
    def __init__(self):
        self.from_email = "kursovaya2006@mail.ru" 
        self.password = "eCYd0BffBGiVNwfzaH5S"

    def send_email(self, file_path, to_email, subject, body):
        # Создание MIME-объекта для письма
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Добавление текста письма
        msg.attach(MIMEText(body, 'plain'))  # Текст письма
        
        # Добавление файла (графика) в письмо
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={file_path.split('/')[-1]}")
            msg.attach(part)
        
        try:
            # Подключение к серверу mail.ru и отправка письма
            server = smtplib.SMTP('smtp.mail.ru', 587)  # Адрес и порт для mail.ru
            server.starttls()  # Начинаем защищённое соединение
            server.login(self.from_email, self.password)  # Логинимся с использованием пароля
            server.sendmail(self.from_email, to_email, msg.as_string())  # Отправка письма
            server.quit()  # Закрытие соединения
            messagebox.showinfo("Успешно!", "Письмо успешно отправлено!")
        except Exception as e:
            messagebox.showinfo(f"Произошла ошибка: {e}")