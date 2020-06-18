import json

from selenium import webdriver

# Salvar a página na variável site
site = 'https://dc.fandom.com/wiki/Category:Good_Characters'

# Inicializar o dicionário
myDict = {'personagens': []}

# Criar instância do navegador
driver = webdriver.Chrome()

# Maximizar o browser
driver.maximize_window()

# Abrir a página do DC Wikia Good Characters
driver.get(site)

# Inicializar a variável contador com 0 para o laço de repetição
contador = 0

# Pegar o link para ir para a próxima página
proximo = driver.find_element_by_class_name('category-page__pagination-next')

# Laço de repetição para percorrer todos os good characters
while contador < 62:
    # Testar
    print(contador)

    # Aguardar 25 segundos para a página ser toda carregada
    driver.implicitly_wait(25)

    # Selecionar todos os elementos que possuem a class category-page__member
    personagens = driver.find_elements_by_class_name('category-page__member')

    # Imprimir informações para cada post encontrado
    for p in personagens:
        # Pegar o nome do personagem
        personagem = p.find_element_by_class_name('category-page__member-link')

        # Pegar o link do post
        link = personagem.get_attribute('href')

        # Imprimir o título do post
        # print(u"Personagem: {personagem}".format(personagem=personagem.text))

        # Imprimir o link do post
        # print(u"Link: {link}".format(link=link))

        # Armazenar as informações em um dicionário
        myDict['personagens'].append(({"Personagem": "{personagem}".format(personagem=personagem.text),
                                       "Link": "{link}".format(link=link)
                                       }))

    # Verificar se chegou ao fim do laço, chegando para a execução do laço de repetição
    if contador == 61:
        break

    # Incrementar o contador
    contador += 1

    # Pegar o link para ir para a próxima página
    proximo = driver.find_element_by_class_name('category-page__pagination-next')

    # Pegar o link para ir para a próxima página de personagens
    site = proximo.get_attribute('href')

    # Abrir a próxima página
    driver.get(site)

# Salvar os dados do dicionário em um arquivo JSON
with open('dadosDcWikia.json', 'w') as json_file:
    json.dump(myDict, json_file, indent=4)

# Fechar o navegador
driver.quit()
