def get_initial(name,forceupper=True):
    if forceupper:
        initial=name[0:1].upper()
    else:
        initial=name[0:1]

    return initial

first_name=input('Enter your first name ')
first_name_ininitial=get_initial(first_name,True)

last_name=input('Enter your last name ')
last_name_ininitial=get_initial(last_name)

print('Your ininitial name is '+ first_name_ininitial + last_name_ininitial)

#swap param location

first_name=input('Enter your first name ')
first_name_ininitial=get_initial(forceupper=False,name=first_name)

last_name=input('Enter your last name ')
last_name_ininitial=get_initial(name=last_name,forceupper=False)


print('Your ininitial name is '+ first_name_ininitial + last_name_ininitial)
