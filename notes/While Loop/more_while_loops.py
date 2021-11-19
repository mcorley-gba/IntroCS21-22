#Using while loops with more than one piece of data at a time.

#A for loop is great for looping through a list
#BUT don't change the list entries too much in a for loop. 


#Move items from list A to list B
#Move users from an unconfirmed list to a confirmed list:
#Start with unconfirmed users:
unconfirmed_users = ['dwayne', 'john', 'brian', 'greg']
#Empty list for confirmed users:
confirmed_users = []

#Move the users one at a time until there are no more in the unconfirmed list
# if unconfirmed_users
while unconfirmed_users: #will run as long as there are users in the unconfirmed list.
    current_user = unconfirmed_users.pop() #take the last entry of the list
                                            #store in new variable current_user
    print(f"Verifying user: {current_user}.")
    confirmed_users.append(current_user) #Add current user to confirmed users. 

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)

print('\n\n\n\n\n\n\n\n')
#Do you remember how to remove a single item from a list?
#del works if you know the index.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets) #print original list
#pets.remove('cat') #deletes only the first instance of the string
#print(pets)

#Loop through pets with a while loop and remove all the 'cat' entries
# What will -- if 'cat' in pets:
while 'cat' in pets: #As long as the string 'cat' is in the list, the loop will run.
    pets.remove('cat')

#print modified list:
print(pets)

print('\n\n\n\n\n\n\n')

#Fill a dictionary with user input
#Make a polling program that collects participants name and address

responses = {}

#Set a flag to indicate the poll is still active:
polling_active = True

while polling_active:
    #Prompt for the person's name and response:
    name = input("\nWhat is your name?")
    response = input("\nWhat is your address?")

    #Store the response in the dictionary:
    responses[name] = response #Adding new entry in dictionary dictionary[new_key] = new_value

    #Find if anyone is going to take the poll:
    repeat = input("Would you like to let another person take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Now polling is complete, show results.
print("\n --- Poll Results --- ")
for name, response in responses.items():
    print(f"{name}'s address is {response}.")