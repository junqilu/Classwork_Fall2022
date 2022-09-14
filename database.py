def create_patient_entry(patient_name, patient_id, patient_age): #Make new entries into a database list by appending to that db list
    new_patient = [patient_name, patient_id, patient_age, []]
    
    return new_patient

def db_printer(inputDatabase): #Print out the whole inputDatabase
    for line in inputDatabase: 
        print(line)
        print('Patient name: {}, Patient ID: {}, Patient age:{}'.format(line[0], line[1], line[2]))
        
    return 0

def db_searcher(inputDatabase, patientID): #Search through inputDatabase for a line with matched patientID
    for line in inputDatabase:
        if line[1] == patientID: 
            return line
    
    return False #This means nothing found for that patientID

def db_result_adder(inputDatabase, patientID, testName, testValue): #Add test name and test result into a patient's info through patientID in a inputDatabase
    line = db_searcher(inputDatabase, patientID)
    
    line[3].append((testName, testValue)) #Prof wants to add testName, testValue as a tuple into that list
    
    return 

def main():
    db = [] #This stores all the patient lists
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 24))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    db_printer(db)
    
    x = db_searcher(db, 2)
    print(x)
    
    db_result_adder(db, 1, 'HDL', '100')
    print(db)
    
    
    roomList = ['Room 1', 'Room 2', 'Room 3']
    for idx, patient in enumerate(db): 
        print('Name = {}, Room = {}'.format(patient, roomList[idx]))
        
        
    for patient, room in zip(db, roomList):
        print('Name = {}, Room = {}'.format(patient, room))
    
    return 0

    
if __name__ == "__main__":
    main()
