name = "    Luong Cao Thang     "

first_name = "thang"
last_name = "luong cao"

##string.method

#Print first_name viet hoa chu dau
print(first_name.title())

#Tim index cua String 'a' trong variable name
print(name.find('a'))

#Print name in lowercase
print(name.lower())

#Replace a part of a string
print(name.replace('Cao', 'Kow'))

#Remove white space from the left/right or both from a string
print(name.strip())
print(name.lstrip())
print(name.rstrip())

#Adding white space, \t and \n
print('\t'+name+'\n')

############################

#Convert number to string, vice versa

name = 'thang'.title()
date_today = 24
welcome_message = "Hi " + name + "welcome back, today's date is the " + str(date_today) + " of October"
print(welcome_message)

number1 = "24"
number2 = 25
total = int(number1) + number2
print(total)

############################

###List

##Create list

months = ["jan", "feb", "mar", "apr", "may"]

print(months)

print(months[0])

print(months[0].title())

##Modify list with methods: append(), insert(), del

bmonths = ["spril", "may", "june", "july"]
print(bmonths)

bmonths[0] = 'april'
print(bmonths)

bmonths.append('mars')
print(bmonths)

bmonths = []
print(bmonths)

bmonths.append('august')
print(bmonths)

bmonths.insert(1, 'july')
print(bmonths)

del bmonths[1]
print(bmonths)

##Using methods: pop() and remove()

subscribers = ["Lorel@example.com", "Ipslum@example.com", "LorelIpslum@example.com"]
print(subscribers)
popped_subscribers = subscribers.pop()
print(subscribers)
print(popped_subscribers + "\n")

subscribers = ["Lorel@example.com", "Ipslum@example.com", "LorelIpslum@example.com"]
first_subscriber = subscribers.pop(0)
print("Your first subscriber: " + first_subscriber + " has been unsubbed!")
print(subscribers)

sub_by_mistake = "Ipslum@example.com"
subscribers.remove(sub_by_mistake)
print("This user: " + sub_by_mistake + " did not mean to sign up!")

##Organizing a list

#Sap xep theo thu tu A-Z vinh vien
b_months = ['may', 'november', 'june']
b_months.sort() 
print(b_months)

#Sap xep theo thu tu Z-A vinh vien
b_months.sort(reverse=True) 
print(b_months)

#Sap xep tam thoi
print(sorted(b_months)) 
print(b_months)

#Dao nguoc trinh tu sap xep ban dau
b_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
b_days.reverse() 
print(b_days)

#Methods: len()
print(len(b_days)) #ket qua la 5


##Looping through a loop
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

#Using a 'for' loop to print a list
for month in months:
    print(month.title() +" is the name of a month")


















