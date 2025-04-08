import pyautogui
import time
# pyaoutogui -> fazer automações com python: pip install pyautogui
# documentação da biblioteca : https://pyautogui.readthedocs.io/en/latest/quickstart.html
# pyautogui.click -> clica em algum lugar
# pyautogui.press -> aperta 1 tecla
# pyautogui.write -> escreve um texto
# ppyautogui.hotkey -> aperta uma combinação de teclas
# pyautogui.PAUSE = 0.5 -> para pausar meio segundo em cada passo
# pyautogui.click() -> pegar o lugar do click em outro arquivo e botar entre os ()
# pyautogui.scroll(10000) -> rolar pra cima, negativo é pra baixo, teste até cair onde quer

# para apertar botão direito ou 2 clicks -> pyautogui.click(x=948, y=338, button="right" ou clicks=2)



pyautogui.PAUSE = 0.5

# Passo 1: Entrar no Sistema da Empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")


# digitar o site
# precisa de delay para dar certo pois sem delay é muito rapido
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


# espera 3 segundos
time.sleep(3)

# Passo 2: Fazer Login ----------------------------------------------

# ATENÇÃO USE 1 TELA PRINCIPAL

pyautogui.click(x=948, y=338)
pyautogui.click(x=645, y=364)
pyautogui.write("pythonkabulozo@gmail.com")

# preencher a senha

pyautogui.press("tab")
pyautogui.write("minhasenhasecreta")

# botão logar
pyautogui.press("tab")
pyautogui.press("enter")

# espera mais 3 segundos
time.sleep(3)


# Passo 3: Importar a base de dados ------------------------------------------
# pip install pandas -- para instalar o pandas
import pandas
# para encontrar o arquivo tem que mostra o caminho c://caminho, criar uma variavel para guardar
tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar 1 produto -----------------------------------------------
# para cada linha da tabela executa, seleciona tudo e identa com tab, tem que esta dentro da identação do for
# para cada linha da tabela executa o index que é cada linha de uma lista
for linha in tabela.index:
    pyautogui.click(x=669, y=247)
# no tabela.loc[linha,coluna] o algoritmo localiza onde tá a informação para passar, isso com o .loc entre [] que é uma lista
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o proximo campo

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab") # passar para o proximo campo

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab") # passar para o proximo campo

    categoria = str(tabela.loc[linha,"categoria"]) # string = texto -> str()
    pyautogui.write(categoria)
    pyautogui.press("tab") # passar para o proximo campo

    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab") # passar para o proximo campo  
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab") # passar para o proximo campo

    obs = str(tabela.loc[linha,"obs"])
# se observação não for nan execute
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab") # passou para o botão enviar
    pyautogui.press("enter") # enviou

    pyautogui.scroll(10000) 



# Passo 5: Repetir para todos os produtos-------------------------------------

# nan -> Not a Number