def interface():
    print("My Program")
    print("Options:")
    print("1 - Analyze HDL")
    print("9 - Quit")
    
    keepRunning = True
    while keepRunning:
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == "1":
            HDLDriver

def inputHDL():
    HDLInput = input(""Enter the HDL value:) #This string will contain an int 
    return int(HDLInput)
    
def check_HDL(HDLValue):
    if HDLValue < 40:
        return "Low"
    elif HDLValue < 60:
        return "Borderline Low"
    else: 
        return "Normal"

def OutputHDLResult(HDLValue, charac):
    print("The results for an HDL value of {} is {}".format(HDLValue, charac))


def HDLDriver(): 
    HDLValue = inputHDL()
    answer = check_HDL(HDLValue)
    OutputHDLResult(HDLValue, answer)

interface()