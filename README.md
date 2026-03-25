# CT-e Extractor

Projeto em Python para leitura de arquivos XML de CT-e (Conhecimento de Transporte Eletrônico),
extração dos principais campos e exportação para Excel.

## Funcionalidades
- Interface gráfica simples (Tkinter)
- Seleção de múltiplos arquivos XML
- Extração de dados como número do CT-e, emitente, destinatário, valores, origem/destino
- Exportação para Excel


# Passo 1 – Criar a venv
No prompt de comando (CMD ou PowerShell), dentro da pasta do seu projeto:

```bash
python -m venv venv
```
Isso cria uma pasta chamada venv com o ambiente virtual.

# Passo 2 – Ativar a venv
No Windows:

```bash
venv\Scripts\activate.bat
```

No PowerShell:

```bash
venv\Scripts\Activate.ps1
```
Você vai ver (venv) no início da linha, indicando que está ativo.

# Passo 3 – Instalar dependências
Instale o PyInstaller e as bibliotecas que seu projeto usa:

```bash
python -m pip install -r requirements.txt
```
# Passo 4 – Testar o app
Antes de compilar, rode para garantir que funciona:

```bash
python app.py
```
# Passo 5 – Gerar o executável
Com tudo funcionando, rode:

```bash
python -m PyInstaller --onefile --noconsole app.py
```

--onefile → gera um único .exe
--noconsole → não abre janela de terminal junto

# Passo 6 – Localizar o executável
O arquivo final estará em:


dist\app.exe
Esse é o executável portátil que você pode distribuir.

