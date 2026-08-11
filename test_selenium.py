import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # roda sem abrir janela
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

def test_fluxo_completo(driver):
    # 1. Login
    driver.get("http://localhost:5000/login")
    driver.find_element(By.NAME, "email").send_keys("admin@teste.com")
    driver.find_element(By.NAME, "senha").send_keys("1234" + Keys.RETURN)
    assert "Dashboard" in driver.page_source

    # 2. Criar chamado
    driver.get("http://localhost:5000/chamados/novo")
    driver.find_element(By.NAME, "titulo").send_keys("Chamado Selenium")
    driver.find_element(By.NAME, "descricao").send_keys("Teste automatizado com Selenium")
    driver.find_element(By.NAME, "categoria").send_keys("TI" + Keys.RETURN)
    assert "Chamado criado com sucesso" in driver.page_source

    # 3. Editar chamado (exemplo com ID=1)
    driver.get("http://localhost:5000/chamados/editar/1")
    status_field = driver.find_element(By.NAME, "status")
    status_field.clear()
    status_field.send_keys("Resolvido" + Keys.RETURN)
    assert "Chamado atualizado com sucesso" in driver.page_source

    # 4. Excluir chamado (exemplo com ID=1)
    driver.get("http://localhost:5000/chamados/excluir/1")
    assert "Chamado excluído com sucesso" in driver.page_source
