with open("Path.txt","r") as txt:
	for line in txt:
		print line

x=str(raw_input("Enter your date of Birth: "));
y=str(raw_input("Enter your last name: "));
print "Hello " +y, 
print "born on " +x

