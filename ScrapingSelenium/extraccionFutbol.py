from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#búsqueda de elementos en lista desplegable. No necesita el código, sino el texto
from selenium.webdriver.support.ui import Select

webSite = "https://www.adamchoi.co.uk/teamgoals/detailed"
path = "C:/Users/Berardi/Google Drive/Programación/Python/ScrapingSelenium"
driver = webdriver.Chrome()
driver.get(webSite)
WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
# .find_element trae el primer elemento que encuentra (en este caso no hay problema)
score_h_btn = driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]') 
score_h_btn.click()
dropdown_countries = Select(driver.find_element(By.ID,'country'))
dropdown_countries.select_by_visible_text("Argentina")
#elements (plural) para que no traiga solo el primero
lista_de_partidos = (driver.find_elements(By.TAG_NAME,'tr'))
for partido in lista_de_partidos:
    print (partido.text)