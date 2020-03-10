your_country=input("Please input your country!  ")

if your_country.lower() == "thailand":
    your_area=input("Please input your area!!  ")

    if your_area in ('bangkok','samutprakarn',\
        'nonthaburi'):
        print("Your area also {} !!".format(your_area))
    elif your_area == "sukhothai":
        print ('Your area is ' + your_area)
else:
    print ("Your country is " + your_country)

