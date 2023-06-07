import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Configuração da janela
window = tk.Tk()
window.title("Relógio Digital")

# Rótulo para exibir o relógio
clock_label = tk.Label(window, font=("Arial", 48), bg="white")
clock_label.pack(padx=50, pady=50)

# Atualizar o relógio inicialmente
update_clock()

# Executar a janela
window.mainloop()
