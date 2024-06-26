import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread
import pandas as pd
from LoginDominioWeb import enviar_dctf

def upload_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            if not {'cnpj', 'periodo', 'valores'}.issubset(df.columns):
                messagebox.showerror("Erro", "O CSV deve conter as colunas: 'cnpj', 'periodo' e 'valores'.")
                return
            cnpj_entry.delete(0, tk.END)
            cnpj_entry.insert(0, file_path)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo CSV: {e}")

def start_automation():
    file_path = cnpj_entry.get()
    if not file_path:
        messagebox.showwarning("Entrada Inválida", "Por favor, faça upload de um arquivo CSV.")
        return

    try:
        df = pd.read_csv(file_path)
        for index, row in df.iterrows():
            cnpj = row['cnpj']
            periodo = row['periodo']
            thread = Thread(target=enviar_dctf, args=(cnpj, periodo))
            thread.start()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o arquivo CSV: {e}")

# Criar a aplicação e configurar a interface gráfica
app = tk.Tk()
app.title("Automação DCTF")
app.geometry('800x300')
app.configure(bg='#FFECA1')

# Estilo de Fonte
font_style = ('Oswald', 14)

# Rótulo e Entrada para Arquivo CSV
tk.Label(app, text="Arquivo CSV:", bg='#FFECA1', font=font_style).grid(row=0, column=0, pady=20, padx=20, sticky='e')
cnpj_entry = tk.Entry(app, width=60)
cnpj_entry.grid(row=0, column=1, pady=20, padx=10, sticky='w')

# Botão de Upload CSV
upload_button = tk.Button(app, text="Upload CSV", command=upload_csv, bg='#4169e1', fg='white', font=font_style)
upload_button.grid(row=1, column=0, pady=10, padx=20)

# Botão de Iniciar Automação
start_button = tk.Button(app, text="Iniciar", command=start_automation, bg='#228b22', fg='white', font=font_style)
start_button.grid(row=1, column=1, pady=10, padx=10, sticky='w')

# Iniciar o loop principal da aplicação
app.mainloop()
