import pandas as pd
import os

def exportar_para_excel(dados, nome_arquivo="resultado.xlsx"):
    # Obtém o caminho da pasta Downloads do usuário
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")

    # Garante que o diretório existe
    if not os.path.exists(downloads):
        raise FileNotFoundError("Não foi possível localizar a pasta Downloads.")

    # Define o caminho completo do arquivo
    caminho_excel = os.path.join(downloads, nome_arquivo)

    # Cria o DataFrame e salva no Excel
    df = pd.DataFrame(dados)
    df.to_excel(caminho_excel, index=False)

    return caminho_excel
