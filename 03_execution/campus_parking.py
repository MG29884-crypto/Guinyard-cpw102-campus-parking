# use a named constant
# by using 2.0 as its value, it is automatically stored
COST_PER_HOUR = 2.0




def calculate_estimated_parking_cost(parked_hours):
    estimated_cost = parked_hours * COST_PER_HOUR
#define the main logic of my program
def main():

    #create a variable in which i will store user-entered parked hours
    # a bariable is named space in memory
    parked_hours = input("how many hours will you be / have you parked?")
    print(parked_hours)

    # call my main function and execute the logic of the program
main()