import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io

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

        print('Success\n')

    except Exception as e:
        print('ERROR FOUND')

driver = webdriver.Chrome()
driver.get('https://etesty2.mdcr.cz/Test/TestPractise/15')
html = driver.page_source
f = open('etesty2.csv', 'w')
i = 0
images_urls = []

# The first line of .csv
f.write('question;a;b;c;correct;image\n')
f.close()

# Clicking the sort button
sort = driver.find_element(By.XPATH, '//*[@id="sortRandomButtonID"]')
sort.click()

# Getting the data
while i in range(928): #928
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
    
    # ANSWERES
    a = driver.find_element(By.XPATH, '//*[@id="questionContentID"]/div[2]/div[1]/p')
    b = driver.find_element(By.XPATH, '//*[@id="questionContentID"]/div[2]/div[2]/p').text
    answers_container = driver.find_elements(By.XPATH, '//*[@id="questionContentID"]/div[2]/*')
    # print('Container length ' + str(len(answers_container)))
    if len(answers_container) == 3:
        c = driver.find_element(By.XPATH, '//*[@id="questionContentID"]/div[2]/div[3]/p').text
    elif len(answers_container) == 2:
        c = 'none'
    else: print('Some error')
    
    # IMAGE
    try:
        image_path = driver.find_element(By.XPATH, '//*[@id="questionContentID"]/div[1]/img').get_attribute('src')
        image_alt = driver.find_element(By.XPATH, '//*[@id="questionContentID"]/div[1]/img').get_attribute('alt').split('.')
        image_format = image_alt[1]
        images_urls.append([image_path, str(i+1) + '.' + image_format])

    except Exception as e:
        print('')
    
    # CORRECT
    a.click()
    next = driver.find_element(By.XPATH, '//*[@id="nextButtonID"]')
    next.click()
    
    correct_answer = driver.find_element(By.XPATH, '//*[@id="questionContentID"]/div[2]/div[contains(concat(" ", @class, " "), " correct ")]/p').text
    correct = ''
    if correct_answer == a.text: correct = 'a'
    elif correct_answer == b: correct = 'b'
    elif correct_answer == c: correct = 'c'
    
    if i < 9:
        question_num = question_ID.text[-1]
    elif i < 99:
        question_num = question_ID.text[-2:]
    else: question_num = question_ID.text[-3:]
    

    f = open('etesty2.csv', 'a')
    f.write(question + ';' + a.text + ';' + b + ';' + c + ';' + correct + '\n')
    f.close()
    print(question_num)
    print(question)
    print('A       ' + a.text)
    print('B       ' + b)
    print('C       ' + c)
    print('Correct ' + correct)
    print()
    
    next.click()

    i += 1

for url in images_urls:
    download_image('./img/', url[0], url[1])

driver.quit()