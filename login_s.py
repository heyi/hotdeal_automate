import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def  test_login(argv):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "http://staging.fever38.com/"
    driver.get(base_url + "/")
    driver.find_element_by_css_selector("b.fb-login").click()

    driver.switch_to_window(driver.window_handles[-1])
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("email"))

    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(argv[0])
    driver.find_element_by_id("pass").clear()
    driver.find_element_by_id("pass").send_keys(argv[1])
    driver.find_element_by_id("persist_box").click()
    driver.find_element_by_id("u_0_1").click()
    driver.switch_to_window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//ul[@id='j-daThumbs']/li[2]/h4"))
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    test_login(sys.argv[1:])
