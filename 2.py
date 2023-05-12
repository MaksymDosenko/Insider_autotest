from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://useinsider.com/"
browser = webdriver.Chrome()
browser.get (link)
if browser.current_url == 'https://useinsider.com/':
    print('Web page opened successfully!')
else:
    print('Failed to open the web page.')

time.sleep(0.7)
cookies_accept=browser.find_element(By.ID, "wt-cli-accept-all-btn").click()
more_button_dropdownbox = browser.find_element (By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[6]/a" ).click()
careers_button = browser.find_element(By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[6]/div/div[1]/div[3]/div/a").click()
time.sleep(0.5)
career_page= browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section")
cs_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section/div/div/div[2]/div[1]/div[2]/a/h3")
sales_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section/div/div/div[2]/div[2]/div[2]/a/h3")
pe_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section/div/div/div[2]/div[3]/div[2]/a/h3")
location_field = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/section[3]/div/div/div/div/div/div/div/section")
life_description = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/section[4]")
print(career_page.is_displayed())
print(cs_button.is_displayed())
print(cs_button.is_enabled())
print(sales_button.is_displayed())
print(sales_button.is_enabled())
print(pe_button.is_displayed())
print(pe_button.is_enabled())
print(location_field.is_displayed())
print(life_description.is_displayed())
see_all_button=browser.find_element(By.XPATH, "//section[@id='career-find-our-calling']//a[contains(text(),'See all teams')]").click()
qa_jobs=browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section/div/div/div[2]/div[12]/div[2]/a").click()
see_all_qa_job=browser.find_element(By.CSS_SELECTOR, "a[class*=btn-outline-secondary]").click()
browser.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/form/div[1]/select/option[2]").click()
browser.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/form/div[2]/select/option[16]").click()
position_qa= browser.find_element(By. CSS_SELECTOR, "p[class*=position-title]")
department_qa = browser.find_element(By.CSS_SELECTOR, "span[class*= position-department]")
location_qa = browser.find_element(By.CSS_SELECTOR, "div[class*= position-location]")
apply_now = browser.find_element(By.LINK_TEXT, "Apply Now")
print(positon_qa.is_displayed())
print(department_qa.is_displayed())
print(location_qa.is_displayed())
print(apply_now.is_displayed())
apply_now = browser.find_element(By.LINK_TEXT, "Apply Now").click()









