# 🎯 Aim TraineR

A simple Python-based aim training game built using Pygame. This tool helps improve mouse accuracy, reaction time, and overall aiming skills through interactive target practice.

---

## 🚀 Motivation
Practicing aim is essential for improving performance in FPS games. This project provides a lightweight and fun way to train your reflexes and precision directly from your computer.

---

## ✨ Features
- Interactive target shooting gameplay  
- Randomized target positions  
- Score tracking system  
- Simple and clean UI  
- Real-time feedback on performance  

---

## 📁 Project Structure
```
aim-traineR/
├── window.py # main game loop and window handling
├── targetClass.py # target behavior and logic
├── requirements.txt # project dependencies
├── .gitignore # ignored files (venv, cache, etc.)
└── README.md # project documentation
```

---

## ▶️ How to Run
```bash
git clone https://github.com/laypatel13/aim-traineR.git
cd aim-traineR

python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
python3 window.py