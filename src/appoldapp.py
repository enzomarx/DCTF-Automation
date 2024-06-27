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
        thread = Thread(target=run_automation, args=(df, sleep_multiplier))
        thread.start()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o arquivo CSV: {e}")

def run_automation(df, multiplier):
    start_time = time.time()
    total_tasks = len(df)
    completed_tasks = 0

    for index, row in df.iterrows():
        status_label.config(text=f"Processando linha {index+1} de {total_tasks}")
        progress['value'] = (completed_tasks / total_tasks) * 100
        app.update_idletasks()
        
        # Login Dominio Web
#pyautogui.press('win')
#time.sleep(0.5)
#pyautogui.write('edge', interval=0.25)
#pyautogui.press('enter')
#time.sleep(2 * multiplier)

#pyautogui.write('https://www.dominioweb.com.br/', interval=0.25)
#pyautogui.press('enter')
#time.sleep(5 * multiplier)

#pyautogui.click(x=914, y=451)
#pyautogui.write('joas@controllersbr.com', interval=0.1 * multiplier) # seu usuario
#pyautogui.press('tab')
#pyautogui.write('005570@Senha', interval=0.1 * multiplier) # sua senha
#pyautogui.press('enter')
#time.sleep(30 * multiplier)

#pyautogui.doubleClick(x=686, y=307)
#time.sleep(7.5 * multiplier)
#pyautogui.write('enzo') # Seu usuario
#pyautogui.press('tab')
#pyautogui.write('senha@123') # Sua senha
#pyautogui.press('tab')
#pyautogui.press('tab')
#pyautogui.press('enter')
#time.sleep(35 * multiplier)


        # Dominio Web Automação
        pyautogui.doubleClick(162, 113)
        time.sleep(5 * multiplier)
        pyautogui.write(str(row['codigo']), interval=0.1 * multiplier)
        pyautogui.press('enter')
        time.sleep(3 * multiplier)
        pyautogui.doubleClick(510, 62)
        time.sleep(1.5 * multiplier)
        pyautogui.doubleClick(510, 62) #2
        time.sleep(1.5 * multiplier)
        pyautogui.doubleClick(588, 133)
        time.sleep(1.5 * multiplier)
        pyautogui.doubleClick(789, 128)
        time.sleep(1.5 * multiplier)
        pyautogui.doubleClick(x=1019, y=267)
        time.sleep(1.5 * multiplier)
        pyautogui.doubleClick(x=1306, y=271)
        time.sleep(1.5 * multiplier)
        pyautogui.write(str(row['data']), interval=0.1 * multiplier)
        pyautogui.press('enter')
        time.sleep(0.25 * multiplier)
        pyautogui.click(1087, 736)
        pyautogui.click(1222, 390)
        pyautogui.click(1181, 425)
        pyautogui.click(x=757, y=468)
        pyautogui.click(x=1104, y=678)
        pyautogui.click(855, 742)
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.write(str(row['codigo']), interval=0.1 * multiplier)
        time.sleep(0.2 * multiplier)
        pyautogui.click(1234, 397)
        time.sleep(7 * multiplier)
        pyautogui.click(1026, 605)
        pyautogui.click(1324, 343)
        time.sleep(1 * multiplier)
        
        completed_tasks += 1

    pyautogui.hotkey('alt', 'f4')

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos")
    status_label.config(text="Processo concluído")
    progress['value'] = 100
    app.update_idletasks()

def estimate_time(df):
    num_entries = len(df)
    sleep_multiplier = float(sleep_multiplier_entry.get())
    estimated_time = num_entries * 10 * sleep_multiplier  # Estimativa ajustada pelo multiplicador
    estimated_time_label.config(text=f"Estimativa de tempo de execução: {estimated_time:.2f} segundos")

def show_help():
    help_text = ("Passos para automação:\n"
                 "1. Faça upload de um arquivo CSV contendo quaisquer colunas.\n"
                 "2. Ajuste o multiplicador de tempo de espera conforme necessário.\n"
                 "3. Clique em 'Iniciar' para começar a automação.")
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
#app.attributes('-fullscreen', True)
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

project_selector_label = tk.Label(frame, text="Seletor de Projeto:                    ", bg='#FFECA1', font=font_style_label)
project_selector_entry = tk.Entry(frame, width=20)
project_selector_entry.grid(row=2, column=1, pady=20, padx=0, sticky='e')
project_selector_entry.insert
project_selector_label.grid(row=2, column=0, columnspan=2, pady=10, padx=50, sticky= 'e')

estimated_time_label = tk.Label(frame, text="Estimativa de tempo de execução: N/A", bg='#FFECA1', font=font_style_label)
estimated_time_label.grid(row=4, column=0, columnspan=2, pady=20, padx=20)

status_label = tk.Label(frame, text="Status: Aguardando ação", bg='#FFECA1', font=font_style_label)
status_label.grid(row=5, column=0, columnspan=2, pady=10, padx=20)

progress = ttk.Progressbar(frame, orient='horizontal', length=400, mode='determinate')
progress.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(app, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

pulse_text()

app.mainloop()
