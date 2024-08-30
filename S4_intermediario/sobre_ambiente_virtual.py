# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env


############ Criando ambientes virtuais ############

# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv venv


#### Ativando e desativando um ambiente virtual ####

# Windows:
# .\venv\Scripts\activate

# Linux e Mac:
# source venv/bin/activate

# Desativar: deactivate


##### Instalando pacotes e bibliotecas com pip #####

# Instalar última versão:
# pip install nome_pacote

# Instalar versão precisa:
# (tem outras formas também não mencionadas)
# pip install nome_pacote==0.0.0

# Desinstalar pacote:
# pip uninstall nome_pacote

# Congelar (ver pacotes):
# pip freeze

# Atualizar pip:
# python.exe -m pip install --upgrade pip


####### Criando e usando um requirements.txt #######

# Para criar:
# pip freeze > requirements.txt

# Para instalar tudo dele:
# pip install -r requirements.txt


###### Desinstalando todos pacotes de uma vez: #####

'''
pip freeze > requirements.txt
Get-Content requirements.txt | ForEach-Object { pip uninstall -y $_ }
Remove-Item requirements.txt  # OPCIONAL
'''
