🖱️ CPS Test App (CustomTkinter)

A simple Clicks Per Second (CPS) test built with CustomTkinter
 — a modern UI library for Python.
Click as fast as you can in 5 seconds, and the app will calculate your average CPS score!

🚀 Features

🧮 Tracks number of clicks during a 5-second test

⏱️ Automatically stops after time runs out

🌗 Uses CustomTkinter for a clean dark/light theme

🎨 Simple, customizable UI

🧰 Requirements

Python 3.8+

CustomTkinter (install via pip)
``` bash
pip install customtkinter
```
💻 How to Run

Save the code as cps_test.py.

Open a terminal in the same directory.

Run:
```
python cps_test.py
```

Click the main button as fast as you can!

🧠 How It Works

When you press button, a timer starts for 5 seconds.

Each button click increases your count.

After 5 seconds, the app automatically calculates:

CPS = total_clicks / 5


The result displays on screen instantly.

🛠️ Code Overview
app.after(5000, stop_test)


This line is key — it schedules the stop_test() function to run 5 seconds later without freezing the GUI.

✨ Future Ideas

Add a visible countdown (“Time Left: 4…3…2…”)

Record high scores

feel free to add anything to the code

Let users choose test length (e.g., 5s, 10s)

Add sound or color effects on clicks
