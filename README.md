# Home Assistant Custom Bluteooth Tracker 


## Introduction 

The following repo is a simple python3 script that works as a bluetooth tracker on home assistant. This was made since I wasn't able to find a reliable platform that was able to get me location tracking and let my home assistant know when i was home or away without any false triggers. This script is optimezed to know exactly when you are home and away, and can be tuned to avoid any false away notifcations. 

What the script does is it initializes a thread that keeps track of your bluetooth device. If there are any false scans that don't discover the device, it will wait for a period of attempts before marking your device as away. You can simply modify the variables in the config files to suit your needs, but the current values should already be good enough. 

The script should work with any bluetooth device. 

In addition to tracking whether the device is available when a bluetooth scan is made from a raspberry pi, this script can also can connect to some bluetooth trackers. Currently I use the itag device which is a cheap bluetooth tracker that can be bought online for next to nothing. An image of the device is attached below. 

![alt text](https://img.grouponcdn.com/deal/bp7UEqswiaeiVTaBTbhi/n8-1666x1000/v1/c700x420.jpg)

This itag device is a cheap tracker that you do not need to charge for a few months, and in addition to help with location tracking it comes with a toggle button. The extra feature is the ability to customize what this button does, with any action on your home assistant. 

Currently the script only tracks one particular device, however if the ability to track more devices are needed, feel free to create an ISSUE and I can build it out when I find some time


## What You Need

1) You will require a raspberry pi with bluetooth. I currently use the same pi running home assistant in a python virtual environment. 

2) You will also need to run this as root or modify permissions to be able to use the bluetooth as any user on the pi   

## I am Running HASSIO 

If you are running hassio, I currently havent figured out how to make this an add-on due to some permission issues with the bluetooth driver in hassio. A current method of still being able to implement this would be installing this on a raspberry pi w , and when you reach step 9, simply change the config of your hassio and point it to your raspberry pi w's ip address 

## Installation: 


1) ``` sudo apt install bluetooth libbluetooth-dev pkg-config libboost-python-dev libboost-thread-dev libglib2.0-dev python-dev ```

2) ``` git clone https://github.com/araa47/hass_bletracker.git ```

3) ``` pip3 install flask bluepy requests ```

4) Identify the mac address of the device you want to track, you can run ```hcitool scan```

5) Now you can modify the config.py file and set the mac address of your device in that file. You can also modify threshold and scan_sleep_time, but this can be tuned later on if you have issues with the current values. If you are using a normal bluetooth device skip to step 7. 

6) If you are using an itag device you may want to enable itag to True, and also set the require home assistant url, password, and entity_id if you want to toggle your smart devices using the button on the itag. 

7) Run the program by typing in ``` sudo python3 app.py ```

8) This should start an api on port 5000 of your device. You can simply send requests to the following url to check whether the program is working ```pi_ip:5000/api/search/mac_addr ```, where pi_ip is the ip of your raspberry pi and mac_addr is the mac address of the device in the config file you are tracking. 

9) Now that the tracker is active, simple add the lines in the ```configuration.yaml``` file attached in this repo.  

10) Your device should show up on home assistant, enjoy!


## Notes 

If you are using the itag device and enabled pairing, when you walk out of range from the pi with the itag tacker, it will start beeping. This is pretty annoying right now, but seems to be a firmware feature on the itag so I havent been enable to disable this. If you are annoyed by this noise, you could aways open up the device and disconnect the buzzer. 

## Future Updates

Currently this script only supports tracking a single device, but it shouldn't be too difficult to add multiple device support. Will be adding this in once I get some more time. 






