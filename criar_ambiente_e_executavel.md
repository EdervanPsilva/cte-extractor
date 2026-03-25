# Passo 1 – Criar a venv
No prompt de comando (CMD ou PowerShell), dentro da pasta do seu projeto:

cmd
python -m venv venv
Isso cria uma pasta chamada venv com o ambiente virtual.

# Passo 2 – Ativar a venv
No Windows:

cmd
venv\Scripts\activate.bat

No PowerShell:

powershell
venv\Scripts\Activate.ps1
Você vai ver (venv) no início da linha, indicando que está ativo.

# Passo 3 – Instalar dependências
Instale o PyInstaller e as bibliotecas que seu projeto usa:

cmd
pip install pyinstaller

# Passo 4 – Testar o app
Antes de compilar, rode para garantir que funciona:

cmd
python app.py

# Passo 5 – Gerar o executável
Com tudo funcionando, rode:

cmd
python -m PyInstaller --onefile --noconsole app.py

--onefile → gera um único .exe
--noconsole → não abre janela de terminal junto

# Passo 6 – Localizar o executável
O arquivo final estará em:

Código
dist\app.exe
Esse é o executável portátil que você pode distribuir.

