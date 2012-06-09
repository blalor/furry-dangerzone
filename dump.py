#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.gpspassion.com/forumsen/topic.asp?TOPIC_ID=77262

import sys
import struct

from pprint import pprint

epsilon = 1.1920929e-07

## only the ones found during discovery
CAMERA_TYPES = {
    # 0x00 : "fixed",
    # 0x01 : "mobile",
    # 0x02 : "section",
    # 0x03 : "built in (traffic)",
    # 0x04 : "red light (traffic2)",

    0x44 : "red light camera",

    0xc0 : "speed camera",
    0xc1 : "mobile speed camera",
    0xc2 : "built-in speed camera",
    0xc6 : "railway crossing",
    0xc7 : "bus lane camera",
    0xc8 : "high accident zone",
    0xc9 : "school zone",
    0xca : "town entry point",
    0xcb : "red light and speed",
    0xcc : "toll booth",
    0xcd : "hospital, ambulance",
    0xce : "fire station",
    0xcf : "congestion charge zone",

    0xdf : "dangerous area",

    0xe3 : "average speed camera",
}

MAX_CAM_LENGTH = max(len(CAMERA_TYPES[x]) for x in CAMERA_TYPES)

CAMERA_DIRECTIONS = {
    0b00 : "single direction",
    0b01 : "bi direction",
    0b10 : "all directions",
    # 0b11 : "all directions",
}

MAX_CAM_DIR = max(len(CAMERA_DIRECTIONS[x]) for x in CAMERA_DIRECTIONS)

ifp = open(sys.argv[1])

while True:
    header = ifp.read(16)
    # print 'header:', " ".join(['%02X' % ord(b) for b in header])

    rec = ifp.read(21)
    # print 'rec:', " ".join(['%02X' % ord(b) for b in rec])

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

    unk, index, lon, lat, speed_limit, camera_type, dir_and_angle, flag = struct.unpack('<4siiiBBhB', rec)

    lat *= epsilon
    lon *= epsilon

    speed_limit *= 0.621371192

    if camera_type in CAMERA_TYPES:
        camera_type = CAMERA_TYPES[camera_type]
    else:
        camera_type = "unknown (%02X)" % camera_type

    direction = dir_and_angle & 0b111111111
    dir_and_angle = dir_and_angle >> 9

    angle = dir_and_angle & 0b11

    if angle in CAMERA_DIRECTIONS:
        angle = CAMERA_DIRECTIONS[angle]
    else:
        angle = "unknown (%02X)" % angle

    elements = [
        ('unk',         " ".join(['%02X' % ord(b) for b in unk])),
        ('index',       index),
        ('lon',         lon),
        ('lat',         lat),
        ('speed_limit', speed_limit),
        ('camera_type', camera_type),
        ('direction',   direction),
        ('angle',       angle),
        ('flag',        flag),
    ]

    # pprint(elements)
    # 0,42.4041785,-71.1102913,40,speed camera,62,bi-direction,0,169,65251

    formats = {
        'index'       : '%3d',
        'lat'         : '%11.7f',
        'lon'         : '%12.7f',
        'speed_limit' : '%3d',
        'camera_type' : ('%%-%ds' % MAX_CAM_LENGTH),
        'direction'   : u'%3d°',
        'angle'       : ('%%-%ds' % MAX_CAM_DIR),
        'flag'        : '%3d',
        'unk'        : '"%s"',
    }


    format_str = " | ".join([formats[x[0]] for x in elements])
    # print format_str
    # print [data[x] for x in elements]
    print (format_str % tuple([x[1] for x in elements])).encode("utf-8")

