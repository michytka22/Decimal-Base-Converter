import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

#Функция перевода введеных чисел в выбранную систему счисления
def decimal_to_selected(n: int, base: int) -> str:

    if n == 0:
        return "0"

    digits = "0123456789ABCDEF"
    negative = n < 0
    n = abs(n)
    result = ""

    while n > 0:
        result = digits[n % base] + result
        n //= base

    return ("-" if negative else "") + result

#Функция для работы кнопки перевода(convert)
def convert():
    try:
        decimal_str = entry_decimal.get().strip()
        if not decimal_str:
            raise ValueError("Введите число.")
        decimal_num = int(decimal_str)
        base = int(combobox_base.get())
        result = decimal_to_selected(decimal_num, base)
        label_result.config(text=f"Результат: {result}")
    except ValueError as e:
        if "invalid literal" in str(e):
            messagebox.showerror("Ошибка", "Введите корректное целое число.")
        else:
            messagebox.showerror("Ошибка", str(e))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Неизвестная ошибка: {e}")


# Создание главного окна
root = tk.Tk()
# Иконка программы
try:
    icon_image = tk.PhotoImage(file="resource/calculator.png")
    root.iconphoto(True, icon_image)
except Exception as e:
    print(f"Не удалось загрузить иконку: {e}")
# Иконка кнопки перевода
try:
    icon_img = Image.open("resource/rotate.png").resize((18, 18))
    icon_photo = ImageTk.PhotoImage(icon_img)
except Exception as e:
    print(f"Ошибка загрузки иконки: {e}")
    icon_photo = None
# Иконка кнопки очистки
try:
    icon_trash = Image.open("resource/trash.png").resize((18, 18))
    icon_phototrash = ImageTk.PhotoImage(icon_trash)
except Exception as e:
    print(f"Ошибка загрузки иконки: {e}")
    icon_phototrash = None
# Иконка кнопки информации
try:
    icon_info = Image.open("resource/info.png").resize((18, 18))
    icon_photoinfo = ImageTk.PhotoImage(icon_info)
except Exception as e:
    print(f"Ошибка загрузки иконки: {e}")
    icon_photoinfo = None
root.title("Конвертер систем счисления")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#1f1f1f")

# Заголовок
title_label = tk.Label(root, text="Перевод из десятичной СС", font=(
    "Segoe UI", 16, "bold"), bg="#1f1f1f", fg="#fff")
title_label.pack(pady=(20, 10))

# Поле ввода числа
frame_input = ctk.CTkFrame(root, fg_color="transparent")
frame_input.pack(pady=5)
ctk.CTkLabel(frame_input, text="Введите число:", text_color="white",
             font=("Segoe UI", 14)).pack(side="left", padx=(0, 10))
entry_decimal = ctk.CTkEntry(
    frame_input, width=150, font=("Segoe UI", 12), corner_radius=10)
entry_decimal.pack(side="left")
entry_decimal.focus()

# Кнопка очистки
btn_clear = ctk.CTkButton(frame_input, image=icon_phototrash, text=None, command=lambda: entry_decimal.delete(0, tk.END), width=1)
btn_clear.pack(side="right", padx=(10, 0))

# Выбор системы счисления
frame_base = ctk.CTkFrame(root, fg_color="transparent")
frame_base.pack(pady=10)
ctk.CTkLabel(frame_base, text="Основание (2–16):", text_color="white",
             font=("Segoe UI", 14)).pack(side="left", padx=(0, 10))
combobox_base = ctk.CTkComboBox(frame_base, values=[str(i) for i in range(
    2, 17)], state="readonly", width=80, font=("Segoe UI", 12), corner_radius=10)
combobox_base.set("2")
combobox_base.pack(side="left")

# Кнопка перевода
btn_convert = ctk.CTkButton(root, text="Перевести", image=icon_photo, compound="right", command=convert, width=120, font=("Segoe UI", 12))
btn_convert.pack(pady=15)

# Кнопка информации о программе
btn_info = ctk.CTkButton(root, text=None, image=icon_photoinfo, command=lambda: messagebox.showinfo(
    "О программе", "Это приложение позволяет переводить числа из десятичной системы счисления в любую систему счисления от 2 до 16."), width=1)
btn_info.place(relx=1.0, rely=0.0, anchor="ne")

# Метка для результата
label_result = tk.Label(root, text="Результат: —", font=(
    "Segoe UI", 12, "bold"), bg="#1f1f1f", fg="#0078d7")
label_result.pack(pady=10)

# Фокус на поле ввода
entry_decimal.focus()

# Запуск главного цикла
root.mainloop()
