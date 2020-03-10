from array import array

scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

names=['mink','da']
print(len(names))
names.insert(0,'rj')
print(names)
names.sort()
print(names)

names2=['mink','da','momo','rj']
presenters=names2[1:3]
presenters2=names2[:3]


print(names2)
print(presenters)

print(presenters2)

