def describe_city(city, country='Pakistan'):
    msg = city.title() + " is in " + country.title() 
    print(msg)

describe_city('Lahore')
describe_city('Faisalabad')
describe_city('Reykjavik' , ' Iceland')