students = ['collin', 'logan', 'doug', \
            'MaKenna', 'Ryder', 'Noah',\
            'Noah L.', 'Ramsey', 'Kameron', 'Ty']

#Use for loops to work on every entry in the list.

for student in students:
#for - tells python we're starting a loop
#student - is a dummy variable to hold individual entries
#           of the students list
#student in students - tells python to loop through each 
#           entry in the list
# : - tells python to start the loop.
    print(f"{student.title()}, you did well on the last HW.")
    print(f"{student.upper()}, you've done great work so far!\n")

print("Our next test will be after Fall Break.".upper())
#Un indent to get out of loop

#General syntax for looping through a list:
# for item in list_of_items:
#   Instructions...

for student in students:
    print(student)

    print(student, "you have learned a lot.")

#What happens when you indent, but you don't need to.

message = "Hello, everyone! Nice weather today."
    #print(message) -- unexpected indent
#Fix 1 - Un indent
print(message)

#Fix 2 - Wrap in a loop -- stays indented
litsa  = ['a', 'b', 'c']
for alsdkjfalsdkj in litsa:
    print(message)

#fix 3 - Remove the offending code entirely.

another_list = ['sadie', 'orange peel', 'hong kong']
for stuff in another_list:
    print(stuff)
