from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')


YourName = input("Enter Your Name: ")
link = input("Enter Link: ")

total_question = 15

driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)
driver.get(link)

print("------Opening Link-------")

sleep(2)

print("-----Entering Your Name------")

driver.find_element(By.ID,"name").send_keys(YourName)
driver.find_element(By.ID,"name").send_keys(Keys.RETURN)

print("------Loading---------")

sleep(2)

print("------Loaded------ \n")

for i in range(0,total_question):
    try:
        unanswerd_question = driver.find_element(By.CLASS_NAME,"question.unanswered")
        correct_answer = unanswerd_question.find_element(By.CLASS_NAME,"answer.correct").click()
        print(str(i + 1) + ") Question Done")
        sleep(1.5)
    except:
        print("Answer Not Found!")
sleep(2)
driver.close()
print("Submitted!")


