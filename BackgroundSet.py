import requests, ctypes, datetime, sys
from random import randint

SPI_SETDESKWALLPAPER = 20

#note: save your backgrounds in this folder, named [weather]x.jpg x being number of rand range.
BACKGROUND_PATH = r'C:\Users\Katherine\Documents\_Python Projects\Set_Background\\'

API_KEY = #Your API Key Here
API_ADDRESS='http://api.openweathermap.org/data/2.5/weather?q='
LOCATION = '77584,us' #Your zipcode. 
BACKGROUNDS = ['Rain','Thunderstorm','Clouds','Drizzle','Clear','Other'] #Common weather patterns.

def set_wallpaper(format_data):
    
    SET_BACKGROUND = BACKGROUNDS[-1]
    
    timestamp = datetime.datetime.now().time()    
    if format_data in BACKGROUNDS: 

        if timestamp >datetime.time(18,1) or timestamp < datetime.time(6,0):
            SET_BACKGROUND = format_data+str(randint(3,4))
        else:
            SET_BACKGROUND = format_data+str(randint(1,2))
    else:
            SET_BACKGROUND = 'Other'+str(randint(1,4))
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, BACKGROUND_PATH + SET_BACKGROUND +'.jpg', 3)
    return 0 
    
def main(argv):
    
    json_data = requests.get(API_ADDRESS + LOCATION + API_KEY).json()
    format_data = json_data['weather'][0]['main']
    print('Looped')
    
    set_wallpaper(format_data)
    print(format_data)
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv))