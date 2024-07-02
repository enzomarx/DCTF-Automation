import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from threading import Thread
import pandas as pd
import pyautogui
import time
from PIL import ImageTk, Image
import os
import shutil

pyautogui.PAUSE = 0.5

source_folder = r'C:\Brother'
destination_folder = r'C:\DCTF'

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
        pyautogui.press('win')
        time.sleep(0.5)
        pyautogui.write('edge', interval=0.25)
        pyautogui.press('enter')
        time.sleep(2 * multiplier)
        pyautogui.rightClick(1694,316)
        pyautogui.click(1641,438)

        pyautogui.write('https://www.dominioweb.com.br/', interval=0.25)
        pyautogui.press('enter')
        time.sleep(5 * multiplier)

        pyautogui.click(x=914, y=451)
        pyautogui.write('x', interval=0.1 * multiplier) # Seu usuario
        pyautogui.press('tab')
        pyautogui.write('y', interval=0.1 * multiplier) # Sua senha
        pyautogui.press('enter')
        time.sleep(30 * multiplier)

        pyautogui.doubleClick(x=686, y=307)
        time.sleep(7.5 * multiplier)
        pyautogui.write('enzo') # Seu usuario
        pyautogui.press('tab')
        pyautogui.write('senha@123') # Sua senha
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(35 * multiplier)


        # Dominio Web Automação
        pyautogui.doubleClick(162, 113)
        time.sleep(5 * multiplier)
        pyautogui.click(x=778, y=250)
        time.sleep(1.5 * multiplier)
        pyautogui.write(str(row['codigo']), interval=0.3 * multiplier)
        pyautogui.press('enter')
        time.sleep(3 * multiplier)
        pyautogui.doubleClick(510, 62)
        time.sleep(1.5 * multiplier)
        pyautogui.click(510, 62) #2
        time.sleep(1.5 * multiplier)
        pyautogui.click(x=559, y=127)
        time.sleep(1.5 * multiplier)
        pyautogui.click(x=780, y=125)
        time.sleep(1.5 * multiplier)
        pyautogui.click(x=1029, y=237)
        time.sleep(1.5 * multiplier)
        pyautogui.click(x=1320, y=244)
        time.sleep(1.5 * multiplier)
        pyautogui.write(str(row['data']), interval=0.3 * multiplier)
        pyautogui.press('enter')
        time.sleep(1.5 * multiplier)
        pyautogui.click(1087, 736)
        time.sleep(1.5 * multiplier)
        pyautogui.click(1222, 390)
        time.sleep(1.5 * multiplier)
        pyautogui.click(1181, 425)
        time.sleep(1.5 * multiplier)
        pyautogui.click(x=757, y=468)
        time.sleep(1.5 * multiplier)
        pyautogui.click(x=1104, y=678)
        time.sleep(1.5 * multiplier)
        pyautogui.click(855, 742)
        time.sleep(1.5 * multiplier)
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.write(str(row['codigo']), interval=0.3 * multiplier)
        time.sleep(1.5 * multiplier)
        pyautogui.click(1234, 397)
        time.sleep(7 * multiplier)
        pyautogui.click(1026, 605)
        time.sleep(1.5 * multiplier)
        pyautogui.click(1324, 343)
        time.sleep(1 * multiplier)
        pyautogui.press('enter')
        pyautogui.click(1028,603)
        
        completed_tasks += 1

        # DCTF programa abrir
        time.sleep(1 * multiplier)
        pyautogui.press('win')
        time.sleep(1 * multiplier)
        pyautogui.write('dctf')
        time.sleep(1 * multiplier)
        pyautogui.press('enter')
        time.sleep(30 * multiplier)

        completed_tasks += 1

        # importar arquivo
        pyautogui.click(29,39)
        pyautogui.click(81,120)
        pyautogui.doubleClick(642,600)
        pyautogui.click(1035,543) 
        pyautogui.click(1306,533)
        pyautogui.click(1074,609) # ok button
        pyautogui.click(1286,576) # cancel button

        completed_tasks += 1

        # Abrir arquivo
        pyautogui.click(57,72)
        pyautogui.click(1064,733)
        
        completed_tasks += 1

        # Gravando arquivo
        pyautogui.click(x=150, y=70)
        pyautogui.click(x=863, y=746)
        pyautogui.click(x=1153, y=606)

        completed_tasks += 1

        # Trasnmitir arquivo
        pyautogui.click(x=230, y=68)
        pyautogui.click(x=1166, y=536)
        pyautogui.click(x=866, y=513)
        pyautogui.click(x=574, y=712)
        pyautogui.click(x=974, y=717)
        pyautogui.click(723,450) # seleciona primeiro na lista de certificados (necessaria logica de seleção)
        pyautogui.click(896,783) # assinar button
        pyautogui.click(1154,669)

        completed_tasks += 1

        # Clean All
        pyautogui.click(x=50, y=41)
        pyautogui.click(x=122, y=201)
        pyautogui.click(x=1072, y=739)
        pyautogui.click(x=953, y=733)
        pyautogui.click(x=895, y=697)

        completed_tasks += 1

        time.sleep(2)

        #browser
        files = os.listdir(source_folder)
        os.makedirs(destination_folder, exist_ok=True)

        #copy
        for file_name in files:
            if file_name.endswith('.rfb'):
                source_file_path = os.path.join(source_folder, file_name)
                destination_file_path = os.path.join(destination_folder, file_name)
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Copied: {file_name}")
        #delete
        for file_name in files:
            if file_name.endswith('.rfb'):
                file_path = os.path.join(source_folder, file_name)
                os.remove(file_path)
                print(f"Deleted: {file_name}")
        print("Operations completed successfully.")

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

#project_selector_label = tk.Label(frame, text="DCTF Automation                    ", bg='#FFECA1', font=font_style_label)
#project_selector_entry = tk.Entry(frame, width=20)
#project_selector_entry.grid(row=2, column=1, pady=20, padx=0, sticky='e')
#project_selector_entry.insert
#project_selector_label.grid(row=2, column=0, columnspan=2, pady=10, padx=50, sticky= 'e')

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
