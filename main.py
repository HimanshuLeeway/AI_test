from selenium import webdriver

# create an instance of Edge driver
driver = webdriver.Edge()

# navigate to Google login page
driver.get("https://accounts.google.com/")

# start an infinite loop to keep the browser window open
while True:
    pass

