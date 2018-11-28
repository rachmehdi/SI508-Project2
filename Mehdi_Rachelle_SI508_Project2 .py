import secrets
from bs4 import BeautifulSoup
import requests
import requests_cache
requests_cache.install_cache('sample_advanced_caching')
import json
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

#Scrape nps.gov using caching --> using class Cache from proj2_nps.py? 
#Information should include the site name, site type, and the physical (or mailing) address
#Should not make new requests each time you run the program 

# set up national parks class to get a clear idea of what info you want to get via scraping 
# implement scraping, pull data to create objects using class
# do caching 
# this, if done correctly, should complete part 1 of the project 

#three things you could be caching 
#1) list of all the states
#2) links to all their websites
#3) cache the html page with all those links 
#once you have them, make a request to each of those sites' homepage 
#in this case it's the state home page of michigan 
#once you've gone to the park page, cache that 
#cache all three
#one big cache file, home page, state name, site name 
#grab site links, go through each of them and scrape --> write forloop to do this for each site

#create a beefy function that logs you into the page you have to be at using beautiful soup. Search for whatever state you want it to go to (ex. Michigan)

#write a function that checks my cache

google_places_key = secrets.google_places_key
PLOTLY_USERNAME = secrets.PLOTLY_USERNAME
PLOTLY_API_KEY = secrets.PLOTLY_API_KEY
MAPBOX_TOKEN = secrets.MAPBOX_TOKEN


base_url = 'https://www.nps.gov'
extension = '/index.htm'


# =============================================================================
#     dict_cache = load_cache()
#     data = get_from_cache(state_sites_key, dict_cache)
#     if data != None:
#         return data # do something
#     else:
#         sites_list = create_sites_for_state(full_name) 
#         return "Called request"
# =============================================================================

CACHE_FNAME = "site_cache.json"
CACHE_NEARBY_SITE = "nearby_site_cache.json"

try:
    with open(CACHE_FNAME) as cached_file:
        CACHE_SITE_DICTION = json.load(cached_file)
except:
    CACHE_SITE_DICTION = {}

try:
    with open(CACHE_NEARBY_SITE) as cached_file2:
        CACHE_NEARBY_SITE_DICTION = json.load(cached_file2)
except:
    CACHE_NEARBY_SITE_DICTION = {}

# =============================================================================
# ################### PART 1 ######################
# =============================================================================


class NationalSite():
    def __init__(self, type, name, desc,url=None):
        self.type = type
        self.name = name
        self.description = desc
        self.url = url
        
        if url:
            NPS_address = requests.get(url).text
            soup = BeautifulSoup(NPS_address, 'html.parser')
            address = soup.find('p', class_='adr')
            try:
                self.address_street = address.find('span', itemprop = 'streetAddress').text.strip()
                self.address_city = address.find('span', itemprop = 'addressLocality').text.strip()
                self.address_state = address.find('span', itemprop = 'addressRegion').text.strip()
                self.address_zip = address.find('span', itemprop = 'postalCode').text.strip()
            except:
                self.address_street = ''
                self.address_city = ''
                self.address_state = ''
                self.address_zip = ''  
        else:
            self.address_street = ''
            self.address_city = ''
            self.address_state = ''
            self.address_zip = ''            

    
    def __str__(self):
        string_site =  "{} ({}): {}".format(self.name, self.type, self.address_street + ', ' + self.address_city + ', ' + self.address_state + ' ' +  self.address_zip)
        return string_site

def get_state_full_name(state_abbr):
    return { 
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming', 
        'ak': 'Alaska',
        'al': 'Alabama',
        'ar': 'Arkansas',
        'as': 'American Samoa',
        'az': 'Arizona',
        'ca': 'California',
        'co': 'Colorado',
        'ct': 'Connecticut',
        'dc': 'District of Columbia',
        'de': 'Delaware',
        'fl': 'Florida',
        'ga': 'Georgia',
        'gu': 'Guam',
        'hi': 'Hawaii',
        'ia': 'Iowa',
        'id': 'Idaho',
        'il': 'Illinois',
        'in': 'Indiana',
        'ks': 'Kansas',
        'ky': 'Kentucky',
        'la': 'Louisiana',
        'ma': 'Massachusetts',
        'md': 'Maryland',
        'me': 'Maine',
        'mi': 'Michigan',
        'mn': 'Minnesota',
        'mo': 'Missouri',
        'mp': 'Northern Mariana Islands',
        'ms': 'Mississippi',
        'mt': 'Montana',
        'na': 'National',
        'nc': 'North Carolina',
        'nd': 'North Dakota',
        'ne': 'Nebraska',
        'nh': 'New Hampshire',
        'nj': 'New Jersey',
        'nm': 'New Mexico',
        'nv': 'Nevada',
        'ny': 'New York',
        'oh': 'Ohio',
        'ok': 'Oklahoma',
        'or': 'Oregon',
        'pa': 'Pennsylvania',
        'pr': 'Puerto Rico',
        'ri': 'Rhode Island',
        'sc': 'South Carolina',
        'sd': 'South Dakota',
        'tn': 'Tennessee',
        'tx': 'Texas',
        'ut': 'Utah',
        'va': 'Virginia',
        'vi': 'Virgin Islands',
        'vt': 'Vermont',
        'wa': 'Washington',
        'wi': 'Wisconsin',
        'wv': 'West Virginia',
        'wy': 'Wyoming'}[state_abbr]

#print (get_state_full_name("mi"))

def get_sites_for_state(state_abbr):
    url = base_url + '/state/%s' % (state_abbr.lower()) + extension
    NPS_park_sites = requests.get(url).text
    soup = BeautifulSoup(NPS_park_sites, 'html.parser')
    
    site_list = []
    
    sites = soup.find_all('li', class_='clearfix')[:-1]
    
    for site in sites:
        site_park_name = site.find('a').text
        site_park_type = site.find('h2').text
        site_park_desc = site.find('p').text
        site_park_ext = site.find('h3').find('a')['href']
        site_park_url = base_url + site_park_ext + extension
        site_list.append(NationalSite(site_park_type, site_park_name, site_park_desc, site_park_url))
#    for site in site_list:        
#        print(site)
    return site_list

#get_sites_for_state('tn')

# =============================================================================
# ################### PART 2 ######################
# =============================================================================


class NearbyPlace():
    def __init__(self, name, CoordDict = {}):
        self.name = name
        self.coord = CoordDict
        
    def __str__(self):
        place_name = self.name
        return place_name

def get_nearby_places(site_object):
    baseurl = "https://maps.googleapis.com"
    searchUrl = "/maps/api/place/findplacefromtext/json"
    parameters = {}
    parameters["key"] = google_places_key
    parameters["fields"] = "name,geometry"
    parameters["inputtype"] = "textquery"
    parameters["input"] = site_object
    google_response = requests.get(baseurl + searchUrl, params=parameters)
    google_map = google_response.text
    google_object = json.loads(google_map)
    candidates = google_object['candidates']

    if len(candidates) > 0:
        coordinates_dictionary = candidates[0]['geometry']['location']
        nearby_key = str(coordinates_dictionary['lat']) + ',' + str(coordinates_dictionary['lng'])
    else:
        coordinates_dictionary = {}
        print("Unable to get national site coordinates, can't plot nearby")

    nearbyUrl = "/maps/api/place/nearbysearch/json"
    
    if nearby_key in CACHE_NEARBY_SITE_DICTION:
        google_object2 = CACHE_NEARBY_SITE_DICTION[nearby_key]
    else:
        nearby_parameters = {}
        nearby_parameters["key"] = google_places_key
        nearby_parameters["location"] = str(coordinates_dictionary['lat']) + "," + str(coordinates_dictionary['lng'])
        nearby_parameters["radius"] = 10000 
    
        google_nearby = requests.get(baseurl + nearbyUrl, params=nearby_parameters)
        google_nearby_text = google_nearby.text
        google_object2 = json.loads(google_nearby_text)
        CACHE_NEARBY_SITE_DICTION[nearby_key] = google_object2
        
    with open(CACHE_NEARBY_SITE, 'w') as cache_file:
        cache_file.write(json.dumps(CACHE_NEARBY_SITE_DICTION))

    nearby_results = google_object2['results']
    NearbyPlace_instances = []
    for result in nearby_results:
        name = result['name']
        coord = result['geometry']['location']
        if name != site_object:
            result_object = NearbyPlace(name, coord)
            NearbyPlace_instances.append(result_object)
    return NearbyPlace_instances

# =============================================================================
# ################### PART 3 ######################
# =============================================================================


def plot_sites_for_state(state_abbr):
    sites = get_sites_for_state(state_abbr)
    latitudes = []
    longitudes = []
    list_of_names = []

    for site in sites:
        sitekey = (site.name + " " + site.type).strip()
        if sitekey in CACHE_SITE_DICTION:
            google_object = CACHE_SITE_DICTION[sitekey]
        else:
            baseurl = "https://maps.googleapis.com"
            searchUrl = "/maps/api/place/findplacefromtext/json"
            parameters = {}
            parameters["key"] = google_places_key
            parameters["fields"] = "name,geometry"
            parameters["inputtype"] = "textquery"
            parameters["input"] = sitekey
            google_resp = requests.get(baseurl + searchUrl, params=parameters)
            google_text = google_resp.text
            google_object = json.loads(google_text)
            CACHE_SITE_DICTION[sitekey] = google_object
    
    
        candidates = google_object['candidates']
    
        if len(candidates) > 0:
            coordinates_dictionary = candidates[0]['geometry']['location']
        else:
            coordinates_dictionary = {}
        with open(CACHE_FNAME, 'w') as my_cache_file:
            my_cache_file.write(json.dumps(CACHE_SITE_DICTION))
    

        name = site.name
        list_of_names.append(name)
        if coordinates_dictionary:
            latitudes.append(coordinates_dictionary['lat'])
            longitudes.append(coordinates_dictionary['lng'])

    min_lat = 200
    max_lat = -200
    min_lon = 200
    max_lon = -200
    
    for str_v in latitudes:
        v = float(str_v)
        if v < min_lat:
            min_lat = v
        if v > max_lat:
            max_lat = v
    for str_v in longitudes:
        v = float(str_v)
        if v < min_lon:
            min_lon = v
        if v > max_lon:
            max_lon = v
    
    center_lat = (max_lat+min_lat) / 2
    center_lon = (max_lon+min_lon) / 2
    
    data = [
        go.Scattermapbox(
            lat= latitudes,
            lon= longitudes,
            mode='markers',
            marker=dict(
                size=9
            ),
            text= list_of_names,
        )
    ]
    
    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=MAPBOX_TOKEN,
            bearing=0,
            center={'lat': center_lat, 'lon': center_lon },
            pitch=0,
            zoom=5
        ),
    )
    
    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='Proj2 Sites Plot')

plotly.tools.set_credentials_file(username=PLOTLY_USERNAME, api_key=PLOTLY_API_KEY)

def plot_nearby_for_site(site_object):
    nearby_objects = get_nearby_places(site_object)
    latitudes = []
    longitudes = []
    list_of_names = []
    
    if nearby_objects:
        for nearby_object in nearby_objects:
            name = nearby_object.name
            list_of_names.append(name)
            if nearby_object.coord:
                coordinates = nearby_object.coord
                latitudes.append(coordinates['lat'])
                longitudes.append(coordinates['lng'])
        min_lat = 200
        max_lat = -200
        min_lon = 200
        max_lon = -200
    
        for str_v in latitudes:
            v = float(str_v)
            if v < min_lat:
                min_lat = v
            if v > max_lat:
                max_lat = v
        for str_v in longitudes:
            v = float(str_v)
            if v < min_lon:
                min_lon = v
            if v > max_lon:
                max_lon = v
    
        center_lat = (max_lat + min_lat) / 2
        center_lon = (max_lon + min_lon) / 2
    
        data = [
            go.Scattermapbox(
                lat=latitudes,
                lon=longitudes,
                mode='markers',
                marker=dict(
                    size=9
                ),
                text=list_of_names,
            )
        ]
    
        layout = go.Layout(
            autosize=True,
            hovermode='closest',
            mapbox=dict(
                accesstoken=MAPBOX_TOKEN,
                bearing=0,
                center={'lat': center_lat, 'lon': center_lon},
                pitch=0,
                zoom=10
            ),
        )
    
        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='Project2 Plot Nearby Sites')





# =============================================================================
# ################### PART 4 ######################
# =============================================================================


results = []
state_input = ''
site_input = ''
last_command = ''

user_input = input("Enter Command (or 'help' for options, enter 'exit' to quit this program): ")
command = user_input.split(' ')

help_statement = """list <stateabbr> e.g. list AK
       result: lists all National Sites in a state with index
       valid inputs: a two-letter state abbreviation

nearby <result_number> e.g. nearby 2
       available only after you have listed the sites of a state
       result: lists all Places nearby a given result
       valid inputs: an integer corresponding to index of that site.

  map
       result: displays the current results on a map

  exit
       exits the program

  help
       lists available commands"""

while command[0] != 'exit':
    if command[0] == 'help':
        print ('\n', help_statement)
    elif command[0] == 'list':
        print ("\nNational Sites in %s:\n" % (command[1].upper()))
        state_input = command[1]
        results = get_sites_for_state(state_input)
        for each_res in results:
            print (results.index(each_res) + 1, ') ', str(each_res), '\n')
        last_command = 'list'
    elif command[0] == 'nearby':
        if len(results) == 0:
            print ("First input command 'list' followed by state abbreviation of choice.\n")
        else:
            nearby_places = get_nearby_places(results[int(command[1]) - 1])
            print ("\nPlaces near ", results[int(command[1]) - 1].name, ',' ,results[int(command[1]) - 1].type, '\n')
            for place in nearby_places:
                print (nearby_places.index(place) + 1, ') ', str(place), '\n')
            results.append(nearby_places)
            site_input = nearby_places
        last_command = 'nearby'
    elif command[0] == 'map':
        if len(results) == 0:
            print ("Invalid command. First input command 'list' or command 'nearby'.\n")
        elif last_command == 'list':
            plot_sites_for_state(state_input)
        elif last_command == 'nearby':
            plot_nearby_for_site(site_input)
    else:
        print ('Invalid input. Please try again.\n')
    user_input = input("Enter Command (or 'help' for options, 'exit' to quit program): ")
    command = user_input.split(' ')
print('Program Exited')