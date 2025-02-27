# UOCIS322 - Project 4 #
Author: Kaetlyn Gibson

Contact Address: kaetlyng@uoregon.edu

## Overview
RUSA ACP Brevet controle time calculator, re-implemented with Flask and AJAX.

### Background
What are brevets? Brevets are timed rides with controls. Controls are points where a rider must obtain proof of passage, and controle times are the minimum and maximum times by which the rider must arrive at the location.

### The Algorithm
To calculate the opening time, we divide the distance of the control point(in km) by the maximum speed(in km/hr) designated by the location of the control. To calculate the closing time, we divide the distance of the control point(in km) by the minimum speed(in km/hr) designated by the location of the control. Of course, it is slightly more complicated than this, so I recommend taking a look at the examples from here: https://rusa.org/pages/acp-brevet-control-times-calculator.

### Time Calculation
Dividing the distance in kilometers by speed of kilometers per hour results in a time
in hours. To convert into hours and minutes, subtract the whole number of hours and multiply the resulting fractional part by 60. Times are rounded to the nearest minute.

## Tasks
- Implemented the logic in acp_times.py based on the algorithm linked.
- Edited the template and Flask app so that the required remaining arguments were passed along.
- Constructed an automated "nose" test suite for the project using test cases created from using the website.

## Usage
- Build the image: 
  ```
  docker build -t kaetlyng-cis322-4 .
  ```
- Run the container (specify a free port)
  ```
  docker run -d -p port:5000 kaetlyng-cis322-4
  ```
- To run tests:
  - Jump into container (specify the container id):
    ```
    docker exec -it YOUR_CONTAINER_ID /bin/bash
    ```
  - While in the container, run the tests using command `nosetests`
- To use the brevet calculator:
  - Launch `http://hostname:port` using web browser
  - Choose a brevet distance
  - Choose begin date and time
  - Enter controle locations in km or miles
  - Watch, as the results appear!

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.

The algorithm, described by RUSA: https://rusa.org/pages/acp-brevet-control-times-calculator

The original calculator: https://rusa.org/octime_acp.html

Additional background: https://rusa.org/pages/rulesForRiders
