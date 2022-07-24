# Python program to illustrate the
# conversion of unix timestamp string
# to its readable date
 
# Importing datetime module
import datetime
 
# Calling the fromtimestamp() function to
# extract datetime from the given timestamp
timestamp = datetime.datetime.fromtimestamp(1669141800)
 
# Calling the strftime() function to convert
# the extracted datetime into its string format
print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))

#output PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> python timestamp.py
#2022-11-23 00:00:00
 