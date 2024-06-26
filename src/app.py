import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from threading import Thread
import pandas as pd
import pyautogui
import time
from PIL import ImageTk, Image

pyautogui.PAUSE = 0.5

def upload_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            cnpj_entry.delete(0, tk.END)
            cnpj_entry.insert(0, file_path)
            estimate_time(df)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo CSV: {e}")

def start_automation():
    file_path = cnpj_entry.get()
    if not file_path:
        messagebox.showwarning("Entrada Inválida", "Por favor, faça upload de um arquivo CSV.")
        return

    try:
        df = pd.read_csv(file_path)
        sleep_multiplier = float(sleep_multiplier_entry.get())
        if selected_task.get() == "EFD Contribuições":
            thread = Thread(target=run_automation_efd, args=(df, sleep_multiplier))
        elif selected_task.get() == "Cadastro SCP":
            thread = Thread(target=run_automation_scp, args=(df, sleep_multiplier))
        elif selected_task.get() == "DCTF":
            thread = Thread(target=run_automation_dctf, args=(df, sleep_multiplier))
        else:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um projeto válido.")
            return
        thread.start()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o arquivo CSV: {e}")

def run_automation_dctf(df, multiplier):
    # Código de automação para DCTF aqui
    pass

def run_automation_efd(df, multiplier):
    # Código de automação para EFD Contribuições aqui
    pass

def run_automation_scp(df, multiplier):
    # Código de automação para Cadastro SCP aqui
    time.sleep(3)
    pyautogui.press('win')
    pyautogui.write('ola, estou aqui')
    pass

def estimate_time(df):
    num_entries = len(df)
    sleep_multiplier = float(sleep_multiplier_entry.get())
    estimated_time = num_entries * 10 * sleep_multiplier  # Estimativa ajustada pelo multiplicador
    estimated_time_label.config(text=f"Estimativa de tempo de execução: {estimated_time:.2f} segundos")

def show_help():
    help_text = ("Passos para automação:\n"
                 "1. Faça upload de um arquivo CSV contendo quaisquer colunas.\n"
                 "2. Ajuste o multiplicador de tempo de espera conforme necessário.\n"
                 "3. Selecione o projeto desejado.\n"
                 "4. Clique em 'Iniciar' para começar a automação.")
    messagebox.showinfo("Ajuda", help_text)

def pulse_text():
    current_color = status_label.cget("foreground")
    next_color = "red" if current_color == "blue" else "blue"
    status_label.config(foreground=next_color)
    app.after(500, pulse_text)

path = r"C:\Users\PC\Downloads\DECS-removebg-preview.png"

app = tk.Tk()
app.title("Automação DCTF")
app.geometry('800x800')
# app.attributes('-fullscreen', True)
app.configure(bg='#FFECA1')

font_style_title = ('Helvetica', 16, 'bold')
font_style_label = ('Helvetica', 12)
font_style_button = ('Helvetica', 12, 'bold')

frame = tk.Frame(app, bg='#FFECA1')
frame.pack(expand=True)

tk.Label(frame, text="Arquivo CSV:", bg='#FFECA1', font=font_style_label).grid(row=0, column=0, pady=20, padx=20, sticky='e')
cnpj_entry = tk.Entry(frame, width=60)
cnpj_entry.grid(row=0, column=1, pady=20, padx=10, sticky='w')

upload_button = tk.Button(frame, text="Upload CSV", command=upload_csv, bg='#4169e1', fg='white', font=font_style_button, relief='raised')
upload_button.grid(row=1, column=0, pady=10, padx=20)

tk.Label(frame, text="Multiplicador de Tempo:", bg='#FFECA1', font=font_style_label).grid(row=2, column=0, pady=20, padx=20, sticky='e')
sleep_multiplier_entry = tk.Entry(frame, width=10)
sleep_multiplier_entry.grid(row=2, column=1, pady=20, padx=10, sticky='w')
sleep_multiplier_entry.insert(0, "1.0")  # Valor padrão

start_button = tk.Button(frame, text="Iniciar", command=start_automation, bg='#228b22', fg='white', font=font_style_button, relief='raised')
start_button.grid(row=3, column=1, pady=10, padx=10, sticky='w')

help_button = tk.Button(frame, text="Ajuda", command=show_help, bg='#FFA500', fg='white', font=font_style_button, relief='raised')
help_button.grid(row=3, column=0, pady=10, padx=10, sticky='e')

project_selector_label = tk.Label(frame, text="Seletor de Projeto:                           ", bg='#FFECA1', font=font_style_label)
project_selector_label.grid(row=2, column=0, columnspan=2, pady=10, padx=50, sticky= 'e')

# Menubutton variable
selected_task = tk.StringVar()
selected_task.set("Selecionar")  # Valor padrão

# create the Menubutton
menu_button = ttk.Menubutton(frame, textvariable=selected_task, width=20)

# create a new menu instance
menu = tk.Menu(menu_button, tearoff=0)

for task in ["EFD Contribuições", "Cadastro SCP", "DCTF"]:
    menu.add_radiobutton(label=task, value=task, variable=selected_task)

# associate menu with the Menubutton
menu_button["menu"] = menu
menu_button.grid(row=2, column=1, pady=20, padx=0, sticky='e')

estimated_time_label = tk.Label(frame, text="Estimativa de tempo de execução: N/A", bg='#FFECA1', font=font_style_label)
estimated_time_label.grid(row=5, column=0, columnspan=2, pady=20, padx=20)

status_label = tk.Label(frame, text="Status: Aguardando ação", bg='#FFECA1', font=font_style_label)
status_label.grid(row=6, column=0, columnspan=2, pady=10, padx=20)

progress = ttk.Progressbar(frame, orient='horizontal', length=400, mode='determinate')
progress.grid(row=7, column=0, columnspan=2, pady=20, padx=20)

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(app, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

pulse_text()

app.mainloop()
