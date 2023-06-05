from selenium import webdriver
import time
import csv

website = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
driver = webdriver.Chrome()
driver.get(website)
time.sleep(3)
SLN = ['Serial No.',1,2,3,4,5]
EVN = ['Est. Value Notes']
Desc =['Description']
CD = ['Closing Date']

def add_to_list():
    EVN.append(driver.find_element("xpath" ,'//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]').text)
    CD.append(driver.find_element("xpath" ,'//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]').text)
    Desc.append(driver.find_element("xpath" ,'//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]').text)


var = driver.find_element("xpath" , '//*[@id="table_id"]/tbody/tr[1]/td[2]/a/b')
var.click()
time.sleep(2)
add_to_list()
time.sleep(1)

for i in range(4):
    var2 = driver.find_element("xpath" ,'//*[@id="id_prevnext_next"]')
    var2.click()
    time.sleep(2)
    add_to_list()
    time.sleep(1)
    
print(EVN,Desc,CD)

rows = zip(SLN,EVN,Desc,CD)
with open('File.csv', "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

driver.quit()
