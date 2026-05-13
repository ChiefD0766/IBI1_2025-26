#set total students number to 91
#set initial infected number to 5
#set growth rate to 0.4
#day = 1
#while infected number is smaller than total students number, calculate new infections for the next day:
#  infected number*(1+growth rate)
#  day+1
#  print day and infected number
#print the final day numbers
total_students = 91
initial_infected = 5
growth_rate = 0.4
infected = initial_infected
day = 1
print("Day",day,infected,"infected students")
while infected < total_students:
    infected = round(infected*(1+growth_rate))
    day += 1
    print("Day",day,infected,"infected students")

print("All students are infected after",day,"days.")