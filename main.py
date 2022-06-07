from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def find(driver):
    list_of_names = f"//b[contains(text(),'{dictionary[i]['name'][0]}')]"
    choice = driver.find_element(By.XPATH, list_of_names)
    if choice:
        return choice
    else:
        return False


chrome_driver_path = "C:/Users/agnie/Developer/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


money = driver.find_element(By.ID, "money")
help_list_money = []
help_name = []
help = driver.find_elements(By.CSS_SELECTOR, 'div[id="rightPanel"] b')
for i in help:
    i = i.text.split(" ")
    help_list_money.append(i[-1])
    help_name.append(i[0:1])

help_list_money.remove(help_list_money[-1])
right_panel_money = []

for i in help_list_money:
    i = i.replace(",", "")
    i = int(i)
    right_panel_money.append(i)


dictionary = {}
for i in range(len(help)-1):
    dictionary[i] = {
        "name": help_name[i],
        "money": right_panel_money[i]
    }

total_time = time.time()

on_game = True
while on_game:
    driver.find_element(By.XPATH, '//*[@id="cookie"]').click()
    if total_time % 5:
        for i in dictionary:
            if int(money.text.replace(",", "")) >= int(dictionary[i]["money"]):
                # try:
                element = WebDriverWait(driver, 3).until(find).click()
                time.sleep(1)
                money = driver.find_element(By.ID, "money")
                help_list_money = []
                help_name = []
                help = driver.find_elements(By.CSS_SELECTOR, 'div[id="rightPanel"] b')
                for i in help:
                    i = i.text.split(" ")
                    help_list_money.append(i[-1])
                    help_name.append(i[0:1])

                help_list_money.remove(help_list_money[-1])
                right_panel_money = []

                for i in help_list_money:
                    i = i.replace(",", "")
                    i = int(i)
                    right_panel_money.append(i)
                dictionary = {}
                for i in range(len(help) - 1):
                    dictionary[i] = {
                        "name": help_name[i],
                        "money": right_panel_money[i]
                    }
                break
