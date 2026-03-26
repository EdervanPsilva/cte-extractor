import tkinter as tk
from tkinter import filedialog, messagebox, ttk
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
        caminho_excel = exportar_para_excel(dados, "resultado.xlsx")
        messagebox.showinfo("Sucesso", f"Excel gerado com sucesso:\n{caminho_excel}")

def iniciar_interface():
    root = tk.Tk()
    root.title("CT-e Extractor")
    root.geometry("700x500")
    root.configure(bg="white")  # fundo branco

    # Estilo ttk minimalista
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TButton",
                    font=("Segoe UI", 12),
                    padding=10,
                    background="#0078D7",   # azul moderno para o botão
                    foreground="white")
    style.map("TButton", background=[("active", "#005a9e")])
    style.configure("TLabel",
                    font=("Segoe UI", 12),
                    background="white",
                    foreground="black")
    style.configure("TLabelframe",
                    background="white",
                    foreground="black",
                    font=("Segoe UI", 12, "bold"))
    style.configure("TLabelframe.Label",
                    background="white",
                    foreground="black",
                    font=("Segoe UI", 12, "bold"))

    # Cabeçalho simples
    titulo = ttk.Label(root, text="CT-e Extractor", font=("Segoe UI", 20, "bold"))
    titulo.pack(pady=(30,10))

    subtitulo = ttk.Label(root, text="Ferramenta para leitura e exportação de CT-e (XML)", font=("Segoe UI", 12))
    subtitulo.pack(pady=(0,20))

    # Botão central
    btn = ttk.Button(root, text="Selecionar Arquivos XML", command=processar_arquivos)
    btn.pack(pady=20)

    # Quadro de informações com título preto
    info_frame = ttk.LabelFrame(root, text="Funcionalidades", padding=15)
    info_frame.pack(fill="both", expand=True, padx=40, pady=30)

    info_text = (
        "• Seleção de múltiplos arquivos XML de CT-e\n"
        "• Extração dos principais campos:\n"
        "   - Número do CT-e\n"
        "   - Emitente e Destinatário\n"
        "   - Valores\n"
        "   - Origem e Destino\n"
        "• Exportação automática para Excel\n"
        "• Arquivo salvo na pasta Downloads com o nome resultado.xlsx"
    )

    lbl_info = ttk.Label(info_frame, text=info_text, justify="left", font=("Segoe UI", 11))
    lbl_info.pack(anchor="w")

    # Rodapé discreto
    rodape = ttk.Label(root, text="© 2026 - Ferramenta de Processamento CT-e",
                       font=("Segoe UI", 9), foreground="black", background="white")
    rodape.pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    iniciar_interface()
