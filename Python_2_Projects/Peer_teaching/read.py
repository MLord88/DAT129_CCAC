count = 0

# open file and handle exceptions:
# Create a loop to open this file and handle exceptions if it can not and attempt to reopen another file,
# Also use a "finally" function to count the amount of attempts the user has tried to open a file
# the correct file name is "golf.txt" for testing and it is located in the same folder as this code when downloaded

user = input("Enter the name of the file which you would like to open: ")
myfile = open(user, 'r')
Name = "Name: "
Golf = "Golf Score: "
         

while True:
    data = myfile.readline()
    data = data.rstrip()
    if not data:
        break
    print(Name + data)
    data = myfile.readline()
    data = data.rstrip()
    print(Golf + data)

myfile.close()

