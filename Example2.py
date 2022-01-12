

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

#driver = webdriver.Chrome(executable_path='/Users/andrejandrus/webdriver/chromedriver')
#link = "http://suninjuly.github.io/find_link_text.html"


try:
    browser = webdriver.Chrome(executable_path='/Users/andrejandrus/webdriver/chromedriver')
    browser.get("https://suninjuly.github.io/execute_script.html")
    #time.sleep(2)

    #browser.find_element(By.ID, 'robotCheckbox').click()
    #browser.find_element(By.ID, 'robotsRule').click()
    #browser.find_element(By.XPATH, '//div[1]/div[3]/input').send_keys("email")

    x = int(browser.find_element(By.ID, 'input_value').text)
    #x2 = int(browser.find_element(By.ID, 'num2').text)
    y = math.log(abs(12*math.sin(x)))
    #y = x1 + x2
    #print(y)
    #answer = Select(browser.find_element(By.ID, 'dropdown'))
    #answer.select_by_visible_text(str(y))
    browser.find_element(By.ID, 'answer').send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    button.click()
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(1)

    # находим элемент, содержащий текст
    #elcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла



# не забываем оставить пустую строку в конце файла

