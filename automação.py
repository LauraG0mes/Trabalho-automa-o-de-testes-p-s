from time import sleep
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions


def test_automacao():
    """Rotina principal"""
    # Copia o caminho do diretório atual
    diretorio = pathlib.Path(__file__).parent.resolve()

    # Ajusta Opções para carregar o chrome
    opcoes_chrome = ChromeOptions()
    # opcoes_chrome.add_argument("--headless")
    opcoes_chrome.add_argument(" --no-sandbox ")
    driver = webdriver.Chrome(options=opcoes_chrome)

    # Abre o HTML
    driver.get("http://127.0.0.1:5500/sample-exercise.html")

    # Clica no botao para gerar o codigo
    geracodigo = driver.find_element(By.NAME, "generate")
    geracodigo.click()

    # Aguarda até que o campo não esteja mais vazio
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "my-value")
        .get_attribute("textContent") != ""
    )

    # Identifica o campo que contém o código gerado
    codigo = driver.find_element(By.ID, "my-value")

    # Identifica o campo de entrada
    entrada = driver.find_element(By.ID, "input")
    entrada.clear()   # limpa o campo
    entrada.send_keys(codigo.text)    # escreve o codigo gerado

    # Identifica o botão "test"
    test_bnt = driver.find_element(By.NAME, "button")
    test_bnt.click()    # clica no botão

    # Identifica o Alert
    alert = driver.switch_to.alert
    alert.accept()  # Clica no botão para fechar o Alert

    # Identifica o campo com o texto final
    resultado = driver.find_element(By.ID, "result")

    # Verifica se o campo resultado está com o texto correto
    assert resultado.text == f"It workls! {codigo.text}!"

    sleep(5)    # pausa para ver o resultado

    driver.quit()   # fecha o navegador