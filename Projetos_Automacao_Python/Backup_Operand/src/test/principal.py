from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pyautogui
import os
import subprocess  # Biblioteca para executar outro arquivo .py

#configurar as opções do chrome
chrome_options = Options ()
chrome_options.add_experimental_option("detach", True)  # Manter a janela aberta

# Instalar o driver do Chrome
servico = Service(ChromeDriverManager().install())

# Inicializar o navegador com as opções configuradas
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Maximizar a janela do navegador
navegador.maximize_window()

# Abrir a página desejada
navegador.get("https://app3.operand.com.br/arquivos")

# Preenchendo dados para login
navegador.find_element('xpath', '//*[@id="email"]').send_keys("financeiro@agenciacondao.com.br")
navegador.find_element('xpath', '//*[@id="password"]').send_keys("Financeiro@2023")

# Clicando em 'Entrar'
navegador.find_element('xpath', '//*[@id="do-login"]').click()

# Esperar a página carregar (ajuste conforme necessário)
time.sleep(5)



# Clicar no botão de filtro
navegador.find_element(By.XPATH, '//*[@id="btn-filtros"]').click()

# Esperar o campo de data ficar visível
time.sleep(2)  # Ajuste o tempo conforme necessário

# Clicar no campo de data para abrir o seletor de datas
navegador.find_element(By.XPATH, '//*[@id="find_date"]').click()

# Esperar o seletor de datas aparecer
time.sleep(2)  # Ajuste o tempo conforme necessário

# Selecionar a opção "Personalizado"
navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/ul/li[5]').click()

# Esperar o campo de data personalizado ficar visível
time.sleep(2)  # Ajuste o tempo conforme necessário



# Selecionar a data de início: xx/xx/xxx
# Selecionar ano de início
ano_inicio = Select(navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/table/thead/tr[1]/th[2]/select[2]'))
ano_inicio.select_by_visible_text("2021")

# Selecionar mês de início
mes_inicio = Select(navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/table/thead/tr[1]/th[2]/select[1]'))
mes_inicio.select_by_visible_text("Agosto")

#ALTERAR DIA INÍCIO
# Selecionar dia de início
navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()  # 1º dia

# Selecionar a data de fim: xx/xx/xxxx
# Selecionar ano de fim
ano_fim = Select(navegador.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/table/thead/tr[1]/th[2]/select[2]'))
ano_fim.select_by_visible_text("2021")

# Selecionar mês de fim
mes_fim = Select(navegador.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/table/thead/tr[1]/th[2]/select[1]'))
mes_fim.select_by_visible_text("Agosto")

#ALTERAR DIA FIM
# Selecionar dia de fim
navegador.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/table/tbody/tr[6]/td[2]').click()  # xxº dia

# Confirmar a seleção das datas
navegador.find_element(By.CSS_SELECTOR, 'body > div.daterangepicker.dropdown-menu.opensright.show-calendar > div.ranges > div > button.applyBtn.btn.btn-sm.btn-success').click()



# Esperar para garantir que a seleção de datas foi confirmada
time.sleep(2)  # Ajuste o tempo conforme necessário

# Clicar no botão "Buscar"
navegador.find_element(By.XPATH, '//*[@id="btn-filtrar"]').click()

# Esperar a página recarregar com os novos filtros
time.sleep(5)


# Função para rolar a página até o final
def rolar_ate_fim_pagina(driver):
    prev_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)  # Ajuste o tempo conforme necessário
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height

# Rola até o fim da página para carregar todos os arquivos
rolar_ate_fim_pagina(navegador)

# Encontrar todos os elementos de arquivos PDF e clicar neles
arquivos_pdf = navegador.find_elements(By.XPATH, '//div[@class="mini-holder other-files pdf"]/..')


# Diretório de destino para salvar os PDFs
destino = r'C:\Users\mateu\Desktop\Anexos OPERAND\2021\AGO'

# Salva as posições com as coordenadas obtidas (para definir destino)
#campo_nome_x, campo_nome_y = 100, 200  # Verificar valores reais quando eu precisar
campo_diretorio_x, campo_diretorio_y = 662, 206  # Coordenadas definição diretorio
campo_salvar_x, campo_salvar_y = 776, 636 # Coordenadas botão salvar

# Função para salvar arquivos PDF usando PyAutoGUI
def salvar_pdf(destino):
    if keyboard.is_pressed('esc'): #Tecla esc definida: parar
        print("Interrupção pelo usuário")
        return
    
    time.sleep(4)  # Esperar um momento para garantir que a página esteja carregada
    pyautogui.hotkey('ctrl', 's')  # Pressionar Ctrl+S para abrir a janela de salvar
    time.sleep(2)  # Esperar a janela abrirC:\Users\mateu\Desktop\Anexos OPERAND\Downloads_automacao

    # Mover para o campo do diretório e colar o destino
    pyautogui.click(campo_diretorio_x, campo_diretorio_y)
    pyautogui.typewrite(destino)  # Escrever o caminho do diretório
    pyautogui.press('enter')  # Confirmar o diretório
    time.sleep(2)  # Esperar um momento para o diretório ser confirmado
    pyautogui.click(campo_salvar_x, campo_salvar_y)
    #pyautogui.press('enter')  # Salvar o arquivo
    time.sleep(2)

# Abrir cada arquivo PDF em uma nova aba e salvá-lo
for arquivo in arquivos_pdf:
    try:
        # Clicar no link do arquivo PDF
        arquivo.click()
        time.sleep(2)  # Esperar a nova aba carregar

        # Alternar para a nova aba
        navegador.switch_to.window(navegador.window_handles[-1])

        # Salvar o PDF
        salvar_pdf(destino)

        # Fechar a aba atual
        navegador.close()

        # Voltar para a aba original
        navegador.switch_to.window(navegador.window_handles[0])
    except Exception as e:
        print(f"Erro ao clicar no arquivo: {e}")


