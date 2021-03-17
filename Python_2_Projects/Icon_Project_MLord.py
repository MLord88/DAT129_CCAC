#intitial Variable setup
List_Base = []
Image_Scale = []
Image=[]

def Input(): # Gets the users input values for the image, makes sure input is exactly 100 characters and only includes 1 and 0 
    User_Input = str(input("Enter values here: \n"))
    while any(c.isalpha() for c in User_Input) is True:
        print("\nERROR: Input can only contain 1's and 0's.\n")
        User_Input = str(input("Enter values here: \n"))        
    while len(User_Input) != 100:
        print("\nERROR: Invalid input, must be exactly 100 digits.\n")
        User_Input = str(input("Enter values here: \n"))
    return User_Input
    

def Creation():    # Creation of the base image(no scaling, no rotation)
    User_Input = Input()
    Symbol = input("Next select a symbol that will be used as the base of your image. (Image looks best if you use one of the following symbols!)(!@#$%^&*)\n")  # selects symbol to create image with
    Scale = input("Would you like to scale the image? (Answer with a 'y' or 'n')\n") # Decides how large to scale the image
    #creation of list broken into chunks of 10 for rows in image
    while (len(User_Input) > 0):
        x = (User_Input)[0:(10)] #first 10 * scaling number digits each pass
        List_Base.append(x) 
        User_Input = (User_Input[(10):])  #strips first 10 digits so it does not repeate entries and converts back to int
    # creation of the image
    while (len(List_Base) > 0):   # replaces 1's and 0's with a space and the selected symbol
        x = List_Base.pop(0)
        x = str(x)
        x = x.replace("0"," ")
        x = x.replace("1", Symbol)
        Image.append(x)
        x = ""
    return Scale, Image, Symbol


def Scaled_Image(): # functions to scale and rotate the image created
    Scale, Image, Symbol = Creation()
    Scale = str(Scale)
    if Scale.lower() == 'y':
        Scaling = int(input("How many times would you like to scale the Image? (Image will double)(Input a integer) \n"))
        Image_copy = Image.copy()
        while Scaling > 0:
            i = 20
            while (len(Image_copy)> 0):      # Scales image by replacing one sybol with two and doubling the spaces between them 
                z = Image_copy.pop(0)                      # While loop does this for every line in the list to create the new image
                z = str(z)
                z = z.replace(Symbol, Symbol+Symbol)
                z = z.replace(" ", "  ")
                Image_Scale.append(z)
                Image_Scale.append(z)
                z = ""
                i = i - 1
            Image_copy = Image_Scale.copy()
            Image_Scale.clear()
            Scaling = Scaling - 1
        Rotate = input("Would you like to rotate the image? (Answer with a 'y' or 'n')\n")
        if Rotate.lower() == 'y':  # function to rotate the image created
            Transform_Degree = str(input("How much would you like to rotate the image? (possible rotations in degrees 90, 180, 270)\n"))
            if Transform_Degree == "90":
                print("\n-------------------------------------------------------------------------------------------------------\n\n")   # aesthetic line    
                
                for i in range(len(Image_copy)): 
                    for n in Image_copy:
                        print(n[i], end =' ')
                    print()
            if Transform_Degree == "180":
                print("\n-------------------------------------------------------------------------------------------------------\n\n")      # aesthetic line  
                
                for i in Image_copy[::-1]:
                    print(i)                
            if Transform_Degree == "270":
                Image_copy.reverse()
                print("\n-------------------------------------------------------------------------------------------------------\n\n")      # aesthetic line  
                
                for i in range(len(Image_copy)): 
                    for n in Image_copy:
                        print(n[i], end =' ')
                    print()                
                
        if Scale.lower() == 'y' and Rotate.lower() == 'n':
            print("\n-------------------------------------------------------------------------------------------------------\n \n \n \n")   # aesthetic line(all lines like this are the same)
             
            print(*Image_copy, sep = "\n")
    if Scale.lower() == 'n':
        Rotate = input("Would you like to rotate the image? (Answer with a 'y' or 'n')\n")
        if Rotate.lower() == 'y':
            Transform_Degree = str(input("How much would you like to rotate the image? (possible rotations in degrees 90, 180, 270)\n"))
            if Transform_Degree == "90":  # takes lines and prints them so that the top is to the left
                print("\n-------------------------------------------------------------------------------------------------------\n\n")        
                
                for i in range(len(Image)): 
                    for n in Image:
                        print(n[i], end =' ')
                    print()
            if Transform_Degree == "180":   # Turns image upside down
                print("\n-------------------------------------------------------------------------------------------------------\n\n")        
                
                for i in Image[::-1]:
                    print(i)
                
            if Transform_Degree == "270": # turns image so the top is to the right
                Image.reverse()
                print("\n-------------------------------------------------------------------------------------------------------\n\n")       
                for i in range(len(Image)): 
                    for n in Image:
                        print(n[i], end =' ')
                    print()                            
        if Rotate.lower() == 'n':
            print("\n-------------------------------------------------------------------------------------------------------\n\n")        
            print(*Image, sep = "\n")
    
    
def Intilization():   #Flavor text to start the program
    print("This program is designed to create an image from the input of 100 booleon characters (1's and 0's)!!!!")
    print("Lets get started by inputing our values! Beware!! You must include exactly 100 characters that are either a '1' or a '0'.\n")

    

def Main():  #function to drive the program
    Intilization()
    Scaled_Image()
    




if __name__ == "__main__":  # Starts program
    Main()
