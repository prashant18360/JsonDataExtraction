# Name - Prashant
# Roll No.- 2018360
# Section - B
# Group - 1
# September 8, 2018

import urllib.request
import datetime

'''function to get weather response
   in which API KEY and location pass the arguement
   it decode the json data and return it'''
def weather_response(location, API_key):
	q=location
	api='http://api.openweathermap.org/data/2.5/forecast?'
	api_url=api+'q='+location+'&'+'APPID='+API_key
	x=urllib.request.urlopen(api_url)
	y=x.read().decode()
	return (y)

'''function to check for valid response
    in which it find the 'name' string index
    using of its index string slicing of location and checked it'''
def has_error(location,json):
	i=json.find("name")
	m=json.find(",",i)
	s=json[i+7:m-1]
	if(s==location):
		return False
	else:
		return True			

'''function to get temperature on nth day
   in which firstly find date and time and find its index
   using of this index find "temp" index and then slicing of temp value and return it''' 
def get_temperature (json, n,t):
	y=datetime.date.today()
	date=y+datetime.timedelta(days=n)
	z=str(date) + ' ' + t
	k=json.find(z)
	p=json.rfind('"temp":',0,k)
	r=json.find(",",p)
	temp=float(json[p+7:r])
	return temp

'''function to get humidity on nth day
   in which firstly find the date and time and find its index
   using of this index , find "humidity" index and then slicing of humidity value and return it'''
def get_humidity(json, n,t):
        y=datetime.date.today()
        date=y+datetime.timedelta(days=n)
        z=str(date) + ' ' + t
        k=json.find(z)
        p=json.rfind('humidity',0,k)
        r=json.find(",",p)
        hum=float(json[p+10:r])
        return hum

'''function to get pressure on nth day
   in which firstly find the date and time and find its index
   using of this index , find "pressure" index and then slicing of pressure value and return it'''
def get_pressure(json, n,t):
        y=datetime.date.today()
        date=y+datetime.timedelta(days=n)
        z=str(date) + ' ' + t
        k=json.find(z)
        p=json.rfind('pressure',0,k)
        r=json.find(",",p)
        press=float(json[p+10:r])
        return press

'''function to get wind speed on nth day
   in which firstly find the date and time and find its index
   using of this index , find "wind" index and then slicing of wind speed value and return it'''
def get_wind(json, n,t):
        y=datetime.date.today()
        date=y+datetime.timedelta(days=n)
        z=str(date) + ' ' + t
        k=json.find(z)
        p=json.rfind('speed',0,k)
        r=json.find(",",p)
        wind_speed=float(json[p+7:r])
        return wind_speed

'''function to get sea level on nth day
   in which firstly find the date and time and find its index
   using of this index , find "sealevel" index and then slicing of sea level value and return it'''
def get_sealevel(json, n,t):
        y=datetime.date.today()
        date=y+datetime.timedelta(days=n)
        z=str(date) + ' ' + t
        k=json.find(z)
        p=json.rfind('sea_level',0,k)
        r=json.find(",",p)
        slevel=float(json[p+11:r])
        return slevel
	
if __name__ == '__main__':
        print(weather_response("Delhi","0cc45578355cd14c6be10b9dac81b283"))
        print('Temperature=',get_temperature(weather_response("Delhi","0cc45578355cd14c6be10b9dac81b283"),n=0,t="18:00:00"))
        print('Humidity=',get_humidity(weather_response("Delhi","0cc45578355cd14c6be10b9dac81b283"),n=0,t="18:00:00"))
        print('Pressure=',get_pressure(weather_response("Delhi","0cc45578355cd14c6be10b9dac81b283"),n=0,t="18:00:00"))
        print('Wind speed=',get_wind(weather_response("Delhi","0cc45578355cd14c6be10b9dac81b283"),n=0,t="18:00:00"))
        print('Sea level=',get_sealevel(weather_response("Delhi","0cc45578355cd14c6be10b9dac81b283"),n=0,t="18:00:00"))
        print(has_error('London',weather_response("London","0cc45578355cd14c6be10b9dac81b283")))
