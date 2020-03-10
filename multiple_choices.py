province=input("What's province you live in? ")
tax=0

#if province == 'Alberta' or province == 'Nunavat':
if province in ('Alberta','Nunavat','Yukon'):
    tax=0.05
elif province == 'Ontario':
    tax=0.13
else: 
    tax=0.15

print(tax)
