from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://flutter.dev/")
    cta_button = driver.find_element_by_class_name("site-header__cta")
    cta_button.click()
    install_button = driver.find_element_by_id("install-macos")
    install_button.click()
    element = driver.find_element_by_id("create-and-run-a-simple-flutter-app")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()


if __name__ == "__main__":
    main()