#######################
# MP_EXM_PY_CODE #
#######################

----------------------
- Paths organization -
----------------------
   
    |-- README.md
    |-- autofabricantes.py --
    |-- constants.py --------
    |-- pid.py
    |-- state.py ------------    
    |-- transition.py -------
    |-- statemachine.py -----    
    `-- ioutils.py ----------


----------------------------
- Installing additional libraries -
------------------------------------
sudo apt-get update
sudo apt-get install python-pip build-essential python-dev git

adafruit neopixel
-----------------
sudo apt-get install scons swig
git clone https://github.com/jgarff/rpi_ws281x.git
sudo python -m pip install rpi_ws281x

MCP3008
-------
sudo apt-get install python-smbus
sudo pip install adafruit-mcp3008

PCA9685
-------
sudo pip install adafruit-pca9685

------------------------------------------
- Setting python3 as default interpreter -
------------------------------------------
Setting python3 as default interpreter
https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux

------------------------------------------
- Enable I2C
------------------------------------------
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
http://www.runeaudio.com/forum/how-to-enable-i2c-t1287.html
