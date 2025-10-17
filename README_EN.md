<p align="center">
  <b>🌐 Choose Language / Выберите язык</b><br><br>
  <a href="README_RU.md"><img src="https://flagcdn.com/w40/ru.png" alt="Русский" /></a> |
  <a href="README_EN.md"><img src="https://flagcdn.com/w40/us.png" alt="English" /></a>
</p>

🌐 Language / Язык
![English version](https://flagcdn.com/w20/us.png)
---


# 🔢 Decimal Base Converter

A simple and stylish **Python (Tkinter + CustomTkinter)** application that allows you to convert numbers from the **decimal system** to any other base — from **2 to 16**.  
The interface is designed in a modern dark theme with smooth elements and custom icons.

---

## 🖥️ Features

✅ Convert numbers from **decimal** to any base between **2 and 16**  
✅ Sleek graphical interface built with **CustomTkinter**  
✅ Input validation and error handling  
✅ Pop-up error messages  
✅ Control buttons:
- 🔁 **Convert**
- 🗑 **Clear**
- ℹ **About the app**

---

## 📸 Interface Screenshot

![Program Interface](resource/screenshot.png)

---

## ⚙️ Installation & Launch

### 1️⃣ Install dependencies

Make sure you have **Python 3.10+** installed, then run:

```bash
pip install customtkinter pillow
````

### 2️⃣ Clone the repository

```bash
git clone https://github.com/michytka22/Decimal-Base-Converter.git
cd calculator-base-converter
```

### 3️⃣ Run the program

```bash
python calculator.py
```

---

## 📁 Project Structure

```
calculator-base-converter/
│
├── calculator.py             # Main application file
├── resource/                 # Icons folder
│   ├── calculator.png
│   ├── rotate.png
│   ├── trash.png
│   └── info.png
└── README.md
```

---

## 💡 How It Works

1. The user enters a **decimal number**.
2. Selects the desired **base (2–16)**.
3. Clicks the **“Convert”** button.
4. The result is displayed at the bottom of the window.

The function `decimal_to_selected()` performs the conversion to the selected numeral system and supports negative numbers.

---

## 🧩 Technologies Used

* 🐍 **Python 3**
* 🪟 **Tkinter / CustomTkinter**
* 🖼 **Pillow (PIL)** — for image loading
* 💬 **tkinter.messagebox / ttk** — for message dialogs

---

## 👨‍💻 Author

* 👤 **michytka22**
* 🌐 GitHub: [github.com/michytka22](https://github.com/michytka22)
