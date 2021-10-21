from selenium import webdriver

navegador = webdriver.Firefox()
navegador.get('http://localhost:8000')

assert 'Django' in navegador.title