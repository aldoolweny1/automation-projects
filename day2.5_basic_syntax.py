def speeding_ticket(speed):
    if speed >= 85:
        ticket = "Reckless Driving"
    elif speed > 65 and speed < 85:
        ticket = "Speeding"
    else:
        ticket = "Safe"
    return ticket


print(speeding_ticket(87)) # Should print Reckless Driving
print(speeding_ticket(66)) # Should print Speeding
print(speeding_ticket(65)) # Should print Safe
print(speeding_ticket(85)) # Should print Reckless Driving
print(speeding_ticket(35)) # Should print Safe
print(speeding_ticket(77)) # Should print Speeding