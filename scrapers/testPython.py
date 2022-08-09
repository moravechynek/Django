import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io
import urllib.request

def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        if file_name.split('.')[1] == 'jpg':
            with open(file_path, 'wb') as f:
                image.save(f, 'JPEG')
        elif file_name.split('.')[1] == 'gif':
            with open(file_path, 'wb') as f:
                image.save(f, 'GIF')
        elif file_name.split('.')[1] == 'png':
            with open(file_path, 'wb') as f:
                image.save(f, 'PNG')

        print('Success\n')

    except Exception as e:
        print('ERROR FOUND')

driver = webdriver.Chrome()
driver.implicitly_wait(0.1)
driver.get('https://etesty2.mdcr.cz/Test/TestPractise/15')
html = driver.page_source
f = open('etesty.csv', 'w')
i = 0
images_urls = []
videos = []

# The first line of .csv
f.write('question;image;a;b;c;correct\n')
f.close()

# Clicking the sort button
sort = driver.find_element(By.XPATH, '//*[@id="sortRandomButtonID"]')
sort.click()

# Getting the data
while i in range(1): #959
    try:
        question_ID = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "questionNumberID"))
        )
    except:
        driver.quit()
    
    # QUESTION
    question = driver.find_elements(By.CLASS_NAME, 'question-text')[0].text
    if driver.find_elements(By.CLASS_NAME, 'question-text')[0].text == '':
        question = driver.find_elements(By.CLASS_NAME, 'question-text')[1].text
    
    # CLICK CORRECT
    a = driver.find_element(By.XPATH, '//*[@id="questionContentID"]/div[2]/div[1]/p')
    a.click()
    next = driver.find_element(By.XPATH, '//*[@id="nextButtonID"]')
    next.click()
    
    
    
    ids = driver.find_elements(By.XPATH, '//*[@data-answerid]')
    a_id = ids[0].get_attribute('data-answerid')
    b_id = ids[1].get_attribute('data-answerid')
    c_id = ids[2].get_attribute('data-answerid')

    print(a_id)
    print(b_id)
    print(c_id)

    next.click()

    i += 1

driver.quit()