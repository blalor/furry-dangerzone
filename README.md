furry-dangerzone
================

Decoding the BRZ's SpeedcamUpdates.spud file

Output for the included `SpeedcamUpdates_all.spud` file, created via the nav interface in my '13 BRZ:

    unknown stuff | ind | longitude    | latitude    | mph | camera type            | hdg  | direction        | flg
    "A9 00 E3 FE" |   0 |  -71.1102913 |  42.4041785 |  24 | speed camera           |  62° | bi direction     |   0
    "BC 00 1C FE" |   1 | -120.8391270 |  47.0069925 |  55 | speed camera           | 330° | single direction |   0
    "BC 00 20 FE" |   2 | -119.8125005 |  47.1046144 |  55 | speed camera           | 270° | single direction |   0
    "BA 00 2E FE" |   3 | -116.3041691 |  46.6374018 |  55 | mobile speed camera    | 353° | single direction |   0
    "BD 00 42 FE" |   4 | -111.3264927 |  47.2690126 |  69 | built-in speed camera  |  83° | bi direction     |   0
    "BD 00 6D FE" |   5 | -100.6906284 |  47.2682344 |  55 | average speed camera   | 271° | all directions   |   0
    "BD 00 85 FE" |   6 |  -94.6026996 |  47.2982027 |  55 | red light camera       |   0° | bi direction     |   0
    "BC 00 9E FE" |   7 |  -88.2649151 |  47.0351089 |  18 | red light and speed    | 270° | bi direction     |   0
    "B4 00 EC FE" |   8 |  -68.8258975 |  45.1389467 |   5 | bus lane camera        | 336° | bi direction     |   0
    "AD 00 1D FE" |   9 | -120.5520634 |  43.4251367 |   5 | railway crossing       |   1° | bi direction     |   0
    "B0 00 4D FE" |  10 | -108.6715168 |  44.0249979 |   5 | high accident zone     | 326° | bi direction     |   0
    "B3 00 6A FE" |  11 | -101.3495182 |  44.7502329 |   5 | school zone            | 315° | bi direction     |   0
    "B1 00 95 FE" |  12 |  -90.6940998 |  44.4207269 |   5 | town entry point       |   0° | bi direction     |   0
    "AE 00 D0 FE" |  13 |  -75.9553531 |  43.5904733 |   5 | toll booth             |   7° | bi direction     |   0
    "9F 00 18 FE" |  14 | -121.8901906 |  39.9649965 |   5 | hospital, ambulance    |  14° | bi direction     |   0
    "A2 00 2B FE" |  15 | -117.0257115 |  40.5721475 |   5 | fire station           | 112° | bi direction     |   0
    "A0 00 40 FE" |  16 | -111.8880925 |  40.1893274 |   5 | congestion charge zone | 276° | bi direction     |   0
    "9B 00 58 FE" |  17 | -105.7931675 |  38.9828035 |   5 | dangerous area         | 308° | bi direction     |   0

The unknown stuff could be additional data, or a checksum?
