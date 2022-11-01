db = ''

def add_to_database(new_entry):
    global db
    db = '{},{}'.format(db, new_entry)

def main():
    add_to_database(1)
    add_to_database(2)
    print(db)

if __name__ == '__main__':
    main()