driver = webdriver.Chrome()  

driver.get("https://books.toscrape.com/")
time.sleep(2)  # espera 2 segundos pra garantir o carregamento

livros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

dados_livros = []

for livro in livros:
    titulo = livro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
    preco = livro.find_element(By.CSS_SELECTOR, "p.price_color").text
    estoque = livro.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
    dados_livros.append([titulo, preco, estoque])

# Exibe no terminal
for l in dados_livros:
    print(l)

# Salva em CSV
with open("livros_selenium.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Título", "Preço", "Estoque"])
    writer.writerows(dados_livros)

print("\nArquivo 'livros_selenium.csv' criado com sucesso!")

# Fecha o navegador
driver.quit()
