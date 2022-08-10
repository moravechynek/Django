import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def topic(count,topic,https):
    i = 0
    driver.get(https)
    while i in range(count):
        try:
            question_ID = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "questionNumberID"))
            )
        except:
            driver.quit()
        
        # CLICK CORRECT
        a = driver.find_element(By.XPATH, '//*[@id="questionContentID"]/div[2]/div[1]/p')
        a.click()
        next = driver.find_element(By.XPATH, '//*[@id="nextButtonID"]')
        next.click()

        ids = driver.find_elements(By.XPATH, '//*[@data-answerid]')
        a_id = ids[0].get_attribute('data-answerid')

        f = open('topics.csv', 'a')
        f.write(a_id + ';' + topic + '\n')
        f.close()
        
        next.click()

        i += 1

driver = webdriver.Chrome()
driver.implicitly_wait(0.1)

html = driver.page_source
f = open('topics.csv', 'w')

# The first line of .csv
f.write('a_id;topic\n')
f.close()

topic(119,'Pojmy','https://etesty2.mdcr.cz/Test/TestPractise/24')
topic(152,'Jizda','https://etesty2.mdcr.cz/Test/TestPractise/16')
topic(116,'Ostatni','https://etesty2.mdcr.cz/Test/TestPractise/25')
topic(202,'Znacky','https://etesty2.mdcr.cz/Test/TestPractise/14')
topic(87,'Situace','https://etesty2.mdcr.cz/Test/TestPractise/17')
topic(60,'BezpecnostA','https://etesty2.mdcr.cz/Test/TestPractise/23')
topic(59,'BezpecnostB','https://etesty2.mdcr.cz/Test/TestPractise/19')
topic(86,'BezpecnostCD','https://etesty2.mdcr.cz/Test/TestPractise/18')
topic(23,'Predpisy','https://etesty2.mdcr.cz/Test/TestPractise/21')
topic(37,'Provoz','https://etesty2.mdcr.cz/Test/TestPractise/22')
topic(35,'Zdravi','https://etesty2.mdcr.cz/Test/TestPractise/20')

driver.quit()