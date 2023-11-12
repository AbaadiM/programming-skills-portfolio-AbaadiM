pets=[]

pet={ 'animal': 'dog',
      'name' : 'max',
      'owner' : 'obaid',
      'food' : 'humans'
    }

pets.append(pet)

pet={ 'animal': 'cat',
      'name' : 'tinker',
      'owner' : 'mohammed',
      'food' : 'tuna'
    }

pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title())
    for key, value in pet.items():
        print("\t" + key + " : " + value)