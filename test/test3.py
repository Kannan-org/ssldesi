from selenium import webdriver


options = webdriver.FirefoxOptions()
options.add_argument('-headless')
 
browser = webdriver.Firefox(options=options)

url1 = "https://www.sslshopper.com/ssl-checker.html#hostname=https://dailin.tvsmotor.com/"
url2 = "https://www.sslshopper.com/ssl-checker.html#hostname=https://elearning.tvsmotor.com/"
a = browser.get(url1)
b = browser.get(url2)

# results1 = a.find_elements_by_class_name('checker_messages')
results2 = b.find_elements_by_class_name('checker_messages')
print("------------------------result1 -------------------------")
print(len(results1))
print(type(results1))
print("------------------------result2 -------------------------")
print(len(results1))
print(type(results1))
 

 
browser.quit()