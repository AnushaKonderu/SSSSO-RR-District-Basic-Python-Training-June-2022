import csv
mydelimeter = csv.excel()
mydelimeter.delimiter=";"
myfile = open("C:/Users/test/Documents/R_projects/homework/rdu-weather-history.csv")
myfile.readline()
myreader=csv.reader(myfile,mydelimeter)
mywind,mydate=[],[]
minTemp, maxTemp = [],[]

for row in myreader:
    print(row[1],row[2])
    minTemp.append(row[1])
    maxTemp.append(row[2])
print ("min value element : ", min(minTemp))
print ("max value element : ", min(maxTemp))