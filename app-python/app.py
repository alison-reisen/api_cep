import requests
import tkinter as tk

from tkinter import messagebox

def consultar_cep():
    cep = entry_cep.get()
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        if 'erro'not in data:
            messagebox.showinfo( title= "Resultado do CEP:"  + " " +str(cep), message=
                f"CEP: {data['cep']}\n"
                f"LOCALIDADE: {data['localidade']}\n"
                f"UF: {data['uf']}\n"
                f"LOGRADOURO: {data['logradouro']}\n"
                f"BAIRRO: {data['bairro']}\n"
                f"COMPLEMENTO: {data['complemento']}\n"
                f"IBGE: {data['ibge']}\n"
                f"DDD: {data['ddd']}\n"
                )
            
            
        else:
            messagebox.showerror("CEP não encontrado")
    else:
        messagebox.showerror("Erro ao consultar o CEP")    

#consultar_cep("77001-040")

janela = tk.Tk()
janela.geometry("360x180")
janela.title("Consulta de CEP")


label_cep = tk.Label(janela, text="Digite o Cep:")
label_cep.grid(row=0, column=0, padx=5, pady=10)
entry_cep = tk.Entry(janela, width=20 )
entry_cep.grid(row= 0, column= 1, padx=5, pady=10)


button_consultar = tk.Button(janela, text="Consultar", command=consultar_cep)
button_consultar.grid(row=0, column=2)


janela.mainloop()
