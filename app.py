################
# Python3 script for tracking bluetooth devices 
# Creates a rest endpoint for home-assistant to check whether you are home or not 
# Also contains and add on to toggle your lights with the button on itag if paired (may work with other ble tags with buttons, still to test)
################
from flask import Flask
from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import time 
import _thread 
import requests
import config 


# flask init 
app = Flask(__name__)




# for scanning device 
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        return()

    # for handling when itag button is pressed 
    def handleNotification(slef, cHandle, data):
        print(data, cHandle, slef)
        try:
            requests.post(config.url, json = {"entity_id": config.entity_id}, headers = {"x-ha-access": config.hassPasswd, "Content-Type": "application/json"})
            print("Lights toggled")
        except Exception as e:
            print(e)    


# global vars 
status_counter = 0
status = "home"


# return the status 
@app.route('/api/search/<string:mac_addr>', methods=['GET'])
def device_scan(mac_addr):
    global status 
    return status


# handle errors 
@app.errorhandler(404)
def not_found(error):
    return("Not Found ", error)


# This is the code that is used to connect to itag
def tracker_connect(addr):
    try:
        # try to connect
        dev = Peripheral()
        dev.connect(addr)
        print("coneccted")

        # Once connected enable notification handling and loop through 
        dev.setDelegate(ScanDelegate())
        while True: 
            dev.waitForNotifications(10)

        dev.disconnect()
        print("Disconnected!")
    # if fail, go back to scanning, or if diconnects
    except Exception as e:
        print(e)



# scan for the device 
def device_scanner(treshold, scan_sleep_time):
    global status_counter
    global status 
    addr = config.bleAddr
    while True:
        # run the scanner 
        scanner = Scanner().withDelegate(ScanDelegate())
        devices = scanner.scan(5.0)
        found = False
        # if device in the list set status_counter to threshold (since if its home, it cant be false detection)
        for dev in devices:
            if dev.addr == addr:
                status_counter = treshold
                found = True

        # else subtract 1 from it, since we dont mind if the away automation takes time, this gives us room for failure to detect devices
        if found == False:
            status_counter = status_counter - 1
      
        # now set global vars if home      
        if status_counter >= treshold:
            status_counter = treshold 
            status = "home"
      
        # now set global vars if not dectected for -treshold value (away)
        if status_counter <= -treshold: 
            status_counter = -treshold
            status = "away"
        print("Device Status: ", status, "Current Value:", status_counter)
        # if its an itag device and its home, try to connect 
        if config.itag == True:
            # if home, try to connect to device 
            if (status_counter == treshold) & (status=="home"):
                tracker_connect(addr)

        # sleep 
        time.sleep(scan_sleep_time)

# run the thread 
_thread.start_new_thread(device_scanner, (config.threshold, config.scan_sleep_time))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)


