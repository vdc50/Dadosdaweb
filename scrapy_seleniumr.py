from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

symbol = "PERP-USD"
url = f"https://finance.yahoo.com/quote/{symbol}/history?p={symbol}"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
price_element3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//table/tbody | //table[@tr.span]')))
data = price_element3.text
driver.quit()

# Separe as linhas da saída
lines = data.strip().split("\n")
# Crie uma lista de dicionários para armazenar os dados
rows = []
for line in lines:
    parts = line.split()
    row = {
        "date": parts[0] + " " + parts[1],
        "ano": parts[2],
        "Open": parts[3],
        "High": parts[4],
        "Low": parts[5],
        "Close": parts[6],
        "AdjC": parts[7],
        "Vol" : parts[8]}
    rows.append(row)
# Crie um dataframe a partir dos dados
df = pd.DataFrame(rows)

print(df)