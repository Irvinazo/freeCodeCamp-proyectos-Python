def add_time(start, duration, starting_day = 0):

    """
    First, we split the start time s.t. we have 
    the strings for the starting hour, the starting 
    minute and the AM or PM time individually. We have to split
    multiple times
    """
    #Starting wiht the start hour
    start_hour_AMPM = start.split()
    start_hour_min = start_hour_AMPM[0].split(':')

    start_AMPM = start_hour_AMPM[1]
    start_hour = start_hour_min[0]
    start_min = start_hour_min[1]

    #Now we do the same for the duration time
    duration_hour_min = duration.split(':')
    duration_hour = duration_hour_min[0]
    duration_min = duration_hour_min[1]

    """
    Once we have the strings for hours and minutes from start and
    duration time, we will use congruences to get the current time
    """
    #We use a 60 min congruence with time 
    final_minute = (int(start_min) + int(duration_min)) % 60

    final_min_hours = (int(start_min) + int(duration_min)) // 60

    # We use a 12 hour congruence to count how many 'mid-days' have passed  since the starting hour. But we must take care when they input a 12 start hour: we don't say "It's 1:60" but we say "It's 12:30"
    #Thus, if the start hour is 12, we'll not count that 'mid-day' in how many mid-days have passed
    if start_hour =='12':
        mid_day_passed = (int(start_hour)+\
        int(duration_hour)+final_min_hours) // 12 -1

        final_hour = (int(start_hour)+\
        int(duration_hour)+final_min_hours) % 12

    else:
        mid_day_passed = (int(start_hour)+\
        int(duration_hour)+final_min_hours) // 12 

        final_hour = (int(start_hour)+\
        int(duration_hour)+final_min_hours) % 12

# Once we have the mid days passed for duration time, we have to calculate 
# if the sum of the starting hour and the duration time gives an AM or PM time
    if mid_day_passed % 2 == 0:
        string_final_part_day = start_AMPM

    elif start_AMPM =='AM':
        string_final_part_day = 'PM'

    else: 
        string_final_part_day = 'AM'

    #We have a little issue with the congruences: we don't say 'it's 0:30 AM/PM', we say 'it's 12:30 AM/PM' and to convert to string
    #Time to fix it:
    if final_hour == 0:
        final_hour = '12'

    else:
        final_hour = str(final_hour)    

    #Also if our minute is a single digit, we don't say 'it's 12:7 AM', we say 'it's 12:07 AM'. We take advantage of this 'if' and convert to string
    if len(str(final_minute)) == 1:
        final_minute = '0'+str(final_minute)

    else:
        final_minute = str(final_minute) 

    
    #Now we ensemble our strings.
    new_time = final_hour + ':' + final_minute + ' ' + string_final_part_day
    
    #Finally we have to differentiate between different cases depending on if the user inputs a starting day or not. By default, starting_day = 0 when no starting day is added to this function

    if starting_day == 0:
        if mid_day_passed == 0 or (mid_day_passed == 1 and start_AMPM =='AM'):
            return new_time

        elif (mid_day_passed == 1 and start_AMPM=='PM') or \
        mid_day_passed == 2 or (mid_day_passed == 3 and start_AMPM == 'AM'):
            new_time+=' (next day)'
            return new_time
        
        elif mid_day_passed % 2 == 1:
            if start_AMPM == 'PM':
                day = (mid_day_passed//2)+1
            else:
                day = (mid_day_passed//2)-1      
                   
            new_time+=f' ({day} days later)'
            return new_time

        elif mid_day_passed % 2 == 0 :
            day = (mid_day_passed//2)
            new_time+=f' ({day} days later)'
            return new_time

    else:
    #Now its time to work with the day of week string. We have to prepare it for a congruenve modulo 7 if the user input a day of the week
        days_of_week = ['sunday','monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday']
        week = {days_of_week[i]: i for i in range(0,7)}
        s_day = starting_day.lower()
        index_s_day = week[s_day]

        if mid_day_passed == 0 or (mid_day_passed == 1 and start_AMPM =='AM'):
            final_day = s_day.capitalize()
            new_time+=', ' +final_day
            return new_time

        elif (mid_day_passed == 1 and start_AMPM == 'PM') or mid_day_passed == 2 or (mid_day_passed == 3 and start_AMPM == 'AM'):
            index_final_day = (index_s_day +1)%7 
            final_day = days_of_week[index_final_day].capitalize()
            new_time+=', ' +final_day+' (next day)'
            return new_time

        elif mid_day_passed % 2 == 1:
            if start_AMPM == 'PM':
                day = (mid_day_passed//2)+1
            else:
                day = (mid_day_passed//2)-1

            index_final_day = (index_s_day + day)%7 
            final_day = days_of_week[index_final_day].capitalize()
            new_time+=', ' +final_day+f' ({day} days later)'
            return new_time

        elif mid_day_passed % 2 == 0:
            day = (mid_day_passed//2)
            index_final_day = (index_s_day + day)%7 
            final_day = days_of_week[index_final_day].capitalize()
            new_time+=', ' +final_day+f' ({day} days later)'
            return new_time