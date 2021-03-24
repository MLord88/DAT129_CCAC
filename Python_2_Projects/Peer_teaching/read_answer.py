count = 0
#open file and handle exception:
#make note what the file name you want to open is so you can test
while True:
    try:
        user = input("Enter the name of the file which you would like to open: ")
        myfile = open(user, 'r')
        Name = "Name: "
        Golf = "Golf Score: "
        break
    raise FileNotFoundError("File not found, please try again")
    finally:
        count += 1
        print(f'You have performed this action {count} time(s)!\n')



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

