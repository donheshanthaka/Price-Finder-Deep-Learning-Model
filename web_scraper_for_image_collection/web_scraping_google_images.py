import bs4
import requests
from selenium import webdriver
import os
import time


#creating a directory to save images
folder_name = 'images'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

def download_image(url, folder_name, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
            file.write(reponse.content)


chromeDriverPath = "D:\Projects\Python\Web_Scraping_Selenium\chromedriver.exe"
driver = webdriver.Chrome(chromeDriverPath)

search_URL = "https://www.google.lk/search?q=suzuki+wagon+r+stingray+2018+japan&tbm=isch&ved=2ahUKEwjRhLj9uPX3AhVP_TgGHY1VAisQ2-cCegQIABAA&oq=suzuki+wagon+r+stingray+2018+japan&gs_lcp=CgNpbWcQAzIECAAQGDoECAAQQzoFCAAQgAQ6BAgAEB5Q2AZY8wxg3g5oAHAAeACAAawBiAHbB5IBAzAuN5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=KmaLYtHHHs_64-EPjauJ2AI&bih=937&biw=1920&hl=en"

driver.get(search_URL)

#//*[@id="islrg"]/div[1]/div[1]
#//*[@id="islrg"]/div[1]/div[50]
#//*[@id="islrg"]/div[1]/div[25]
#//*[@id="islrg"]/div[1]/div[75]
#//*[@id="islrg"]/div[1]/div[350]

a = input("Waiting for the user input to start: ")

# Scrolling the way up
driver.execute_script("window.scrollTo(0, 0);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, "html.parser")
containers = pageSoup.findAll("div", {"class":"isv-r PNCib MSM1fd BUooTd"})

len_containers = len(containers)
print("Found %s image containers" %(len_containers))


for i in range(1, len_containers+1):
    if i % 25 == 0:
        continue
    
    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)
    
    # Grabbing the URL of the small preview image
    previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
    previewImageElement = driver.find_element_by_xpath(previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")
    #print("preview URL", previewImageURL)

    # Clicking on the image container
    driver.find_element_by_xpath(xPath).click()


    # Starting a while True loop to wait until the URL inside the larger image view is different from the preview one
    timeStarted = time.time()

    while True:

        imageElement = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img""")
        imageURL= imageElement.get_attribute('src')


        if imageURL != previewImageURL:
            break

        else:
            #making a timeout if the full res image can't be loaded
            currentTime = time.time()

            if currentTime - timeStarted > 10:
                print("Timeout! Will download a lower resolution image and move onto the next one")
                break


    #Downloading image
    try:
        download_image(imageURL, folder_name, i)
        print("Downloaded element %s out of %s total. URL: %s" % (i, len_containers + 1, imageURL))
    except:
        print("Couldn't download an image %s, continuing downloading the next one"%(i))

    #//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img
    #//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img

driver.quit()

