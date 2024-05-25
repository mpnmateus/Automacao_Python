import pyautogui
import time

pyautogui.alert("O código vai começar")

pyautogui.PAUSE = 0.5

#abre o navegador chrome
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')

#clica no usuário contato condão
pyautogui.moveTo(420, 449)
pyautogui.mouseDown()
pyautogui.mouseUp()

#digita o endereço arquivos operand no navegador
#time.sleep(1)
pyautogui.write("https://app3.operand.com.br/arquivos")
pyautogui.press('enter')

#clica no botão de login para acessar a página dos anexos
time.sleep(2)
pyautogui.moveTo(358, 633)
pyautogui.mouseDown()
pyautogui.mouseUp()

#esperar 10 segundos para a página carregar
time.sleep(10)


pyautogui.alert("O parou de rodar. Pode voltar a usar seu PC.")