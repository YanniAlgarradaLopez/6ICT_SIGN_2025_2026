import tkinter as tk
from tkinter import simpledialog
import json
import os
from datetime import datetime, timedelta
import threading
from gpiozero import OutputDevice
import time

# ===== INSTELLINGEN =====
MOTOR_PIN = 18
SNOOZE_MINUTES = 5
DATA_FILE = "alarms.json"

motor = OutputDevice(MOTOR_PIN)

# ===== DATA OPSLAG =====
def load_alarms():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_alarms():
    with open(DATA_FILE, "w") as f:
        json.dump(alarms, f)

alarms = load_alarms()

# ===== MOTOR FUNCTIE =====
def vibrate():
    while alarm_active:
        motor.on()
        time.sleep(0.5)
        motor.off()
        time.sleep(0.5)

# ===== ALARM CHECK =====
def check_alarms():
    global alarm_active
    now = datetime.now().strftime("%H:%M")

    for alarm in alarms:
        if alarm["time"] == now and alarm["active"]:
            trigger_alarm()

    root.after(30000, check_alarms)  # elke 30 sec check

def trigger_alarm():
    global alarm_active
    alarm_active = True

    threading.Thread(target=vibrate).start()

    alarm_window = tk.Toplevel(root)
    alarm_window.attributes("-fullscreen", True)
    alarm_window.configure(bg="black")

    tk.Label(alarm_window, text="⏰ WAKKER WORDEN!",
             fg="white", bg="black",
             font=("Helvetica", 40)).pack(pady=100)

    tk.Button(alarm_window, text="STOP",
              font=("Helvetica", 30),
              command=lambda: stop_alarm(alarm_window)).pack(pady=20)

    tk.Button(alarm_window, text="SNOOZE",
              font=("Helvetica", 30),
              command=lambda: snooze_alarm(alarm_window)).pack(pady=20)

def stop_alarm(window):
    global alarm_active
    alarm_active = False
    motor.off()
    window.destroy()

def snooze_alarm(window):
    global alarm_active
    alarm_active = False
    motor.off()

    snooze_time = (datetime.now() + timedelta(minutes=SNOOZE_MINUTES)).strftime("%H:%M")
    alarms.append({"time": snooze_time, "active": True})
    save_alarms()

    window.destroy()
    refresh_alarm_list()

# ===== UI FUNCTIES =====
def add_alarm():
    time_input = simpledialog.askstring("Nieuwe alarm", "Voer tijd in (HH:MM)")
    if time_input:
        alarms.append({"time": time_input, "active": True})
        save_alarms()
        refresh_alarm_list()

def toggle_alarm(index):
    alarms[index]["active"] = not alarms[index]["active"]
    save_alarms()
    refresh_alarm_list()

def delete_alarm(index):
    alarms.pop(index)
    save_alarms()
    refresh_alarm_list()

def refresh_alarm_list():
    for widget in alarm_frame.winfo_children():
        widget.destroy()

    for i, alarm in enumerate(alarms):
        frame = tk.Frame(alarm_frame)
        frame.pack(fill="x", pady=5)

        status = "🟢" if alarm["active"] else "🔴"

        tk.Label(frame, text=f"{alarm['time']} {status}",
                 font=("Helvetica", 25)).pack(side="left", padx=20)

        tk.Button(frame, text="Aan/Uit",
                  command=lambda i=i: toggle_alarm(i)).pack(side="left")

        tk.Button(frame, text="Verwijder",
                  command=lambda i=i: delete_alarm(i)).pack(side="left")

# ===== HOOFDVENSTER =====
root = tk.Tk()
root.title("Digitale Wekker")
root.attributes("-fullscreen", True)

clock_label = tk.Label(root, font=("Helvetica", 50))
clock_label.pack(pady=20)

def update_clock():
    now = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

tk.Button(root, text="+ Nieuwe Alarm",
          font=("Helvetica", 25),
          command=add_alarm).pack(pady=10)

alarm_frame = tk.Frame(root)
alarm_frame.pack(fill="both", expand=True)

alarm_active = False

refresh_alarm_list()
update_clock()
check_alarms()

root.mainloop()