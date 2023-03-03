import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://github.com/")
driver.maximize_window()
#driver.implicitly_wait(4)
driver.find_element(By.XPATH, '(//a[@class="HeaderMenu-link HeaderMenu-link--sign-in flex-shrink-0 no-underline d-block d-lg-inline-block border border-lg-0 rounded rounded-lg-0 p-2 p-lg-0"])[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//input[@name="login"]').send_keys("AhmedGG22")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("Ep00330801")
driver.find_element(By.XPATH,'//input[@name="commit"]').click()
time.sleep(2)
#driver.find_element(By.LINK_TEXT,"AhmedGG22/Localisateurs-Web").click()
driver.find_element(By.XPATH,"(//a[@href='/AhmedGG22/Localisateurs-Web'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//summary[@class='btn css-truncate']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@href='https://github.com/AhmedGG22/Localisateurs-Web/tree/master']").click()
time.sleep(2)

#ouvrir la fichier Tp_automatisation1.py
driver.find_element(By.XPATH,"//a[@href='/AhmedGG22/Localisateurs-Web/blob/master/TP_automatisation1.py']").click()
time.sleep(2)
driver.back()
#ouvrir la fichier index.html
driver.find_element(By.XPATH,"//a[@href='/AhmedGG22/Localisateurs-Web/blob/master/index.html']").click()
time.sleep(4)
driver.back()
#ouvrir la fichier scripts.js
driver.find_element(By.XPATH,"//a[@href='/AhmedGG22/Localisateurs-Web/blob/master/scripts.js']").click()
time.sleep(4)
driver.back()
#ouvrir la fichier styles.css
driver.find_element(By.XPATH,"//a[@href='/AhmedGG22/Localisateurs-Web/blob/master/styles.css']").click()
time.sleep(4)
driver.quit()