# UOCIS322 - Project 4 #
Author: Kaetlyn Gibson
Contact Address: kaetlyng@uoregon.edu

## Overview
RUSA ACP Brevet controle time calculator, re-implemented with Flask and AJAX.

### Background
What are brevets? Brevets are timed rides with controls. Controls are points where a rider must obtain proof of passage, and controle times are the minimum and maximum times by which the rider must arrive at the location.

### The Algorithm
To calculate the opening time, we divide the distance of the control point(in km) by the maximum speed(in km/hr) designated by the location of the control. To calculate the closing time, we divide the distance of the control point(in km) by the minimum speed(in km/hr) designated by the location of the control.

### Time Calculation
Dividing the distance in kilometers by speed of kilometers per hour results in a time
in hours. To convert into hours and minutes, subtract the whole number of hours and multiply the resulting fractional part by 60. Times are rounded to the nearest minute.

### An Example, for Further Clarification


## Tasks
- Implemented the logic in acp_times.py based on the algorithm linked above.
- Edited the template and Flask app so that the required remaining arguments were passed along.
- Constructed an automated "nose" test suite for the project using test cases created from using the website.

## Usage


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.

The algorithm, described by RUSA: https://rusa.org/pages/acp-brevet-control-times-calculator
The original calculator: https://rusa.org/octime_acp.html
Additional background: https://rusa.org/pages/rulesForRiders
