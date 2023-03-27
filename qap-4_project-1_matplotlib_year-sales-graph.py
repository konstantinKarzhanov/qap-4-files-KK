# ---------------------------------------------------------------------------------------
# QAP-4. Project_2: Matplotlib. The Year Sales Graph
# ---------------------------------------------------------------------------------------
# The program allows the user to enter the total amount of sales 
# for each month from January to December and creates a graph of the total sales
# ---------------------------------------------------------------------------------------
# Author: Kostiantyn Karzhanov
# Date: March 23, 2023
# =======================================================================================

# ------------------------
# Import required modules
# ------------------------
from matplotlib import pyplot as plt
import calendar

# ---------------------------
# Declare required functions
# ---------------------------
def msgInvalid(valueName, invalidValue) :
# The function returns message for "invalid situations"
    return f"\nSorry, the \"{valueName}\" is not valid. You entered: \"{invalidValue}\""


def msgTryAgain(valueToLeave = "END") :
# The function returns message for "try again situations"
    return f"Please, try again or type \"{valueToLeave}\" to leave the program\n"


def leaveIfEnd(valueToCheck) :
# The function checks if the input is "END" and exits the program if so, or returns the "valueToCheck"
    if valueToCheck.upper() == "END" :
        print("\nCongrats, you have successfully left the program. Hope to see you soon!\n")
        exit()
    else :
        return valueToCheck


def checkFloat(valueName, valueToCheck) :
# The function checks whether the given value ("valueToCheck") is a number, and if it is, returns it as a floating point number, if not, returns "None"
    try :
    # Try to convert given value to Float type
        valueToCheck = float(valueToCheck)
    except :
    # In case value cannot be converted to Float type show the message
        if valueToCheck == "" :
        # if "valueToCheck" is an empty string show the warning message
            print(f"\nSorry the \"{valueName}\" cannot be empty")
        else :
            print(msgInvalid(valueName, valueToCheck))
    else :
    # Return floating point number 
        return valueToCheck


# --------------------------
# Declare required constants
# --------------------------
MONTHS = calendar.month_name[1:]
CURRENCY = "$"

# Assign lists for graph data
xMonth = []
yAmount = []

# -------------------------
# Main program starts here
# -------------------------
while True :
    # Repeat the loop until "END" is entered
    # Assign a flag ("outerFlag") that will be used to stop ("STOP") the program at any point and display the graph after there is enough data
    outerFlag = False

    for month in MONTHS :
    # Repeat the loop for each element of the list "MONTHS"
        while True :
        # Repeat the loop until the last element in the list is reached or user enters "STOP" or "END"
            inputValue = leaveIfEnd(input(f"Please enter the sales amount for \"{month}\" (\"STOP\" to display the graph, \"END\" to exit):\n"))
            if inputValue.upper() == "STOP" and len(yAmount) > 1 :
            # If the user entered "STOP" and there are at least two elements in the "yAmount" list, re-assign the flag "outerFlag" and exit the loop
                outerFlag = True
                break
            elif inputValue.upper() == "STOP" and len(yAmount) <= 1 :
            # If the user entered "STOP" but there is not enough data in the "yAmount" list, show the warning message and repeat the loop
                print(f"\nSorry, there is not enough data to display yet. Must have at least 2 values ({2 - len(yAmount)} left)")
                # Show "Try Again Message" and repeat the loop
                print(msgTryAgain())
                continue
            
            # Check if the input value ("inputValue") can be converted to a number, and if so, return it as a floating point number, if not, return "None"
            amountOfSales = checkFloat("sales amount", inputValue)

            if amountOfSales is not None :
            # If "amountOfSales" is a positive number, add it to the list "yAmount" also add the first three characters of the "month" as a new element to the list "xMonth"
                if amountOfSales > 0 :
                    xMonth.append(month[:3])
                    yAmount.append(amountOfSales)
                    # Break the loop and go to the next iteration of the outer loop   
                    break        
                elif amountOfSales == 0 :
                # If "amountOfSales" is equal to "0" make some additional checks before proceed
                    while True :
                        # Check if the user is sure about their input
                        inputValue = input(f"Are you sure the sales amount is \"{amountOfSales}\"? (\"Y\" for \"Yes\" or \"N\" for \"No\"):\n")

                        if inputValue == "" :
                        # if "inputValue" is an empty string show the warning message
                            print("\nSorry the option cannot be empty")
                        elif inputValue.upper() == "Y" :
                        # Check if the user wants to see zero sales in their final graph
                            while True :
                                inputValue = input(f"Do you wanna see \"{amountOfSales}\" on the graph? (\"Y\" for \"Yes\" or \"N\" for \"No\"):\n")

                                if inputValue == "" :
                                # if "inputValue" is an empty string show the warning message
                                    print("\nSorry the option cannot be empty")
                                elif inputValue.upper() == "Y" :
                                # If the answer is "Yes" add zero value to the list "yAmount" also add the first three characters of the "month" as a new element to the list "xMonth"
                                    xMonth.append(month[:3])
                                    yAmount.append(amountOfSales)
                                    # Break the loop and go to the next iteration of the outer loop
                                    break
                                elif inputValue.upper() == "N" :
                                # If the answer is "No" - break the loop and go to the next iteration of the outer loop
                                    break
                                else :
                                # In case user entered something different show the warning message and repeat the loop
                                    print(msgInvalid("option", inputValue))

                                print("Please, try again\n")

                            # Assign a flag ("flag") that will be used to exit the outer loop and proceed to the next iteration
                            flag = True
                            break

                        elif inputValue.upper() == "N" :
                        # Assign a flag ("flag") that will be used to repeat the outer loop asking the user to enter the sales amount for the same "month"
                            flag = False
                            break
                        else :
                        # In case user entered something different show the warning message and repeat the loop
                            print(msgInvalid("option", inputValue))

                        print("Please, try again\n")
                    
                    if flag :
                    # If flag value is "True" exit the outer loop and proceed to the next iteration
                        break
                    elif not flag : 
                    # If flag value is "False" repeat the outer loop asking the user to enter the sales amount for the same "month"
                        continue
                else :
                # If user entered a negative value for the sales amount "amountOfSales" show the warning message and repeat the loop
                    print(msgInvalid("sales amount", inputValue))

            # Show "Try Again Message" and repeat the loop
            print(msgTryAgain())
        
        # If the user entered "STOP" and there are at least two elements in the "yAmount" list stop the loop and display the graph based on the values entered
        if outerFlag :
            break
    
    # Create a title for the graph
    plt.title("The Year Sales Graph")
    # Draw the graph based on the data in the lists "xMonth" and "yAmount"
    plt.plot(xMonth, yAmount, color='magenta', marker='o', label="Sales")

    # Create a label for the x-axis
    plt.xlabel("Month")
    # Create a label for the y-axis
    plt.ylabel(f"Total Sales ({CURRENCY})")
    # Draw the grid for our graph
    plt.grid(True)
    # Create a legend for our graph line
    plt.legend()
    # Display the graph
    plt.show()

    # Ask the user if they want to leave the program or continue with a new data
    leaveIfEnd(input("\nPress any key to start with new data, or type \"END\" to leave the program:\n"))
    # If the user chooses to continue, clear the lists from previous data and repeat the loop
    del xMonth[:]
    del yAmount[:]