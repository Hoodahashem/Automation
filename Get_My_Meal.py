from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import date, timedelta
personal_id = your_id
personal_password = your_password
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get('https://alzahraa.mans.edu.eg/studentLogin')

driver.implicitly_wait(5)

username = driver.find_element(By.NAME, "txtStudentID")
username.send_keys(f"{personal_id}")

password = driver.find_element(By.NAME, "txtStudentPassword")
password.send_keys(f'{personal_password}')

button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.account-btn")
button.click()

div1 = driver.find_element(By.CSS_SELECTOR, 'div.sidebar-inner')
div2 = div1.find_element(By.ID, "sidebar-menu")
ul = div2.find_element(By.CSS_SELECTOR, 'ul')

getmeal = ul.find_element(By.ID, 'getMeals')

driver.execute_script("arguments[0].click();", getmeal)

date_of_today = date.today()

date_of_next_day = date_of_today + timedelta(days=1)

meal_of_to = driver.find_element(By.CSS_SELECTOR, f'td[data-date="{date_of_next_day}"]')

check_box = meal_of_to.find_element(By.CSS_SELECTOR, 'input[name="chkMeals"]')
check_box.click()

save_button = driver.find_element(By.XPATH, '//*[@id="divMealsCalendar"]/div[1]/div[1]/button')
save_button.click()

driver.quit()
