import urllib.request
import urllib.parse
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')

    try:
        js = json.loads(data.decode('ascii'))
    except:
        js = None

    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue

    print (json.dumps(js, indent=4))


location = js['results'][0]['formatted_address']
c_code = js['results'][0]['address_components'][-1]['short_name']
if len(c_code) != 2:
    print("No Country Code Provided")
else:
    print (location)
    print(c_code)