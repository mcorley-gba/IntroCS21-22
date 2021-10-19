#For each of the following type of tests,
#write at least one True and one False test.
#You may either hand write the code, or you
#may type it on your iPad (in a google doc, 
#for example), and submit it to google classroom

#1. Test for equality with strings

#2. Test for inequality with strings

#3. Test with strings using the .lower() method

#4. Numerical tests with ==, !=, <=, >=, <, and >

#5. Test multiple conditions with 'and'

#6. Test multiple conditions with 'or'

#7. Test if an item is in a list. 

#8. Test if an item is not in a list
#   (I dont' think we covered this, but it is not difficult.
#    Python is very natural with its language here. To test
#    if an item is NOT in a list, simply use the format
#    
#    [item] not in [list]
#
#    where [item] and [list] are your particular values,
#    variables, or list. 

#All in all, you should have 26 tests, one True
#and one False for each of the above. Your tests should 
#look something like this:

today = 'Wednesday'
print(today == 'Wednesday') #will print True. 

voting_age = 18 
my_age = 16
print(my_age >= voting_age) #will print False.

tomorrow = 'Thursday'
weather = 'Rain'
print((today != tomorrow) and (weather == 'Sun')) #will print False

fav_restaurants = ['McDonalds', 'Taco Bell', 'Sonic']
print('KFC' not in fav_restaurants) #will print True

#You should come up with your own tests and not use these
#three examples. If you run into trouble, ask your neighbor
#for help, do your best, and submit what you've got. We will
#begin Thursday by discussing this work. 