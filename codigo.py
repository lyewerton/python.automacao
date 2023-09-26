import pyautogui
import time
import pandas
pyautogui.PAUSE = 0.3

# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # abrir o chrome
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

    # entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

    # esperar o site carregar   testando
time.sleep(1)

# Passo 2: Fazer login
pyautogui.click(x=672, y=358)
pyautogui.write("lyewerton008@gmail.com")

pyautogui.press("tab")
pyautogui.write("12345")

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# Passo 3: Importar a base de dados de produtos
tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Passo 5: Repetir o cadastro para todos os produtos
for linha in tabela.index:

    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=732, y=248)

    codigo = tabela.loc[linha, "codigo"]


    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    time.sleep(0.4)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # Enviar
    pyautogui.press("tab")
    pyautogui.press("enter")


    pyautogui.scroll(50000)


# pip instal pyautogui
# pip instal pandas numpy openpyxl


# pyautogui.click -> CLicar com o mouse
# pyautogui.write -> Escrever um texto
# pyautogui.press -> Apertar 1 tecla
# pyautogui.hotkey -> atalho (Combinação de teclas)