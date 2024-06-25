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
            # valores = row['valores'] # use valores if needed in the automation
            thread = Thread(target=enviar_dctf, args=(cnpj, periodo))
            thread.start()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o arquivo CSV: {e}")

app = tk.Tk()
app.title("Automação DCTF")

# Modern styling
app.geometry('400x200')
app.configure(bg='#f5f5f5')

tk.Label(app, text="Arquivo CSV:", bg='#f5f5f5', font=('Helvetica', 12)).grid(row=0, column=0, pady=10, padx=10)
cnpj_entry = tk.Entry(app, width=40)
cnpj_entry.grid(row=0, column=1, pady=10, padx=10)

tk.Button(app, text="Upload CSV", command=upload_csv, bg='#0073e6', fg='white', font=('Helvetica', 12)).grid(row=1, column=0, pady=10, padx=10)
tk.Button(app, text="Iniciar", command=start_automation, bg='#28a745', fg='white', font=('Helvetica', 12)).grid(row=1, column=1, pady=10, padx=10)

app.mainloop()
