import customtkinter as ctk
import time

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

cps = 0
start_time = None

def on_click():
    global cps, start_time
    
    if start_time is None:
        start_time = time.time()
        cps = 0
        result_label.configure(text="Test running...")
        app.after(5000, stop_test)
    
    cps += 1
    cps_label.configure(text=f"CPS: {cps}")


def stop_test():
    duration = 5
    cps_total = cps / duration
    result_label.configure(text=f"Final CPS: {cps_total:.2f}")
    button.configure(state="disabled")  

app = ctk.CTk()
app.geometry("1920x1080")
app.title("CPS test")

label = ctk.CTkLabel(app, text="CPS Test", font=("Arial", 40))
label.pack(pady=10)

button = ctk.CTkButton(app, text="Click me", font=("Arial", 40), command=on_click)
button.pack(pady=10)

cps_label = ctk.CTkLabel(app, text="CPS: 0", font=("Arial", 40))
cps_label.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 40))
result_label.pack(pady=10)

app.mainloop()
