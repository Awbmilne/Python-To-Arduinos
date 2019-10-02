# 
# This program is a basic outline of interaction between
# a Python Script and an Arduino.
# 
# The Basics of this Protocol can be expanded upon by
# setting up seperate serial ports for each Arduino and 
# andressing them each sequentially.
# 


import serial                                   # Serial Setup for Python, Must install library on computer ```pip install pySerial```
import time                                     # Allow for pauses (not neccesary in this code, short puases included in API code)
import ArduinoSetup as Arduino                  # API Library for WatLock Arduino Commands


# LIST OF ARDUINOS
#Arduino.Arduino_List.append(["SERIAL_PORT_NAME"    , "SERIAL_#_OF_ARDUINO"     , ""])
 Arduino.Arduino_List.append(["Testduino"           , "85735313033351409161"    , ""]) 
 

#NECCESARY SETUP FOR SERIAL OBJECTS
Arduino.match_Arduinos()                                            # Locate Arduinos based on Serial Number
for a in Arduino.Arduino_List:
    exec (a[0] + " = Arduino.create_serial('" + a[2] + "', 9600)")  # Create Serial Objects for each Arduino in the list
for a in Arduino.Arduino_List:
    exec ("Arduino.start_serial(" + a[0] + ")")                     # Start Each Serial Interface


#---------------------------------------------------------------------------------------------------------------------------------
#MAIN COMMAND LOOP

# This loop just repeatedly sends 3 different commands,
# the First being a data request, where the arduino just sends back data
# the Second being a command, where the arduino must receive a string command and then reply
# the Third being another command, could serve any purpose (possibly return the arduino information)

while (True): #Run Forever

    # Data request Command
    
    data_from_arduino = Testduino.get_data()
    print (data_from_arduino)
    
    # Command to send String Command
    
    reply_from_arduino = Testduino.send_command("Test Command")
    print (reply_from_arduino)
                

    #Extra third command for example
    
    reply_from_other = Testduino.other_command()
    print (reply_from_other)


    #time.sleep(1)                             # Pause so the terminal doesnt fill instantly (only needed for testing)
#---------------------------------------------------------------------------------------------------------------------------------   
    