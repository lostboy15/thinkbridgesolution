from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from csv_helper import get_company_list,create_company_link_csv

options = webdriver.ChromeOptions()
options.add_argument("headless")

exe_path = ChromeDriverManager().install()
service = Service(exe_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.linkedin.com/login")
sleep(6)

linkedin_username = "#Linkedin Mail I'd"
linkedin_password = "#Linkedin Password"

driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[\
							1]/input").send_keys(linkedin_username)
driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[\
							2]/input").send_keys(linkedin_password)
sleep(3)
driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[\
							3]/button").click()

company_list = get_company_list('company.csv') #path of original file




def get_dict(company_name):
	company_url = []
	driver.get('https://www.linkedin.com/search/results/all/?keywords='+company_name)
	sleep(5)
	links = driver.find_element(By.XPATH,"//a[@class='app-aware-link  search-nec__hero-kcard-v2-link-wrapper link-without-hover-state link-without-visited-state t-normal t-black--light']")
	company_url.append(company_name)
	company_url.append(links.get_attribute('href'))
	return company_url
	sleep(5)

main_dict = []

for company_name in company_list:
	temp = get_dict(company_name)
	# print(temp)
	main_dict.append(temp)


# print(main_dict)
create_company_link_csv('company_links.csv',main_dict)  #path of links file
      
driver.close()
