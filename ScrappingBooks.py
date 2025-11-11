from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
time.sleep(2)

livros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

dados_livros = []

for livro in livros:
    titulo = livro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
    preco = livro.find_element(By.CSS_SELECTOR, "p.price_color").text
    estoque = livro.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
    dados_livros.append([titulo, preco, estoque])

for l in dados_livros:
    print(l)

print("\nColeta finalizada com sucesso!")

driver.quit()