from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# enter the keyword for the video
keyword = input("Enter the keyword for the video: ")

# open the browser and go to YouTube
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

# search for the keyword
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)
search_box.send_keys(keyword)
search_box.submit()

# click on the first video
video = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a#video-title"))
)
video.click()

# # keep the browser open
input("Press Enter to close the browser...")
driver.quit()
