import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Temporizador Pomodoro")
        self.root.geometry("300x200")
        self.root.configure(bg='#3498db')

        self.work_duration = 25 * 60
        self.break_duration = 5 * 60
        self.time_left = self.work_duration

        self.canvas = tk.Canvas(root, width=150, height=150, bg='#3498db', highlightthickness=0)
        self.canvas.pack(pady=10)

        self.ampulheta_image = Image.open("ampulheta.jpg")  # Substitua "ampulheta.png" pelo caminho da sua imagem
        self.ampulheta_image = self.ampulheta_image.resize((150, 150))
        self.ampulheta_photo = ImageTk.PhotoImage(self.ampulheta_image)

        self.ampulheta_item = self.canvas.create_image(75, 75, image=self.ampulheta_photo)

        self.label = tk.Label(root, text=self.format_time(self.time_left), font=("Helvetica", 24), bg='#3498db', fg='#ecf0f1')
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_timer, bg='#2ecc71', fg='#ecf0f1')
        self.start_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reiniciar", command=self.reset_timer, bg='#e74c3c', fg='#ecf0f1')
        self.reset_button.pack(pady=5)

        self.is_running = False
        self.inversions = 0  # Adiciona uma variável para contar inversões

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.label.config(text=self.format_time(self.time_left))
            self.rotate_ampulheta()
            self.root.after(1000, self.update_timer)
            self.calculate_inversions()  # Calcula inversões a cada segundo
        else:
            if self.work_duration == self.time_left:
                messagebox.showinfo("Pomodoro", "Hora de descansar!")
                self.time_left = self.break_duration
            else:
                messagebox.showinfo("Pomodoro", "Hora de trabalhar!")
                self.time_left = self.work_duration

            self.label.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)

    def calculate_inversions(self):
        # Função para calcular inversões
        if self.time_left == self.work_duration // 2:  # Exemplo: Conta uma inversão quando metade do tempo de trabalho é alcançado
            self.inversions += 1
            print(f'Número de inversões: {self.inversions}')

    def reset_timer(self):
        self.is_running = False
        self.time_left = self.work_duration
        self.label.config(text=self.format_time(self.time_left))
        self.canvas.itemconfig(self.ampulheta_item, image=self.ampulheta_image)  # Restaura a imagem da ampulheta

    def rotate_ampulheta(self):
        self.ampulheta_image = self.ampulheta_image.rotate(6)  # Gira 6 graus a cada segundo
        self.ampulheta_photo = ImageTk.PhotoImage(self.ampulheta_image)
        self.canvas.itemconfig(self.ampulheta_item, image=self.ampulheta_photo)

    @staticmethod
    def format_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
