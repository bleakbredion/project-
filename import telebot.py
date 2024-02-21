from datetime import datetime
 
datenow = str(datetime.now()).split()[0].split("-")
date1 = datetime.strptime('11/27/2023', '%m/%d/%Y')
date2 = datetime.strptime('11/20/2023', '%m/%d/%Y')
num_days = (date2 - date1).days
print(abs(num_days))