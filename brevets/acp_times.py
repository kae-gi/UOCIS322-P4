"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

def convert_to_hrs_and_min(time):
    hours = time // 1 # get whole hour
    minutes =  round((time-hours)*60) # round to nearest whole minute
    return hours, minutes

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    first = 200/34
    second = 200/32
    third = 200/30
    times = {'200': first, '400': first+second, '600': first+second+third}
    # checking: did control_dist_km exceed within 20%/meet brevet_dist_km?
    if brevet_dist_km<control_dist_km<=(brevet_dist_km*1.2):
        # response: yes, adjust accordingly
        return open_time(brevet_dist_km, brevet_dist_km, brevet_start_time)
    else:
        # response: no, continue
        if control_dist_km <= 200: # control location 0 to 200km
            time_shift = control_dist_km/34
        elif control_dist_km <= 400: # control location 200 to 400km, 300 falls here
            time_shift = times['200'] + (control_dist_km-200)/32
        elif control_dist_km <= 600: # control location 400 to 600km
            time_shift = times['400'] + (control_dist_km-400)/30
        elif control_dist_km <= 1000: # control location 600 to 1000km
            time_shift = times['600'] + (control_dist_km-600)/28
        converted_time_shift = convert_to_hrs_and_min(time_shift)
        return brevet_start_time.shift(hours=converted_time_shift[0], minutes=converted_time_shift[1])


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    fixed_times = {'200':13.5, '300':20, '400':27, '600': 40, '1000': 75}
    # checking: did control_dist_km exceed within 20%/meet brevet_dist_km?
    if brevet_dist_km<control_dist_km<=(brevet_dist_km*1.2):
        # response: yes, adjust accordingly
        return close_time(brevet_dist_km, brevet_dist_km, brevet_start_time)
    else:
        # response: no, continue
        # => Time limit for a control within the first 60km is based on 20 km/hr, plus 1 hour.
        if control_dist_km < 60: # control location <60km from start
            time_shift = 1 + (control_dist_km/20)
        # => Beyond 60km, the standard algorithm applies.
        elif control_dist_km <= 600: # control location 60 to 600km
            # checking: control_dist_km meets exact brevet distances
            # also which brevet distance
            if control_dist_km == 200 and brevet_dist_km==200:
                # response: the fixed time. Continued for values below.
                time_shift = fixed_times['200']
            elif control_dist_km == 300 and brevet_dist_km==300:
                time_shift = fixed_times['300']
            elif control_dist_km == 400 and brevet_dist_km==400:
                time_shift = fixed_times['400']
            elif control_dist_km == 600 and brevet_dist_km==600:
                time_shift = fixed_times['600']
            else:
                time_shift = control_dist_km/15
        elif control_dist_km > 600: # control location 600 to 1000km
            # checking: control_dist_km meets exact brevet distance
            if control_dist_km == 1000 and brevet_dist_km==1000:
                # response: the fixed time
                time_shift = fixed_times['1000']
            else:
                time_shift = 600/15 + (control_dist_km-600)/11.428
        converted_time_shift = convert_to_hrs_and_min(time_shift)
        return brevet_start_time.shift(hours=converted_time_shift[0], minutes=converted_time_shift[1])
