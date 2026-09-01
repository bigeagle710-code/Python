country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '0097',
                'Pakistan' : '0092',
                'USA' : '0001',
                'China' : '0086',
                'Japan' : '0081',
                'South Korea' : '0082',
                'North Korea' : '0850',
                'Turkey' : '0090',}
print("Country code for Japan:")
print(country_code.get('Japan','not Found'))
print("Country code for India:")
print(country_code.get('India','not Found'))
print("Country code for Pakistan:")
print(country_code.get('Pakistan','not Found'))
print("Country code for Afganistan:")
print(country_code.get('Afganistan','not Found'))