def get_initial(name):
    initial=name[0:1].upper()
    return initial

first_name=input('Enter your first name ')
first_name_ininitial=get_initial(first_name)

last_name=input('Enter your last name ')
last_name_ininitial=get_initial(last_name)

print('Your ininitial name is '+ first_name_ininitial + last_name_ininitial)

