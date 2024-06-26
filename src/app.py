import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread
import pandas as pd
import pyautogui
import time

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
        for index, row in df.iterrows():
            thread = Thread(target=run_automation, args=(row, sleep_multiplier))
            thread.start()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o arquivo CSV: {e}")

def run_automation(row, multiplier):
# Login Dominio Web
    
    pyautogui.hotkey('win', 'r')
    pyautogui.press('edge', interval=0.5 * multiplier)
    time.sleep(2 * multiplier)
    
    pyautogui.write('https://dominio-web.thomsonreuters.com', interval=0.4 * multiplier)
    time.sleep(5 * multiplier)
    
    pyautogui.click(x=400, y=300)
    pyautogui.typewrite('usuario\n', interval=0.1 * multiplier)
    pyautogui.typewrite('senha\n', interval=0.1 * multiplier)
    pyautogui.press('enter')
    time.sleep(5 * multiplier)
    
    pyautogui.click(x=400, y=400)
    time.sleep(3 * multiplier)
    
    #Simulating aut0 tasks
    #for key, value in row.items():
        #pyautogui.typewrite(f"{key}: {value}\n", interval=0.1 * multiplier)
        #time.sleep(1 * multiplier)
    
    #pyautogui.hotkey('alt', 'f4')

# Dominio Web
    tabela = pd.read_csv(r"C:\Users\PC\Desktop\Área de Trabalho\ByteVault\PROJETOS\Controllers\DCTF-Automation\DCTF-Automation\tests\dados.csv") # "EMPRESASID.csv = Relatorio Padrão Ajustavel.csv"
    print(tabela)
    for linha in tabela.index:
        start_time = time.time()
    pyautogui.doubleClick(162, 113)
    time.sleep(1)
    data = tabela.loc[linha, "CODIGO"]
    pyautogui.write(str(tabela.loc[linha, "CODIGO"]))
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.doubleClick(510, 62) #PASSO 2 :
    time.sleep(1.5)
    pyautogui.doubleClick(588, 133)
    time.sleep(1.5)
    pyautogui.doubleClick(789, 128)
    time.sleep(1.5)
    pyautogui.doubleClick(x=1019, y=267) #x=1055, y=239)
    time.sleep(1.5)
    pyautogui.doubleClick(x=1306, y=271) #x=1354, y=240)
    time.sleep(1.5)
    data = tabela.loc[linha, "DATA"]
    pyautogui.write(str(tabela.loc[linha, "DATA"]))
    pyautogui.press('enter')
    time.sleep(0.25)
    pyautogui.click(1087, 736) #...
    pyautogui.click(1222, 390) #setinha icon
    pyautogui.click(1181, 425) #clinte M 
    pyautogui.click(x=757, y=468) #pasta DCTF
    pyautogui.click(x=1104, y=678) #Ok 
    pyautogui.click(855, 742) #campo da escrita
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    empresa = tabela.loc[linha, "EMPRESA"]
    pyautogui.write(str(tabela.loc[linha, "EMPRESA"]))
    time.sleep(0.20)
    pyautogui.click(1234, 397) #exportar butão
    time.sleep(7)
    pyautogui.click(1026, 605)
    pyautogui.click(1324, 343)
    time.sleep(1)
	
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos")

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

app = tk.Tk()
app.title("Automação DCTF")
app.geometry('800x400')
app.configure(bg='#FFECA1')

font_style_title = ('Helvetica', 16, 'bold')
font_style_label = ('Helvetica', 12)
font_style_button = ('Helvetica', 12, 'bold')

tk.Label(app, text="Arquivo CSV:", bg='#FFECA1', font=font_style_label).grid(row=0, column=0, pady=20, padx=20, sticky='e')
cnpj_entry = tk.Entry(app, width=60)
cnpj_entry.grid(row=0, column=1, pady=20, padx=10, sticky='w')

upload_button = tk.Button(app, text="Upload CSV", command=upload_csv, bg='#4169e1', fg='white', font=font_style_button, relief='raised')
upload_button.grid(row=1, column=0, pady=10, padx=20)

tk.Label(app, text="Multiplicador de Tempo:", bg='#FFECA1', font=font_style_label).grid(row=2, column=0, pady=20, padx=20, sticky='e')
sleep_multiplier_entry = tk.Entry(app, width=10)
sleep_multiplier_entry.grid(row=2, column=1, pady=20, padx=10, sticky='w')
sleep_multiplier_entry.insert(0, "1.0")  # Valor padrão

start_button = tk.Button(app, text="Iniciar", command=start_automation, bg='#228b22', fg='white', font=font_style_button, relief='raised')
start_button.grid(row=3, column=1, pady=10, padx=10, sticky='w')

help_button = tk.Button(app, text="Ajuda", command=show_help, bg='#FFA500', fg='white', font=font_style_button, relief='raised')
help_button.grid(row=3, column=0, pady=10, padx=10, sticky='e')

estimated_time_label = tk.Label(app, text="Estimativa de tempo de execução: N/A", bg='#FFECA1', font=font_style_label)
estimated_time_label.grid(row=4, column=0, columnspan=2, pady=20, padx=20)

app.mainloop()
