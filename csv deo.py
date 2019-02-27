## CSV library

import csv


with open ("C:\\Users\\gvernekar\\Downloads\\Python_Examples\\datasets\\employees.csv") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print (line)