import tkinter as tk
from tkinter import messagebox
from threading import Thread
from LoginDominioWeb import enviar_dctf

def start_automation():
    cnpj = cnpj_entry.get()
    periodo = periodo_entry.get()
    if not cnpj or not periodo:
        messagebox.showwarning("Entrada Inválida", "Por favor, preencha todos os campos.")
        return
    
    thread = Thread(target=enviar_dctf, args=(cnpj, periodo))
    thread.start()

app = tk.Tk()
app.title("Automação DCTF")

tk.Label(app, text="CNPJ:").grid(row=0)
tk.Label(app, text="Período:").grid(row=1)

cnpj_entry = tk.Entry(app)
periodo_entry = tk.Entry(app)

cnpj_entry.grid(row=0, column=1)
periodo_entry.grid(row=1, column=1)

tk.Button(app, text="Iniciar", command=start_automation).grid(row=2, column=0, columnspan=2)

app.mainloop()
