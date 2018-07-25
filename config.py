# Please set all your variables here

################ Required !!! ##################################

# mac address of device to track (Required)
bleAddr = "00:A0:C9:14:C8:29"

# detection threshold to classify device as away (number of times device has to be scanned as away)
threshold = 3

# number of seconds to sleep between scans in seconds 
scan_sleep_time = 5 

################################################################

################ Optional ######################################

## set to True if you want to enable extra feature 
# the ability to use the botton on itag bluetooth tracker 
# to control a home assistant endpoint 
itag = True 

### Only need to fill in if itag is set to True

# the url you want to call if itag button is pressed 
url = "https://homeass.duckdns.org/api/services/light/toggle"

# the entity_id you want to call 
entity_id = "light.bedroom"

# your hass password 
hassPasswd = "password"


################################################################






