def interface():
    print("My Program")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze Total Cholesterol")
    print("9 - Quit")

    keepRunning = True
    while keepRunning:
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == "1":
            HDLDriver()
        elif choice == '2':
            LDLDriver()


def inputHDL():
    HDLInput = input(
        "Enter the HDL value:")  # This string will contain an int
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


def inputLDL():
    LDLInput = input(
        "Enter the LDL value:")  # This string will contain an int
    return int(LDLInput)


def check_LDL(LDLValue):
    if LDLValue < 130:
        return "Normal"
    elif LDLValue < 159:
        return "Borderline High"
    elif LDLValue < 189:
        return "High"
    else:
        return "Very High"


def OutputLDLResult(LDLValue, charac):
    print("The results for an LDL value of {} is {}".format(LDLValue, charac))


def LDLDriver():
    LDLValue = inputLDL()
    answer = check_LDL(LDLValue)
    OutputLDLResult(LDLValue, answer)


def inputTotalCholesterol():
    TotalCholesterolInput = input(
        "Enter the TotalCholesterol value:")  # This string will contain an int
    return int(TotalCholesterolInput)


def check_TotalCholesterol(TotalCholesterolValue):
    if TotalCholesterolValue < 200:
        return "Normal"
    elif TotalCholesterolValue < 239:
        return "Borderline High"
    else:
        return "High"


def OutputTotalCholesterolResult(TotalCholesterolValue, charac):
    print("The results for an TotalCholesterol value of {} is {}".format(
        TotalCholesterolValue, charac))


def TotalCholesterolDriver():
    TotalCholesterolValue = inputTotalCholesterol()
    answer = check_TotalCholesterol(TotalCholesterolValue)
    OutputTotalCholesterolResult(TotalCholesterolValue, answer)


interface()
