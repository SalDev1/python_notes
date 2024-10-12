name = "That's my Boy ! "
print(name)
first_name = "Salman"

print(first_name[3:5])

claim = "Pluto is a planet"
print(claim.split())

datestr = '1956-01-31'
year, month, day = datestr.split('-')
'/'.join([month, day, year])

print("Yoo".join([word.upper() for word in claim]))

"{}, you'll always be the {}th planet to me.".format(planet, position)
