"""
7.you live 4 miles from university.
the bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
how long will the bus journey take? Alternatively, you could run to university. you jog the first miles at 7mph;
 then run the next two at 15mph;before jogging the last at 7 mph again.
 will this be slower or quicker then the bus?
"""
distance_uni_miles = 4
min_taken = 60
distance_covered_bus = 25
one_miles = 60/25
four_miles = one_miles*4
stops = 10
time_stops = 10*2
bus_journey= four_miles + time_stops


firstlast_miles_covered = 60/7
remaining_two_covered = 60/15
min_taken_on_foot = firstlast_miles_covered + remaining_two_covered
unit = min_taken_on_foot<bus_journey
if unit:
    print(f'  it takes {min_taken_on_foot} minutes so jogging is quicker')
else:
    print(f'it takes {bus_journey} minutes on bus so bus ride is faster')



