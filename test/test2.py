from selenium import webdriver


options = webdriver.FirefoxOptions()
options.add_argument('-headless')
 
browser = webdriver.Firefox(options=options)
file1 = open('tvsm.txt', 'r') 

Lines = file1.readlines()

lamp = list(map(lambda x:x.strip(),Lines))

print(lamp)

for i in range(0, len(lamp)):
  
  
    domanin_name = str(lamp[i])
    print(domanin_name)
    url = "https://www.sslshopper.com/ssl-checker.html#hostname=https://dailin.tvsmotor.com/"
    browser.get(url)
    
    results = browser.find_elements_by_class_name('checker_messages')
    
    print(len(results))
    print(type(results))
 

 
browser.quit()