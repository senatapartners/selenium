from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

chrome_service = Service(
    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
)


chrome_options = Options()
options = [
    "--headless=new",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)


driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://nytimes.com")
print(driver.title)

driver.quit()
