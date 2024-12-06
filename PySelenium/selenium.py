from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")


signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box = send_keys("username")

password_box = browser.find_element_by_id("password")
password_box.send_keys("thisPassword")
password_box.submit()

assert "thisPassword" in browser.page_source

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "thispassword" in link_label

browser.quit()

#https://developer.chrome.com/docs/chromedriver/downloads#chromedriver_1140573590