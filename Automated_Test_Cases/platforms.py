import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.configs import loginPassword, loginEmail, screenshotFolder, filePathToTestcases
from shared_files import xlsUtils
from shared_files.login_module import Login
from Config import configs
from selenium.webdriver.chrome.options import Options

# Initialize WebDriver
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

sheetname = "login"
Platfortestcase = "MSQA_Admin_platformModule.xlsx"
filePath = (f"{filePathToTestcases}{Platfortestcase}")
# Open the webpage
url = configs.urlToAdminPOrtal
driver.get(url)

# Perform login
login_page = Login(driver)
login_page.login(loginEmail, loginPassword)

# Wait for the "Platforms" title element to be visible
platform_title_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//span[@title="Platforms"]'))
)
platform_title_element.click()
# Get the text of the platform title
platform_title = platform_title_element.text
print("Platform Title:", platform_title)
time.sleep(5)
platformScreenshot_name = "platformScreenshotlandingpg.png"
driver.save_screenshot(f"{screenshotFolder}{platformScreenshot_name}")
# show Email #
checkbox_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.MuiCheckbox-root')))
checkbox_element.click()
time.sleep(3)
# screenshot to show email
showEmailScreenshot_name = "showEmailPlatformScreenshot.png"
driver.save_screenshot(f"{screenshotFolder}{showEmailScreenshot_name}")
xlsUtils.writeData(filePath, sheetname,2 , 8, "Assert this by looking at the screenshot")
xlsUtils.writeData(filePath, sheetname,2 , 9, "PENDING")

# add new platform
add_platform_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'btn_platform_add_new_platform')))
add_platform_button.click()
xlsUtils.writeData(filePath, sheetname,3 , 8, "Add new was successful")
xlsUtils.writeData(filePath, sheetname,3 , 9, "PASS")
# upload image
upload_button = driver.find_element(By.ID, "btn_platforms_modal_upload_new_image")
Testimage = "testimage.png"
imagepath= f"{screenshotFolder}{Testimage}"
upload_button.send_keys(imagepath)
time.sleep(2)
xlsUtils.writeData(filePath, sheetname,4 , 8, "Image was added successful,assert with screenshots")
xlsUtils.writeData(filePath, sheetname,4 , 9, "PASS")
# screenshot to show uploaded picture
uploadedpictureScreenshot_name = "uploadedpictureScreenshotplatformpg.png"
driver.save_screenshot(f"{screenshotFolder}{uploadedpictureScreenshot_name}")
time.sleep(1)
# input name
inputPlatformname = driver.find_element(By.ID, "input_platforms_modal_name")
name_to_input = xlsUtils.readDAta(filePath, sheetname,5,5)
inputPlatformname.send_keys(name_to_input)
xlsUtils.writeData(filePath, sheetname,5 , 8, "name inserted successfully")
xlsUtils.writeData(filePath, sheetname,5 , 9, "PASS")
time.sleep(1)
# input url
inputPlatformURL = driver.find_element(By.ID, "input_platforms_modal_url")
URL_to_input = xlsUtils.readDAta(filePath, sheetname,6,5)
inputPlatformURL.send_keys(URL_to_input)
xlsUtils.writeData(filePath, sheetname,6 , 8, "URL_ inserted successfully")
xlsUtils.writeData(filePath, sheetname,6 , 9, "PASS")
time.sleep(1)
# select token
select_tokens_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,"text-slate-900")))
select_tokens_dropdown.click()
time.sleep(3)

# check token
#selecttoken = driver.find_element(By.ID,"CheckBoxOutlineBlankIcon")
test_2_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.MuiListItemText-primary.css-yb0lig")))
test_2_element.click()
time.sleep(3)
xlsUtils.writeData(filePath, sheetname,7 , 8, "successfully selected the token")
xlsUtils.writeData(filePath, sheetname,7 , 9, "PASS")
# click save on the selected token
saveSelection_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//em[contains(text(), 'Save')]")))
saveSelection_button.click()
time.sleep(3)
xlsUtils.writeData(filePath, sheetname,8 , 8, "Save successfully")
xlsUtils.writeData(filePath, sheetname,8 , 9, "PASS")
# click submit
driver.find_element(By.ID, "btn_add_platforms_modal_submit").click()
xlsUtils.writeData(filePath, sheetname,9 , 8, "Submitted successfully")
xlsUtils.writeData(filePath, sheetname,9 , 9, "PASS")
time.sleep(2)
# search for the added record
search_button = driver.find_element(By.ID,"input_platforms_page_search_table")
search_button.send_keys(name_to_input)
time.sleep(5)
# screenshot the records
SearchScreenshot_platform = "searchScreenshot.png"
driver.save_screenshot(f"{screenshotFolder}{SearchScreenshot_platform}")