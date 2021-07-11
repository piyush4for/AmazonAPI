from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('F:\windows tools\chromedriver')
browser.get('https://www.amazon.in/Apple-Watch-Smart-Space-Aluminum/dp/B075R9P7H8/ref=sr_1_3?dchild=1&keywords=apple&qid=1626029435&sr=8-3')

# result_list = browser.find_elements_by_class_name('s-result-item')
# links = []
#             #find div box
# results = result_list[0].find_elements_by_xpath(
# "//div[1]/div/div[1]/div/span[3]/div[2]/div[3]")
# #send href link of all div box to links[] 
# links = [link.get_attribute('href') for link in results]

# price = browser.find_element_by_id('priceblock_ourprice').text
# price = price.split('₹')[1]
# price = price.split(",")[0] + price.split(",")[1]
# print(f"{price}{len(price)}")
# browser.close()
image = browser.find_elements_by_xpath('//*[@id="landingImage"]')
for i in image:
    print(i.get_attribute('src'))
    
browser.close()

