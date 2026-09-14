print("How many seconds ?")
second = int(input())
minute = second//60
second = second%60
hour = minute//60
minute = minute%60
print(str(hour) + " hour(s), " + str(minute) + " minute(s), " +str(second) + " second(s)")