# -*- coding: utf-8 -*-
import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def  test_promo(argv):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "http://staging.fever38.com/"
    driver.get(base_url)
    driver.find_element_by_css_selector("b.fb-login").click()

    driver.switch_to_window(driver.window_handles[-1])
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("email"))

    #登陸
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(argv[0])
    driver.find_element_by_id("pass").clear()
    driver.find_element_by_id("pass").send_keys(argv[1])
    driver.find_element_by_id("persist_box").click()
    driver.find_element_by_id("u_0_1").click()
    driver.switch_to_window(driver.window_handles[0])

    driver.get(base_url)
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//ul[@id='j-daThumbs']/li[2]/h4"))

    driver.find_element_by_xpath("//ul[@id='j-daThumbs']/li[2]/h4").click()
    driver.find_element_by_xpath("//ul[@id='j-pinterest']/li[2]/i").click()
    driver.find_element_by_xpath("//ul[@id='j-pinterest']/li[2]/a[1]").click()
    time.sleep(5)
    #切換到活動頁面點讚
    driver.switch_to_window(driver.window_handles[-1])
    driver.switch_to_frame(1)
    driver.find_element_by_class_name("pluginConnectButton").click()

    #回到主頁面 點設計對白.
    driver.switch_to_window(driver.window_handles[-1])
    driver.find_element_by_css_selector(".button>.j-chkId").click()
    driver.find_element_by_css_selector(".j-design>.tip").click()
    driver.find_element_by_id("j-dialogMsg").send_keys(argv[2])
    driver.find_element_by_id("j-draw").click()

    driver.find_element_by_css_selector(".wt>.check-bg").click()
    driver.find_element_by_css_selector(".button>.j-send").click()
    # driver.quit()

if __name__ == "__main__":
    test_promo(sys.argv[1:])
