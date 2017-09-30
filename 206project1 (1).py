import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	usefile = open(file, "r")
	splitdata = [newline.strip().split(',') for newline in usefile.readlines()]
	headings = splitdata[0]
	alldata = []
	for info in splitdata[1:]:
		backgroundinfo = {}
		backgroundinfo[headings[0]] = info[0]
		backgroundinfo[headings[1]] = info[1]
		backgroundinfo[headings[2]] = info[2]
		backgroundinfo[headings[3]] = info[3]
		backgroundinfo[headings[4]] = info[4]
		alldata.append(backgroundinfo)
	return alldata


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	newlist = sorted (data, key = lambda x: x[col])
	newperson = newlist[0]
	return newperson['First'] + " " + newperson['Last']

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	classes = {}
	for dic in data:
		if dic["Class"] not in classes:
			classes[dic["Class"]] = 0
		classes[dic["Class"]] += 1
	return sorted (classes.items(), key = lambda x: x[1], reverse = True)



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	dic = {}
	for student in a:
		date = student["DOB"].split('/')[1]
		if date in dic:
			dic[date] +=1
		else:
			dic[date] =1 
	days = list(dic.keys())
	mostcommon_day = days[0]
	for x in days:
		if dic[x] > dic[mostcommon_day]:
			mostcommon_day = x
	return int(mostcommon_day)


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	import datetime
	avg_age = []

	for date in a[1:]:

		month, day, year = date["DOB"].split("/")
		thisyear = int(datetime.date.today().year)
		thismonth = int(datetime.date.today().month)
		today = int(datetime.date.today().day)

		if int(year) == int("2017"):
			if ((today > int(day)) and thismonth > int(month)):
				if int(month) == 1 or 2 or 3:
					avg_age.append(int('1'))
				else:
					avg_age.append(int('0'))
			else:
				avg_age.append(int('0'))
		else:
			if ((today > int(day)) and thismonth >int(month)):
				avg_age.append(thisyear - int(year))
			else:
				avg_age.append(thisyear - int(year) + 1)

	return int(round((sum(avg_age)/len(avg_age)),0))

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	output = open(fileName, 'w')
	newlist = sorted(a, key = lambda x: x[col])
	for dic in newlist:
		x = dic["First"]
		y = dic["Last"]
		z = dic["Email"]
		output.write("{},{},{}\n".format(x,y,z))
	output.close()



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

