def func1():
    #Dictionary Introduction
    book_1 = {'author': 'thang lc', 'price': 20}

    print(book_1['author'])
    print(book_1['price'])

def func2():
    # Using a key to get a value
    # Create a dictionary of terms
    terms = {
        'variable': 'Represents or refers to a value stored in memory','string': 'A sequence of character'
        }

    if 'float' in terms:
        print("I know what a float is.")
    else:
        print("I do not know what that is.")
        while True:
            print("Would you like to define it?")
            choice = input('Y/N? ')
            if choice == 'Y':
                terms['float'] = input('Please enter the definition of "float": ')
                return False
            elif choice == 'N':
                print("It's ok to not know everything!")
                return False
            else:
                print('Please type Y or N for selection!')
   
    print(terms['variable'])

def func3():
    #Using get() method with a dictionary
    terms = {'integer' : 'A whole number', 'string' : 'A sequence of characters'}
    print(terms.get('integer'))

    #neu khong get() duoc, thi hien gia tri o vi tri 2
    print(terms.get('float', 'Not in the dictionary!'))  
    
    del terms['integer']
    print(terms)

def func4():
    b_months = {
        'tony' : 'november',
        'pat'  : 'june',
        'mary' : 'may',
    }

    print(b_months)
    



    