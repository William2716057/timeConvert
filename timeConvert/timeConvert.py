from datetime import datetime
import pytz 

#function that will retrieve correct country timezone
def TimeToCountry(currentTime, country):
    try:
        countryTimezones = pytz.country_timezones[country]
        if countryTimezones:
            countryTimeZone = pytz.timezone(countryTimezones[0]) 
        else:
            return "No timezone found for this country code"
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
        
