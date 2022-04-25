from selenium import webdriver
import time

#Precio del Bitcoin con Web Scraping (Python y Selenium)

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.ef.com.mx/blog/language/10-cosas-para-comer-en-japon/")



Onigiri = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/article/div[3]/h3[7]')

print('La comida seleccionada es: '+ Onigiri.text)

driver.quit()
