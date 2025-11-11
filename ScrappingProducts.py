from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get("https://www.amazon.com.br/s?k=notebook")
time.sleep(3)


produtos = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")

dados_produtos = []

for produto in produtos:
    try:
        titulo = produto.find_element(By.CSS_SELECTOR, "h2 a span").text
    except:
        titulo = "Título não encontrado"
    try:
        preco = produto.find_element(By.CSS_SELECTOR, "span.a-price span.a-offscreen").text
    except:
        preco = "Preço não disponível"

    dados_produtos.append([titulo, preco])


for p in dados_produtos:
    print(p)

print("\nColeta finalizada com sucesso!")

