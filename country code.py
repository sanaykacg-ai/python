country_code = {'India' : '0091', 
                'Australia' : '0025', 
                'Nepal' : '00977'}

# Search dictionary for country code of India
print("Country code for India -")
print(country_code.get('India', 'Not Found'))

# Search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))

# Search dictionary for country code of Nepal
print("Country code for Nepal -")
print(country_code.get('Nepal', 'Not Found'))

# Search dictionary for country code of China
print("Country code for China -")
print(country_code.get('China', 'Not Found'))