import tkinter as tk
from tkinter import filedialog, messagebox
import os
from parser.cte_parser import extrair_dados_cte
from exporter.excel_exporter import exportar_para_excel

def processar_arquivos():
    files = filedialog.askopenfilenames(filetypes=[("XML files", "*.xml")])
    if not files:
        return
    
    dados = []
    for file in files:
        try:
            dados.append(extrair_dados_cte(file))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar {file}: {e}")

    if dados:
        # Salvar na área de trabalho
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        caminho_excel = os.path.join(desktop, "resultado.xlsx")

        caminho_excel = exportar_para_excel(dados, "resultado.xlsx")
        messagebox.showinfo("Sucesso", f"Excel gerado com sucesso na pasta Downloads:\n{caminho_excel}")



def iniciar_interface():
    root = tk.Tk()
    root.title("Processador de CT-e")
    root.geometry("600x400")  # aumenta o tamanho da janela

    titulo = tk.Label(root, text="Adicione os arquivos CT-e aqui no formato XML", font=("Arial", 14))
    titulo.pack(pady=20)

    btn = tk.Button(root, text="Selecionar Arquivos XML", font=("Arial", 12), command=processar_arquivos)
    btn.pack(pady=40)

    root.mainloop()
