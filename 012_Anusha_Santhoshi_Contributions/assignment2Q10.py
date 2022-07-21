import csv 
Details = ['Name', 'class', 'passoutYear', 'subject']  
rows = [ ['Anusha', '2nd', '2023', 'Computers'],  ['Sai', '3rd', '2022', 'Electonics'],  ['Ram', '4th', '2021', 'Mechanical']] 
with open('Assignment_2_2.13.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(Details) 
    write.writerows(rows) 