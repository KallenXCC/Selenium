import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r"C:\Program Files (x86)\chromedriver.exe"

class TrelliswareMenuTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service = Service(PATH)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://www.trellisware.com/")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_about_us_menu(self):
        driver = self.driver
        about_us_menu = driver.find_element(By.ID, "mega-menu-item-6632")

        ActionChains(driver).move_to_element(about_us_menu).perform()

        submenu_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#mega-menu-item-6632 .mega-sub-menu a"))
        )
        self.assertGreater(len(submenu_links), 0, "No submenu links found under 'About Us'")

        for link in submenu_links:
            with self.subTest(link=link.text):
                self.assertIn("https://www.trellisware.com/", link.get_attribute("href"),
                              f"Unexpected link: {link.get_attribute('href')}")

    def test_products_menu(self):
        driver = self.driver
        products_menu = driver.find_element(By.ID, "mega-menu-item-6633")

        ActionChains(driver).move_to_element(products_menu).perform()

        submenu_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#mega-menu-item-6633 .mega-sub-menu a"))
        )
        self.assertGreater(len(submenu_links), 0, "No submenu links found under 'Products'")

        for link in submenu_links:
            with self.subTest(link=link.text):
                self.assertTrue(link.get_attribute("href").startswith("https://www.trellisware.com/"),
                                f"Unexpected link: {link.get_attribute('href')}")


if __name__ == "__main__":
    unittest.main()
