import tkinter as tk
from tkinter import ttk, messagebox

class PomodoroLogic:
    def __init__(self, master, update_callback, confirmation_callback):
        self.master = master
        self.timer_running = False
        self.time_left = 0
        self.work_time = 0
        self.break_time = 0
        self.update_callback = update_callback
        self.confirmation_callback = confirmation_callback
        self.repetitions = 0

    def start_timer(self, work_time, break_time):
        if not self.timer_running:
            try:
                self.work_time = int(work_time)
                self.break_time = int(break_time)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
                return

            self.timer_running = True
            self.time_left = self.work_time * 60  # Inicializar com o tempo de trabalho
            self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.time_left = 0
        self.update_callback("")

    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            self.update_callback(timeformat)
            self.time_left -= 1
            self.after_id = self.master.after(1000, self.update_timer)
        elif self.timer_running and self.time_left == 0:
            self.confirmation_callback("Trocar para descanso!")
            self.after_id = self.master.after(1000, self.start_break_timer)
        else:
            self.confirmation_callback("Timer parado.")

    def start_break_timer(self):
        self.time_left = self.break_time * 60
        self.update_timer()

    def update_repetitions(self):
        self.repetitions += 1


class PomodoroGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")

        self.setup_styles()

        self.logic = PomodoroLogic(master, self.update_timer_label, self.show_confirmation)

        self.work_label = tk.Label(master, text="Tempo de trabalho (minutos):", style="Label.TLabel")
        self.work_entry = tk.Entry(master, style="Entry.TEntry")
        self.work_entry.insert(0, "25")  # Configuração padrão para 25 minutos
        self.break_label = tk.Label(master, text="Tempo de descanso (minutos):", style="Label.TLabel")
        self.break_entry = tk.Entry(master, style="Entry.TEntry")
        self.break_
