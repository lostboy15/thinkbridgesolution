# thinkbridgesolution
Solution of thinkbridge assignment

This repo contains program to fetch linkedin url of companies that are present and a csv file then writes url in different file. After getting url it fetches employee count of respective companies and store it in same csv. It uses selenium to scrape from web. Provide linkedin user details for login and path of csv mentioned in comments.

Folder structure:
  count : emp_count.py # get employee count of company from linkedin url 
  urls : get_url.py # get linkedin url of company 
         csv_helper  # read and write from csv files

run python get_url.py 
run python emp_count.py
        
