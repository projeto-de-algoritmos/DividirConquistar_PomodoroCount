import tkinter as tk
from tkinter import messagebox
from pomodoro_logic import PomodoroLogic

class PomodoroGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")

        # Configurando o fundo em degradê roxo
        self.master.configure(bg="#6b5b95")

        self.logic = PomodoroLogic(master, self.update_timer_label, self.show_confirmation)

        self.work_label = tk.Label(master, text="Tempo de trabalho (minutos):", bg="#6b5b95", fg="white")
        self.work_entry = tk.Entry(master, bg="#8e44ad", fg="white", insertbackground="white")
        self.work_entry.insert(0, "25")  # Configuração padrão para 25 minutos
        self.break_label = tk.Label(master, text="Tempo de descanso (minutos):", bg="#6b5b95", fg="white")
        self.break_entry = tk.Entry(master, bg="#8e44ad", fg="white", insertbackground="white")
        self.break_entry.insert(0, "5")  # Configuração padrão para 5 minutos

        self.start_button = tk.Button(master, text="Iniciar", command=self.start_button_click, bg="#16a085", fg="white")
        self.stop_button = tk.Button(master, text="Parar", command=self.stop_button_click, bg="#c0392b", fg="white")

        self.timer_label = tk.Label(master, text="", font=("Helvetica", 16), fg="#f39c12", bg="#6b5b95")
        self.repetitions_label = tk.Label(master, text="Repetições: 0", font=("Helvetica", 12), bg="#6b5b95", fg="white")

        # Configurar layout usando grid
        self.work_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.work_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        self.break_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.break_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=20)
        self.stop_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.timer_label.grid(row=4, column=0, columnspan=2)
        self.repetitions_label.grid(row=5, column=0, columnspan=2, pady=10)

    def start_button_click(self):
        response = messagebox.askyesno("Confirmação", "Você deseja iniciar o Pomodoro?")
        if response:
            self.logic.start_timer(self.work_entry.get(), self.break_entry.get())

    def stop_button_click(self):
        response = messagebox.askyesno("Confirmação", "Você deseja parar o Pomodoro?")
        if response:
            self.logic.stop_timer()

    def update_timer_label(self, message):
        self.timer_label.config(text=message)
        self.master.update_idletasks()

    def show_confirmation(self, message):
        response = messagebox.showinfo("Pomodoro Concluído", message)
        if response:
            self.logic.update_repetitions()
            self.repetitions_label.config(text=f"Repetições: {self.logic.repetitions}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroGUI(root)
    # Centralizar a janela na tela
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    root.mainloop()
