from urllib.parse import urlencode
from requests import get



# Replace with your API key here!
KEY = 'AIzaSyApUODYn6dpkpTWsX62LkJxAVZlSDdk_rE'
KEY = 'AIzaSyC8ezA75-Lhm4C6GWowFDrH9fLI19AqtOU'



def _fetch(api, args):

    base_url = 'https://maps.googleapis.com/maps/api/%s/json?key=%s&'
    return get(base_url % (api, KEY) + urlencode(args)).json()

def _decode(polyline):

    values, current = [], []
    for byte in bytearray(polyline, 'ascii'):

        byte -= 63

        current.append(byte & 0x1f)
        if byte & 0x20:

            continue

        value = 0
        for chunk in reversed(current):

            value <<= 5
            value |= chunk

        values.append(((~value if value & 0x1 else value) >> 1) / 100000.)
        current = []

    result, x, y = [], 0., 0.
    for dx, dy in [tuple(values[i:i+2]) for i in range(0, len(values), 2)]:

        x, y = x + dx, y + dy
        result.append((round(x, 6), round(y, 6)))

    return result



def coordinates(location):
    '''
    Get the coordinates of a given location.
        >>> coordinates('Paris')
        (48.856614, 2.3522219)
    Returns None if it didn't work.
    '''

    try:

        result = _fetch('geocode', {'address': location})
        result = result['results'][0]['geometry']['location']

    except:

        return None

    return result['lat'], result['lng']

def name(lat,lng):
    '''
    Get the name of a given location.
    According to the geocoordinates
    Returns None if it didn't work.
    '''

    try:



        result = _fetch('geocode', {'lat': lat,'lng': lng})
        result = result['results'][0]
        print("r",result)

    except:

        return None

    return result['formatted_address']


def distance(lat,lng):
    '''
    Get the distance between to points.
    According to the geocoordinates
    Returns None if it didn't work.
    '''

    try:



        result = _fetch('geocode', {'lat': lat,'lng': lng})
        result = result['results'][0]
        print("r",result)

    except:

        return None

    return result['formatted_address']




def path(origin, destination = None, mode = 'walking'):
    '''
    Find a not-so-long path from somewhere to somewhere else.
    'origin' and 'destination' must be coordinates.
    If 'destination' is omitted, 'origin' must be a list of coordinates.
        >>> path(coordinates('Paris'), coordinates('London'))
        [(48.85668, 2.35196), (48.86142, 2.33929), (48.86897, 2.32369), ...
    Returns a list of coordinates to follow, or None if it didn't work either.
    '''

    args = {'mode': mode}
    if destination:

        origin, destination = '%f,%f' % origin, '%f,%f' % destination

    else:

        points = ['%f,%f' % coordinates for coordinates in origin]
        origin, destination = points[0], points[-1]

        if len(points) > 2:

            args = {'waypoints': 'optimize:true|via:' + '|via:'.join(points[1:-1])}

    args.update({'origin': origin, 'destination': destination})
    try:

        result = _fetch('directions', args)
        # You can extract other useful informations here, such as duration
        #print(result['routes'][0])
        for key in result['routes'][0]['legs'][0]['distance']:
            print(key)
        print(result['routes'][0]['legs'][0]['distance'])
        result = result['routes'][0]['overview_polyline']['points']
       

    except:

        return None

    return _decode(result)

def distance_duration(origin, destination = None, mode = 'walking'):
    '''
    Find a not-so-long path from somewhere to somewhere else.
    'origin' and 'destination' must be coordinates.
    If 'destination' is omitted, 'origin' must be a list of coordinates.
        >>> path(coordinates('Paris'), coordinates('London'))
        [(48.85668, 2.35196), (48.86142, 2.33929), (48.86897, 2.32369), ...
    Returns a list of coordinates to follow, or None if it didn't work either.
    '''

    args = {'mode': mode}
    if destination:

        origin, destination = '%f,%f' % origin, '%f,%f' % destination

    else:

        points = ['%f,%f' % coordinates for coordinates in origin]
        origin, destination = points[0], points[-1]

        if len(points) > 2:

            args = {'waypoints': 'optimize:true|via:' + '|via:'.join(points[1:-1])}

    args.update({'origin': origin, 'destination': destination})
    try:

        result = _fetch('directions', args)
        # You can extract other useful informations here, such as duration
        #print(result['routes'][0])
        for key in result['routes'][0]:
            print(key)
        distance = result['routes'][0]['legs'][0]['distance']['text']
        duration = result['routes'][0]['legs'][0]['duration']['text']
        #result = result['routes'][0]['overview_polyline']['points']
       

    except:

        return None

    return distance, duration

#print(coordinates('Paris'))
print(coordinates('Brussel'))
distance, duration = distance_duration(coordinates('Brussel'),coordinates('Gent'),'bycicle')
print(duration)
print(distance)