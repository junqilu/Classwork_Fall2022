def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    
    keepRunning = True
    while keepRunning:
        choice = input("Enter your choice: ")
        if choice == '9':
            return
   
interface()