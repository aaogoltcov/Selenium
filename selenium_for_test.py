import time
from selenium import webdriver


def selenium(login, password):
    chrome_path = r'./venv/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get("https://passport.yandex.ru/auth/")
    search_login = driver.find_element_by_name("login")
    search_login.send_keys(login)
    search_login.submit()
    time.sleep(1)
    search_password = driver.find_element_by_id("passp-field-passwd")
    time.sleep(1)
    search_password.send_keys(password)
    search_password.submit()
    submit_button = driver.find_elements_by_tag_name("button")
    submit_button.submit()
    # driver.close()


if __name__ == '__main__':
    my_login = input('Login: ')
    my_password = input('Password: ')
    selenium(my_login, my_password)
