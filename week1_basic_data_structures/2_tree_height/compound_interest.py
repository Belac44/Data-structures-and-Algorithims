def days_to_target(principle, interest, target):
    assert(interest > 0)
    
    days = 1

    while  principle < target:
        principle = principle * (1+interest/100)
        days += 1
    return (days, principle)

results = days_to_target(1000, 2, 1000000)
print("Its takes ", results[0], "days to get to ", results[1] )