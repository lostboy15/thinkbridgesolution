import csv
def get_company_list(file_name):
    fields = []
    rows = []
    with open(file_name,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            if row != []:
                rows.append(row[0])
    return rows

def create_company_link_csv(file_name,details):
    fields = ['company_name','company_url']
    with open(file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(details)

def get_company_link(file_name):
    fields = []
    rows = []
    with open(file_name,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            if row != []:
                rows.append(row[1])
    return rows

def create_company_emp(details):
    fields = ['company_name','company_employess']
    file_name = 'company.csv'  # give path of original file
    names = get_company_list('company.csv')   # give path of original file
    emp = []
    for rows in details:
        e = rows[1]
        e = e.replace(' employees','')
        emp.append(e)
    main_dict = [list(x) for x in zip(names, emp)]
    with open(file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(main_dict)