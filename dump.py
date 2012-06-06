#!/usr/bin/env python

# http://www.gpspassion.com/forumsen/topic.asp?TOPIC_ID=77262

import sys
import struct
from pprint import pprint

epsilon = 1.1920929e-07

ifp = open(sys.argv[1])

header = ifp.read(24)

print 'header:', " ".join(['%02X' % ord(b) for b in header])

while True:
    rec = ifp.read(13)

    if not rec:
        print "all done"
        break

    ## Byte 03H~00H: Longitude
    ##     Signed HEX value, multiple Epsilon to get longitude value. Epsilon = 1.1920929E-07
    ## 
    ## Byte 07H~04H: Latitude
    ##     Signed HEX value, multiple Epsilon to get latitude value. Epsilon = 1.1920929E-07
    ## 
    ## Byte 08H: Speed Limit
    ##     HEX value in MPH
    ## 
    ## Byte 09H: Camera Type
    ##     00H: Fixed 
    ##     01H: Mibile
    ##     02H: Section
    ##     03H: Built-in (Traffic)
    ##     04H: Redlight (Traffic2)
    ## 
    ## Byte 0BH & 0AH: Camera Direction and Camera Angle
    ##     Bit0 of 0BH and Bit7~0 of 0AH
    ##         Camera Angle. Valid value: 000H~167H (0~359). 0:North, 90: East.
    ##
    ##     Bit2 and Bit1 of 0BH
    ##         Camera Direction. 
    ##          00B: Single direction, according to Miomap manual, it should be traffic direction, not camera facing direction.
    ##          01B: Bi-direction
    ##          11B: All direction 
    ##          10B: All direction 
    ##     
    ##     Bit7~bit3 of 0BH
    ##         Seems like not used or reserved.
    ## 
    ## Byte 0CH: Flag
    ##     00H: New Record
    ##     01H: Deleted Record, when record is deleted, byte 08~0B will be set to 00.
    ##     02H: Edited Record 

    lon, lat, speed_limit, camera_type, dir_and_angle, flag = struct.unpack('<iiBBhB', rec)

    lat *= epsilon
    lon *= epsilon

    if camera_type == 0:
        camera_type = "fixed"
    elif camera_type == 1:
        camera_type = "mobile"
    elif camera_type == 2:
        camera_type = "section"
    elif camera_type == 3:
        camera_type = "built-in (traffic)"
    elif camera_type == 4:
        camera_type = "red light (traffic2)"
    else:
        camera_type = "unknown (%02X)" % camera_type

    direction = dir_and_angle & 0b111111111
    dir_and_angle = dir_and_angle >> 9

    angle = dir_and_angle & 0b11

    if angle == 0b00:
        angle = "single direction"
    elif angle == 0b01:
        angle = "bi-direction"
    elif angle in (0b11, 0b10):
        angle = "all direction"
    else:
        angle = "unknown"

    data = {
        'latitude' : lat,
        'longitude' : lon,
        'speed_limit' : speed_limit,
        'camera_type' : camera_type,
        'direction' : direction,
        'angle' : angle,
        'flag' : flag,
    }

    pprint(data)

