# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Practical1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\tushar\Desktop\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_practical1(self):
        driver = self.driver
        driver.get(
            "https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html?myPhoto=09+Students+app.pptx")
        time.sleep(5)
        self.assertIn("media",driver.current_url)
        el=driver.find_element_by_id("uploadImage")
        time.sleep(5)
        el.send_keys(r"C:\Users\tushar\Desktop\practicalexam\test.png")
        time.sleep(3)
        self.assertEquals("You must select valid image file!",self.close_alert_and_get_its_text())
        driver.save_screenshot(r"C:\Users\tushar\Desktop\practicalexam\file.png")
        time.sleep(5)
        driver.find_element_by_xpath("//input[@value='send']")



    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
