import time

print("Hello! Welcome to Who has the Highest Overall Software by Vraj Bhavsar")

time.sleep(2)
print("  ")

# Ask user for how many students are getting their average calculated
how_many_students = int(input("Before we begin, How many students are there?: "))

num_of_assignments = int(input("How many evaulations do you wish to input? "))

# These variables store the value on who will get the highest average
highest_avg = 0
highest_avg_name = ""

# This code below is a loop where it takes the name of the student and asks for their 5 Computer Science Marks
for i in range(how_many_students):
    total_sum = 0
    name = input("Name of student? " + "#" + str(i + 1) + ": " )
    for i in range(num_of_assignments):
        one_student = float(input("Evalution Mark (%) " + "#" + str(i + 1) + ": "))
        total_sum += one_student 
        
    
        
# This code below finds the average of the marks and identify's who has the highest with what average
    avg = total_sum / num_of_assignments
    if avg > highest_avg:
        highest_avg = avg
        highest_avg_name = name
    print("Average: " + str(round(avg, 1)) + "%")

#This code below prints the name of the student with the highest average
print("The highest average is " + str(highest_avg) + "%" + " obtained by " + str(highest_avg_name + "!" ))