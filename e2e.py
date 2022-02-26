# e2e - Lior A

import Utils
from Utils import SCORES_FILE_NAME
from selenium import webdriver
from time import sleep

def test_scores_service(url):
    driver = webdriver.Chrome(executable_path="C:/Users/ASSIS/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get(f'{url}')
    driver.maximize_window()
    score_data = driver.find_element_by_xpath('/html[1]/body[1]/h1[1]/div[1]').text
    print(f'The Score is: {score_data}')
    try:
        if 0 < int(score_data) < 1001:
            return True
        else:
            return False
    except:
        print('Scores Value is not legal')
        return False


def main_function(input):
    if input:
        print("Number is between 1 to 1000")
        exit(0)
    else:
        print("Number is out of range [1:1000]")
        exit(Utils.BAD_RETURN_CODE)

test = test_scores_service("http://127.0.0.1:8777")
main_function(test)