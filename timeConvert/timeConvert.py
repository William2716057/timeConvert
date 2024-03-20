from datetime import datetime
import pytz 

def TimeToCountry(currentTime, country):
        try:
            countryTimeZone = pytz.timezone(pytz.country_timezones[country[0]])
        except KeyError:
            return "Country not found"
        try:
            countryTime = currentTime.astimezone(countryTimeZone)
            return countryTime.strftime("%Y-%m-%d %H:%M:%S %z")
        except Exception as e:
            return f"Error converting time: {e}" 
        
if __name__ == "__main__":
     currentTime = datetime.now(pytz.utc) 
     country = input("Enter 2 letter country code").upper()
     converted = TimeToCountry(currentTime, country)
     print(f"Time in {country}: {converted}")
        
