# Objetivo: abrir uma playlist no youtube
def pausa():
    time.sleep(1)


# 1 - abrir o navegador
import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pausa()
pyautogui.write("chrome")
pyautogui.press("enter")
pausa()

# 2 - entrar no youtube
pyautogui.click(x=980, y=556)
pyautogui.write("youtube")
pausa()
pyautogui.press("enter")
pausa()
pyautogui.click(x=381, y=416)
pausa()

# 3 - digitar o nome da banda
pyautogui.click(x=813, y=195)
pyautogui.write("twenty one pilots")
pausa()
pyautogui.press("enter")
pausa()

# 4 - tocar a playlist
pyautogui.click(x=1496, y=679)
