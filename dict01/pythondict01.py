#!/usr/bin/python3

switch = {"hostname": "sw1", "ip": "10.0.0.0", "version": "1.2", "vendor": "cisco"}

print( switch["hostname"] )

print( switch["ip"] )

print( "First test - .get()" )
print( switch.get("lynx") )

print( "Second test - .get()" )
print( switch.get("lynx", "The KEY IS IN ANOTHER CASTLE!") )

print( "Third test - .get()" )
print( switch.get("version") )

print( "Fourth test - .keys()" )
print( switch.keys() )

print( "Fifth test - .values()" )
print( switch.values() )

print( "Sixth test - .pop()" )
switch.pop("version")
print( switch.keys() )
print( switch.values() )

print( "Seventh test - ADD a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print( switch.values() )

print( "Eight test - ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print( switch.values() )
