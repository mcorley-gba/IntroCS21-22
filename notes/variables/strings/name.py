name = "ada lovelace"
#print(name.title())

#name refers to a the string "ada lovelace". The title *method* changes each word 
#to title-case.

#A method is a specific function or group of funcitons that python can perform on
#   a piece of data.

name = "adA LoveLace"
#print(name.upper())
#print(name.lower())
#print(name.title())

#Use variables within strings

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
#Important: put the letter f immediately before the opening quotation marks
#           put braces around any variable names
#This is an 'f-string' 
print(full_name)
print(f'{full_name.title()}')