from pickle import NONE
from webbrowser import get
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

# # url = 'https://www.etf.com/modal_forms/nojs/login?destination=//'
# url = 'https://www.etf.com'
# browser = webdriver.Chrome('C:/chromedriver.exe')
# browser.get(url)
# # time.sleep(5)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'loginLnk')))
# print(browser.find_element_by_id('edit-name').text)


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# options.add_argument("proxy-server=localhost:8080")
driver = webdriver.Chrome('C:/chromedriver.exe', options=options)
# driver = webdriver.Chrome('C:/chromedriver.exe')

# url = 'https://www.etf.com/etfanalytics/etf-finder'
url = 'https://www.etf.com/modal_forms/nojs/login?destination=/'
# url = 'https://www.etf.com'
driver.get(url)
driver.maximize_window()
 
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table-tabs"]/li[7]')))
# element.send_keys(Keys.ENTER)

res = 0
while res < 1:
        try:
                element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "edit-name")))
                element.click()
                element.send_keys('hugguggu@gmail.com')

                element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "edit-pass")))
                element.click()
                element.send_keys('Rodroddl01!')

                element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "edit-submit")))
                element.click()
                
                res = 1
        except:
                res = 0

res = 0
while res < 1:
        try:

                div_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'main-navigation')))
                hover = ActionChains(driver).move_to_element(div_element)
                hover.perform()

                # driver.execute_script("window.scrollTo(0, Y)") 

                button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-navigation"]/ul/li[1]')))
                hover = ActionChains(driver).move_to_element(button)
                hover.perform()

                element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-navigation"]/ul/li[1]/ul/li[1]')))
                hover = ActionChains(driver).move_to_element(element).click()
                hover.perform()

                # time.sleep(3)

                div_element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'finder-root')))
                hover = ActionChains(driver).move_to_element(div_element)
                hover.perform()

                res = 1
        except:
                res = 0

res = 0
while res < 1:
        try:
                element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'results_display')))
                hover = ActionChains(driver).move_to_element(element)
                hover.perform()
                driver.execute_script("arguments[0].scrollIntoView(true);", element)

                # /html/body/div[7]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/section[2]/div[1]/div/div[3]/button
                element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="results_display"]/div/div[3]/button')))
                hover = ActionChains(driver).move_to_element(element).click()
                hover.perform()

                # time.sleep(3)
                div_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'table-tabs')))
                hover = ActionChains(driver).move_to_element(div_element)
                hover.perform()
                driver.execute_script("arguments[0].scrollIntoView(true);", div_element)

                # time.sleep(3)
                element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="table-tabs"]/li[7]')))
                hover = ActionChains(driver).move_to_element(element).click()
                hover.perform()
                # driver.execute_script("arguments[0].scrollIntoView(true);", element)
                
                # time.sleep(3)
                element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'more-btn')))
                hover = ActionChains(driver).move_to_element(element).click()
                hover.perform()
                res = 1
        except:
                res = 0
                print('retry\n')



# if driver.find_element_by_xpath('//input[@type="checkbox"]').get_attribute('checked'):  
#         driver.find_elements_by_class_name('uiInputLabelLabel')[-1].click()

div_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'finderCustomTabOptions')))
hover = ActionChains(driver).move_to_element(div_element)
hover.perform()

div_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finderCustomTabOptions"]/div[2]')))
hover = ActionChains(driver).move_to_element(div_element)
hover.perform()

value = driver.find_elements(By.CLASS_NAME, 'form-check')
print(len(value))
# /html/body/div[7]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/div[2]/div/section/div[2]/div[1]/span/label/input

for idx in range (1, 59, 1):
        element = driver.find_element(By.XPATH, f'//*[@id="finderCustomTabOptions"]/div[2]/div[{idx}]/span/label')
        checked = driver.find_element(By.XPATH, f'//*[@id="finderCustomTabOptions"]/div[2]/div[{idx}]/span/label/input')
        if checked.get_attribute('checked') :
                print( ' checked')        
        else:
                # //*[@id="finderCustomTabOptions"]/div[2]/div[1]/span/label
                # div_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finderCustomTabOptions"]/div[2]/div[4]/span/label')))
                hover = ActionChains(driver).move_to_element(element).click()
                hover.perform()
                print(' change')        



div_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finderCustomTabOptions"]/div[3]')))
hover = ActionChains(driver).move_to_element(div_element)
hover.perform()

div_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finderCustomTabOptions"]/div[3]/button[2]')))
hover = ActionChains(driver).move_to_element(div_element).click()
hover.perform()


element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'finderTable')))
tbody = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'tbody')))
rows = tbody.find_elements(By.TAG_NAME, 'tr')

# for index, value in enumerate(rows):
#     body=value.find_elements_by_tag_name("td")[1]
#     print(body.text)

# 엑셀 파일 생성
workbook = openpyxl.Workbook()

# 엑셀 워크시트 생성
# sheet = workbook.create_sheet("test")
sheet = workbook.worksheets[0]

for row_idx, row_val in enumerate(rows):
        col = row_val.find_elements_by_tag_name("td")
        # print(len(body))
        for td_idx, col_val in enumerate(col):
                # print(col_val.text, end=" ")
                sheet.cell(row = row_idx + 1, column = td_idx + 1).value = col_val.text
        # print("")
        
workbook.save(r'etf_com.xlsx')

driver.quit()

