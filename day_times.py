def day_times():
    return "morning", "afternoon", "evening", "night"

times = day_times()
print(times)
print(type(times))

a,b,c,d = day_times()
print("Trzeci element to %s" %c)