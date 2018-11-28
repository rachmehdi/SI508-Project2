# SI508-Project2
Repository for SI 508 Project 2

RACHELLE MEHDI – SI 508 – Fall 2018

This repository includes the following .py files: 
1.	proj2_nps – skeleton code used to build off of and expand upon (given)
2.	proj2_nps_test – code that tests the skeleton code in Proj2_nps (given)
3.	secrets – a file that includes account information for plotly/google places/mapbox in order to run the code successfully (given empty, updated with own information)
4.	Mehdi_Rachelle_SI508_Project2 – this file includes all of the code required to run project 2 successfully. A more detailed description of this file can be found below.

In order to run this code, you will need to install the following packages.
1.	Plotly - Type the following into your terminal to install Plotly:  pip install plotly 
2.	Requests - Type the following into your terminal to install Requests: pip install requests
3.	BeautifulSoup - Type the following into your terminal to install BeautifulSoup: pip install beautifulsoup4 

The code file “Mehdi_Rachelle_SI508_Project2” should already contain the following quoted text at the very top when you download the file. You will need this text to be present in order to run the code successfully: 

“import secrets
from bs4 import BeautifulSoup
import requests
import requests_cache
requests_cache.install_cache('sample_advanced_caching')
import json
import plotly
import plotly.plotly as py
import plotly.graph_objs as go”
 

In Mehdi_Rachelle_SI508_Project2,  caching takes place through the requests_cache library. Information returned from the requests made through the command input is stored in the cache file “sample_advanced_caching.” Information regarding all national sites for a specified state are cached in the file “site_cache.json” and information regarding all nearby sites for a specified national site are stored in the cache file “nearby_site_cache.json.” 

When you run the code, you will be prompted to input a command. It should look like this: “Enter Command (or 'help' for options, 'exit' to quit program):” If you type “help” then the code will return a list of the commands you are able to invoke/input into the command line. Your first command should be “list” and the abbreviation of the state you are looking for. The code will return a list of indexed national sites in the specified state, including their mailing address. Your second command should be “nearby” and the integer associated with the index of the national site you are interested in, assuming you have already invoked the “list” command. Otherwise, the “nearby” command will be invalid. The code will return a list of nearby places within 10 kilometers. The word “map” is the next command that can be used. If you have already invoked the “nearby” command, it will generate a map of up to 20 nearby places, based on the results of the “nearby” command you invoked earlier. If you invoke the “map” command directly after you have invoked “list,” it will generate a map of all the national sites that are located within the specified state. The map is generated via Plotly and should automatically open up and display in a new webpage in your browser. The “exit” command is the final command you can run. When this command is invoked, it will return “Program Exited” to show you that you are now exiting the program. Otherwise, the code will ask the user to input a new command. If any invalid commands are entered, or commands are entered out of order, the code will return the message “Invalid input. Please try again” and it will prompt the user to enter a new command.



Additional Information to Note: 

1.	If a national site does not have a mailing address, blank values will be returned for each of the address class instances for that site. If a mailing address has not been retrieved, the code will not try to find nearby places.

2.	If a nearby site of a national site does not have any given latitude/longitude coordinates, the code will return a print statement that reads “ Unable to get national site coordinates, can’t plot nearby.” The code will only attempt to retrieve coordinates only after it has created an object from the Google Places API provided within the code. 



Specific example of how to run the code: 

1.	Run the code 
2.	When prompted to enter command, type “list ak” and this will give us an indexed list of all the national sites found in Arkansas. The code returned should look like this: 

1 )  Alagnak (Wild River): PO Box 245, King Salmon, AK 99613 

2 )  Alaska Public Lands (): 605 West 4th Avenue
Suite 105, Anchorage, AK 99501 

3 )  Aleutian World War II (National Historic Area): Affiliated Areas, Alaska Regional Office
National Park Service
240 W 5th Avenue, Anchorage, AK 99501 

4 )  Aniakchak (National Monument & Preserve): PO Box 245, KIng Salmon, AK 99613 

5 )  Bering Land Bridge (National Preserve): P.O. Box 220, Nome, AK 99762 

6 )  Cape Krusenstern (National Monument): PO Box 1029, Kotzebue, AK 99752 

7 )  Denali (National Park & Preserve): PO Box 9, Denali Park, AK 99755 

8 )  Gates Of The Arctic (National Park & Preserve): P.O. Box 30, Bettles, AK 99726 

9 )  Glacier Bay (National Park & Preserve): Glacier Bay National Park & Preserve
PO Box 140, Gustavus, AK 99826 

10 )  Iñupiat Heritage Center (): P.O Box 69, Barrow, AK 99723 

11 )  Katmai (National Park & Preserve): PO Box 7
1000 Silver Street, Building 603, King Salmon, AK 99613 

12 )  Kenai Fjords (National Park): PO Box 1727, Seward, AK 99664 

13 )  Klondike Gold Rush (National Historical Park): Klondike Gold Rush National Historical Park
P.O. Box 517, Skagway, AK 99840 

14 )  Kobuk Valley (National Park): PO Box 1029, Kotzebue, AK 99752 

15 )  Lake Clark (National Park & Preserve): PO Box 226, Port Alsworth, AK 99653 

16 )  Noatak (National Preserve): PO Box 1029, Kotzebue, AK 99752 

17 )  Sitka (National Historical Park): 103 Monastery St., Sitka, AK 99835 

18 )  World War II Valor in the Pacific (National Monument): National Park Service
WWII Valor in the Pacific National Monument
1845 Wasp Blvd. Bldg. 176, Honolulu, HI 96818 

19 )  Wrangell - St Elias (National Park & Preserve): Wrangell-St. Elias National Park & Preserve
PO Box 439
Mile 106.8 Richardson Highway, Copper Center, AK 99573 

20 )  Yukon - Charley Rivers (National Preserve): P.O. Box 167, Eagle, AK 99738


3. When prompted to enter a new command, type “nearby 2” and this will give us an indexed list of all the nearby places (within 10 kilometers) to the second national site returned from “list ak” 
The code returned should look like this:

Places near  Alaska Public Lands ,  

1 )  Anchorage 

2 )  Hilton Anchorage 

3 )  Westmark Anchorage Hotel 

4 )  Hotel Captain Cook 

5 )  Sheraton Anchorage Hotel & Spa 

6 )  SpringHill Suites by Marriott Anchorage Midtown 

7 )  Homewood Suites by Hilton Anchorage 

8 )  The Lakefront Anchorage 

9 )  Courtyard by Marriott Anchorage Airport 

10 )  Crowne Plaza Anchorage-Midtown 

11 )  SpringHill Suites by Marriott Anchorage University Lake 

12 )  Americas Best Value Inn and Suites Airport 

13 )  Lake Hood Seaplane Base 

14 )  Anchorage Downtown Hotel 

15 )  Inlet Tower Hotel & Suites 

16 )  Residence Inn by Marriott Anchorage Midtown 

17 )  Historic Anchorage Hotel 

18 )  Hampton Inn Anchorage 

19 )  Anchorage Grand Hotel 

20 )  Northeast Anchorage


4. When prompted to enter a new command, type “map” and this will open a new window in your web browser that displays a map in Plotly that shows all the nearby sites returned from “nearby 2”
If you hover over each location, the text will show you the name of that specific site, as well as the coordinates of that site.

