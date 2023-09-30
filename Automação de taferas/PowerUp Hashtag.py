# Passo a passo do projeto
# Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Imortar a base de dados de produtos
import pyautogui #biblioteca
import time

# pyautogui.click -> clica com o mouse
# pyautogui.write -> escreve
# pyautogui.press -> aperta 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas ex: ctrl + c)

pyautogui.PAUSE = 1

# Abrir o chrome
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write (link)
pyautogui.press ("enter")

# esperar o site carregar
time.sleep(8)

# Fazer login
pyautogui.click (x=894, y=406) 
pyautogui.write ("teste@hotmail.com")

pyautogui.click (x=885, y=509)
pyautogui.write ("Teste@123")

pyautogui.press ("enter")

time.sleep(3)

# Imortar a base de dados de produtos
import pandas

tabela = pandas.read_csv("produtos.csv")
print (tabela)

for linha in tabela.index:

    # Cadastrar um produto
    pyautogui.click (x=751, y=292)

    codigo = tabela.loc[linha, "codigo"]

    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, obs]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    # apertar para enviar 
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll (50000 )

# 5º Repetir o cadastro para os demais produtos


 