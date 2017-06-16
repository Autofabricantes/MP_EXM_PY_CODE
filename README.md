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

sudo apr-get update

numpy
-----
sudo apt-get install python-numpy

adafruit neopixel
-----------------
sudo apt-get install build-essential python-dev git scons swig
git clone https://github.com/jgarff/rpi_ws281x.git
sudo python -m pip install rpi_ws281x


------------------------------------------
- Setting python3 as default interpreter -
------------------------------------------
Setting python3 as default interpreter
https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux

