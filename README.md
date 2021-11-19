#RPi-IO

This script was created to allow a viable solution to using an On/Off Button with a Raspberry Pi. 

This is fully compatable with the Raspberry Pi Zero W and any other RPi with the same pinout. 
It is confirmed compatable with Raspbian/Debian as of 11/18/2021. 



Install Instructions:

The button should be wired to GPIO 3(pin 5) and any ground but pin 6 right across from GPIO 3 grants better 
cable managment and I can vouch that this set up works

In Termincal type 

                  sudo git clone www.https://github.com/BashPink/RPi-IO

                  cd RPi-IO
                  
                  sudo bash install
                             
In some cases, the start script will post an internal error. So it may be necessary to use the command [sudo /etc/init.d/shutdown-listener.sh].
You can test the pins to see if the command above is needed. 

Please report any issues. I'd be happy to look into them!
