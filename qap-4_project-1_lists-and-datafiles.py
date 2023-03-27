# ---------------------------------------------------------------------------------------
# QAP-4. Project_1: The One Stop Insurance Company
# ---------------------------------------------------------------------------------------
# The program allows the user to enter the appropriate information 
# and calculate new insurance policy for its customers
# ---------------------------------------------------------------------------------------
# Author: Kostiantyn Karzhanov
# Date: March 22, 2023
# =======================================================================================

# ------------------------
# Import required modules
# ------------------------
import datetime
import atexit
import re

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


def currencyFormat(value, decimals = 2, currency = "$", tcomma = True) :
# The function transforms the incoming value into the currency format
    if tcomma :
        return "{2}{0:,.{1}f}".format(value, decimals, currency)
    else :
        return "{2}{0:.{1}f}".format(value, decimals, currency)


def readDefaultsFile(fileName, separator = False, calibrationValue = 2) :
# The function reads data from the file and returns it in a form of a list or tuple
    # The lists where the data will be added
    listDataNames =[]
    listData = []

    # Open the file with Context Manager in read mode
    with open(fileName, "r") as fhandle :
        # Read all lines from the file
        lines = fhandle.readlines()

        startIndex = 0
        # If we specified separator, re-assign startIndex based on separator's position
        if separator :
            for line in lines :
                startIndex = line.find(separator)
                listDataNames.append(line[: startIndex].rstrip())
                listData.append(line[(startIndex + calibrationValue) :].rstrip())
        else :
        # Grab data from each line starting from index 0
            for line in lines :
                listData.append(line[startIndex :].rstrip())

    # Based on the length of "listDataNames", return a tuple with lists ("listDataNames" and "listData") OR just return list "listData"
    if len(listDataNames) > 0 :
        return listDataNames, listData
    else :
        return listData


def updateDefaultsFile(fileName, listData, listDataNames = False, separator = " = ") :
# The function writes the data in a specified file (fileName)
    # Open the file with Context Manager in write mode
    with open(fileName, "w") as fhandle :
        # If list with variable names ("listDataNames") was specified, write the data to a file in the specified format
        if listDataNames :
            for i in range(len(listDataNames)) :
                fhandle.write(f"{listDataNames[i]}{separator}{listData[i]}\n")
        else :
        # Write all the data from "listData" list to a file in the specified format
            for i in range(len(listData)) :
                fhandle.write(f"{listData[i]}\n")

        # Show a message after the information has been written to the file
        message = f"The file \"{fileName}\" was updated"

        print("*" * len(message))
        print(f"{message}")
        print("*" * len(message))
        print()


def modifyStrRegExp(origStr, rawRegExp, replaceStr = "") :
# The function modifies the initial string by replacing the specified characters with "replaceStr"
    # create a regular expression object using "rawRegExp" pattern
    regexObject = re.compile(rf"{rawRegExp}")
    # return modified string
    return regexObject.sub(replaceStr, origStr)


def validateUsingList(valueName, valueToCheck, listName) :
# The function checks if the value ("valueToCheck") is in the list ("listName") or returns "None"
    if valueToCheck in listName :
        return valueToCheck
    else :
        print(msgInvalid(valueName, valueToCheck))


def checkCharNum(valueName, valueToCheck, highCharNum, lowCharNum = 1) :
# The function checks whether the length of the given value ("valueToCheck") is within the specified range or returns "None"
    if valueToCheck == "" :
    # if "valueToCheck" is an empty string show the warning message
        print(f"\nSorry the \"{valueName}\" cannot be empty")
    elif lowCharNum <= len(valueToCheck) <= highCharNum :
    # if the length is within the specified range return the value
        return valueToCheck
    else :
    # if the length is NOT within the specified range, show a warning message
        if lowCharNum == highCharNum :
            print(f"\nSorry, the \"{valueName}\" must be \"{highCharNum}\" characters long. You entered \"{len(valueToCheck)}\"")
        else :
            print(f"\nSorry, the \"{valueName}\" must be from \"{lowCharNum}\" to \"{highCharNum}\" characters long. You entered \"{len(valueToCheck)}\"")


def checkValidDigit(valueName, valueToCheck) :
    # The function checks if the given value ("valueToCheck") contains only digits and returns it if it is or returns "None" if it is not
    if valueToCheck.isdigit() :
        return valueToCheck
    else :
    # Show the warning message if not
       print(msgInvalid(valueName, valueToCheck))


def getAcceptedSet(format = False) :
# The function returns a certain set of accepted characters depending on the "format" given
    if not format or format == "A-z'- .#0-9" :
        return set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- .#0123456789")
    elif format == "A-z'- ." :
        return set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- .")
    elif format == "A-z'-" :
        return set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
    else :
        return set(format)


def checkValidFormat(valueName, valueToCheck, format = False) :
    # The function checks if the given value ("valueToCheck") is valid based on the specified "format"

    # "getAcceptedSet" returns a certain set of accepted characters depending on the specified "format"
    acceptedChar = getAcceptedSet(format)

    if set(valueToCheck).issubset(acceptedChar) :
    # If "valueToCheck" has a valid format return this value
        return valueToCheck 
    else :
    # Show the warning message if not
        print(msgInvalid(valueName, valueToCheck))


def checkInteger(valueName, valueToCheck) :
# The function checks if a given value ("valueToCheck") is an Integer number and returns it if it is or returns "None" if it is not
    try :
    # Try to convert given value to an Integer type
        valueToCheck = int(valueToCheck)
    except :
    # In case value cannot be converted to an Integer type show the message
        if valueToCheck == "" :
        # if "valueToCheck" is an empty string show the warning message
            print(f"\nSorry the \"{valueName}\" cannot be empty")
        else :
            print(msgInvalid(valueName, valueToCheck))
    else :
        return valueToCheck


def checkRange(valueName, valueToCheck, highRangeNum, lowRangeNum = 0) :
# The function checks if a given value ("valueToCheck") is in the given range and returns it if it is or returns "None" if it is not
    if lowRangeNum <= valueToCheck <= highRangeNum :
        return valueToCheck
    else :
    # Show the warning message if not
        print(f"\nSorry, the \"{valueName}\" must be from {lowRangeNum} to {highRangeNum}. You entered: \"{valueToCheck}\"")


def checkOption(valueName, valueToCheck, listOptions) :
# The function checks if the entered option is in the list of possible options and returns it if it is or returns "None" and shows the message if it is not
    if valueToCheck == "" :
    # if "valueToCheck" is an empty string show the warning message
        print(f"\nSorry the \"{valueName}\" cannot be empty")
    elif valueToCheck in listOptions :
    # If "valueToCheck" is in the list of possible options return it
        return valueToCheck
    else :
    # Show the warning message if not
        print(msgInvalid(valueName, valueToCheck))


# --------------------------
# Declare required constants
# --------------------------
DATE_INVOICE = datetime.date.today()
DATE_NEXT_PAYMENT = datetime.date(DATE_INVOICE.year, DATE_INVOICE.month + 1, 1)
FILE_DEFAULTS = "OSICDef.dat"
FILE_OUTPUT = "Policies.dat"
LIST_CONSTANTS = readDefaultsFile(FILE_DEFAULTS, "=")

# Declare constants for output structure
HEADER_COMPANY = "The One Stop Insurance Company"
LINE_BORDER = "=" * 38
LINE_BORDER_TITLE = "<>" * (len(HEADER_COMPANY) // 2)
LINE_MAIN = "-" * 38
LINE_TOTAL_SUM = "-" * 10

if type(LIST_CONSTANTS) == tuple :
# Get constants from the file and assign variables/constants for later use if the type of "LIST_CONSTANTS" is tuple
    idPolicy = int(LIST_CONSTANTS[1][0])
    RATE_BASIC_PREMIUM = float(LIST_CONSTANTS[1][1])
    DISCOUNT_ADD_CARS = float(LIST_CONSTANTS[1][2])
    RATE_EXT_LIAB = float(LIST_CONSTANTS[1][3])
    RATE_GLASS = float(LIST_CONSTANTS[1][4])
    RATE_LOAN_CAR = float(LIST_CONSTANTS[1][5])
    RATE_HST = float(LIST_CONSTANTS[1][6])
    RATE_PROC_FEE_MP = float(LIST_CONSTANTS[1][7])
    THRESHOLD_NUM_MON_PAYMENTS = int(LIST_CONSTANTS[1][8])
    THRESHOLD_EXT_LIAB = float(LIST_CONSTANTS[1][9])
    THRESHOLD_NUM_CARS_INSURED = int(LIST_CONSTANTS[1][10])
    LIST_PROVINCES = modifyStrRegExp((LIST_CONSTANTS[1][11]), "[\"\[ \]\']").split(",")

    # Use atexit module to register a function that will run before leaving the program
    atexit.register(updateDefaultsFile, FILE_DEFAULTS, LIST_CONSTANTS[1], LIST_CONSTANTS[0])
else :
# Get constants from the file and assign variables/constants for later use if the type of "LIST_CONSTANTS" is list
    idPolicy = int(LIST_CONSTANTS[0])
    RATE_BASIC_PREMIUM = float(LIST_CONSTANTS[1])
    DISCOUNT_ADD_CARS = float(LIST_CONSTANTS[2])
    RATE_EXT_LIAB = float(LIST_CONSTANTS[3])
    RATE_GLASS = float(LIST_CONSTANTS[4])
    RATE_LOAN_CAR = float(LIST_CONSTANTS[5])
    RATE_HST = float(LIST_CONSTANTS[6])
    RATE_PROC_FEE_MP = float(LIST_CONSTANTS[7])
    THRESHOLD_NUM_MON_PAYMENTS = int(LIST_CONSTANTS[8])
    THRESHOLD_EXT_LIAB = float(LIST_CONSTANTS[9])
    THRESHOLD_NUM_CARS_INSURED = int(LIST_CONSTANTS[10])
    LIST_PROVINCES = modifyStrRegExp((LIST_CONSTANTS[11]), "[\"\[ \]\']").split(",")

    # Use atexit module to register a function that will run before leaving the program
    atexit.register(updateDefaultsFile, FILE_DEFAULTS, LIST_CONSTANTS)

# -------------------------
# Main program starts here
# -------------------------
while True :
# Repeat the loop until the user enters "END"
    while True :
    # Repeat the loop until the user enters a valid "Customer Name"
        custFN = leaveIfEnd(input("Please enter the customer first name (Accepted characters: \"A-z'-\") (\"END\" to exit):\n"))
        # Check if the length of "custFN" is within the specified range or return "None" 
        custFN = checkCharNum("customer first name", custFN, 15)

        if custFN :
        # Check if "custFN" is valid based on the "format" given
            custFN = checkValidFormat("customer first name", custFN, "A-z'-")

            if custFN : 
            # If "custFN" is valid make it "Title Case" and exit the loop
                custFN = custFN.title()
                break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid "Customer Last Name"
        custLN = leaveIfEnd(input("Please enter the customer last name (Accepted characters: \"A-z'-\") (\"END\" to exit):\n"))
        # Check if the length of "custLN" is within the specified range or return "None" 
        custLN = checkCharNum("customer last name", custLN, 14)

        if custLN :
        # Check if "custLN" is valid based on the "format" given
            custLN = checkValidFormat("customer last name", custLN, "A-z'-")

            if custLN :
            # If "custLN" is valid make it "Title Case" and exit the loop
                custLN = custLN.title()
                break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid "Street"
        custStreet = leaveIfEnd(input("Please enter the customer street address (Accepted characters: \"A-z'- .#0-9\") (\"END\" to exit):\n"))
        # Check if the length of "custStreet" is within the specified range or return "None" 
        custStreet = checkCharNum("customer street address", custStreet, 30)

        if custStreet :
        # Check if "custStreet" is valid based on the "format" given
            custStreet = checkValidFormat("customer street address", custStreet, "A-z'- .#0-9")

            if custStreet : 
            # If "custStreet" is valid make it "Title Case" and exit the loop
                custStreet = custStreet.title()
                break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid "City"
        custCity = leaveIfEnd(input("Please enter the customer city (Accepted characters: \"A-z'- .\") (\"END\" to exit):\n"))
        # Check if the length of "custCity" is within the specified range or return "None"
        custCity = checkCharNum("customer city", custCity, 19)

        if custCity :
        # Check if "custCity" is valid based on the "format" given
            custCity = checkValidFormat("customer city", custCity, "A-z'- .")

            if custCity :
            # If "custCity" is valid make it "Title Case" and exit the loop
                custCity = custCity.title()
                break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid "Province"
        custProvince = leaveIfEnd(input(f"Please enter the customer province ({', '.join(LIST_PROVINCES)}) (\"END\" to exit):\n"))
        # Check if the length of "custProvince" is within the specified range or return "None"
        custProvince = checkCharNum("customer province", custProvince, 2, 2)

        if custProvince :
        # Make "custProvince" "Upper Case" and check if it is valid based on the given list "LIST_PROVINCES"
            custProvince = custProvince.upper()
            if validateUsingList("customer province", custProvince, LIST_PROVINCES) :
            # If "custProvince" is valid exit the loop
                break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid "Postal Code"
        custPostalInp = leaveIfEnd(input("Please enter the customer postal code (In format: \"L9L9L9\") (\"END\" to exit):\n"))
        # Check if the length of "custPostalInp" is within the specified range or return "None"
        custPostal = checkCharNum("customer postal code", modifyStrRegExp(custPostalInp, "[() -]"), 6, 6)

        if custPostal :
        # Make "custPostal" "Upper Case" and check if it is valid based on the "format" given
            custPostal = custPostal.upper()

            flag = False
            # Loop over the characters of the "custPostal" and check if the evens are letters and the odds are digits
            for i in range(len(custPostal)) :
                if i % 2 == 0 and not custPostal[i].isalpha() :
                    break
                elif i % 2 != 0 and not custPostal[i].isdigit() : 
                    break
                
                # Change "flag" to "True" if the end of the loop is reached
                if i == (len(custPostal) - 1) :
                    flag = True
            
            if flag :
            # End the infinite loop if "flag" is "True" (which means "custPostal" is a valid "Postal Code")
                break
            elif not flag :
            # If "flag" is "False" - show "INVALID" message
                print(msgInvalid("customer postal code", custPostalInp))

        # Show "Try Again Message" and repeat the loop        
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid "Phone number"
        custPhone = leaveIfEnd(input("Please enter the customer phone number (10 digits) (\"END\" to exit):\n"))
        # Check if the length of "custPhone" is within the specified range or return "None"
        custPhone = checkCharNum("customer phone number", modifyStrRegExp(custPhone, "[() -]"), 10, 10)

        if custPhone :
        # Check if "custPhone" contains only digits
            custPhone = checkValidDigit("customer phone number", custPhone)

            if custPhone :
            # If "custPhone" is valid exit the loop
                break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid "Number Of Cars Being Insured"
        numCarsInsured = leaveIfEnd(input("Please enter the number of cars being insured (\"END\" to exit):\n"))
        # Check if "numCarsInsured" is a valid Integer number
        numCarsInsured = checkInteger("number of cars", numCarsInsured)

        if numCarsInsured is not None :
        # If "numCarsInsured" is a valid Integer number, check if it is in the specified range
            numCarsInsured = checkRange("number of cars", numCarsInsured, THRESHOLD_NUM_CARS_INSURED, 1)
            if numCarsInsured is not None :
            # If "numCarsInsured" is in the specified range exit the loop
                break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid option for "Extra Liability"
        optionExtLiab = leaveIfEnd(input(f"Add an option for extra liability up to {currencyFormat(THRESHOLD_EXT_LIAB, 0)}? (\"Y\" for \"Yes\" or \"N\" for \"No\") (\"END\" to exit):\n")).upper()
        # Check if "optionExtLiab" is in the list of possible options
        optionExtLiab = checkOption("extra liability option", optionExtLiab, ["Y", "N"])

        if optionExtLiab :
        # if "optionExtLiab" is a valid option assign required variables and exit the loop
            coverageExtLiab = 0
            if optionExtLiab == "Y" :
                coverageExtLiab = RATE_EXT_LIAB * numCarsInsured
                
            break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid option for "Glass Coverage"
        optionGlass = leaveIfEnd(input(f"Add an option for glass coverage? (\"Y\" for \"Yes\" or \"N\" for \"No\") (\"END\" to exit):\n")).upper()
        # Check if "optionGlass" is in the list of possible options
        optionGlass = checkOption("glass coverage option", optionGlass, ["Y", "N"])

        if optionGlass :
        # if "optionGlass" is a valid option assign required variables and exit the loop
            coverageGlass = 0
            if optionGlass == "Y" :
                coverageGlass = RATE_GLASS * numCarsInsured

            break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid option for "Loaner Car"
        optionLoanCar = leaveIfEnd(input(f"Add an option for loan car? (\"Y\" for \"Yes\" or \"N\" for \"No\") (\"END\" to exit):\n")).upper()
        # Check if "optionLoanCar" is in the list of possible options
        optionLoanCar = checkOption("loan car option", optionLoanCar, ["Y", "N"])

        if optionLoanCar :
        # if "optionLoanCar" is a valid option assign required variables and exit the loop
            coverageLoanCar = 0
            if optionLoanCar == "Y" :
                coverageLoanCar = RATE_LOAN_CAR * numCarsInsured

            break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    while True :
    # Repeat the loop until the user enters a valid option for "Payment Type"
        optionPaymentType = leaveIfEnd(input(f"Please enter the type of payment (\"F\" for \"Full\" or \"M\" for \"Monthly\") (\"END\" to exit):\n")).upper()
        # Check if "optionPaymentType" is in the list of possible options
        optionPaymentType = checkOption("payment type option", optionPaymentType, ["F", "M"])

        if optionPaymentType :
        # if "optionPaymentType" is a valid option assign required variables and exit the loop
            monthlyPayment = 0
            if optionPaymentType == "M" :
                monthlyPayment = RATE_PROC_FEE_MP

            break

        # Show "Try Again Message" and repeat the loop
        print(msgTryAgain())

    # --------------------------------------
    # All required calculations starts here
    # --------------------------------------
    insurancePremium = RATE_BASIC_PREMIUM + ((numCarsInsured - 1) * ((1 - DISCOUNT_ADD_CARS) * RATE_BASIC_PREMIUM))
    totalExtraCost = coverageExtLiab + coverageGlass + coverageLoanCar
    totalInsurance = insurancePremium + totalExtraCost
    hst = RATE_HST * totalInsurance
    totalCost = hst + totalInsurance

    if monthlyPayment > 0 :
        monthlyPayment += totalCost / THRESHOLD_NUM_MON_PAYMENTS

    # ----------------------------------------
    # Format variables for better output look
    # ----------------------------------------
    # Assign formatting variables for a better output look
    custFullNameDsp = "{0} {1}".format(custFN, custLN)
    custCPPDsp = "{0}, {1} {2}".format(custCity, custProvince, custPostal)
    custPhoneDsp = "({0}){1}-{2}-{3}".format(custPhone[:3], custPhone[3:6], custPhone[6:8], custPhone[8:])

    # Assign variables based on a ternary operator's condition
    optionExtLiabDsp = ("yes" if optionExtLiab == "Y" else "no").title()
    optionGlassDsp = ("yes" if optionGlass == "Y" else "no").title()
    optionLoanCarDsp = ("yes" if optionLoanCar == "Y" else "no").title()

    # Change the output look of currency related variables
    thresholdExtLiabDsp = "{}:".format(currencyFormat(THRESHOLD_EXT_LIAB, 0))
    insurancePremiumDsp = "{}".format(currencyFormat(insurancePremium))
    totalInsuranceDsp = "{}".format(currencyFormat(totalInsurance))
    hstPercDsp = "({:.0%}):".format(RATE_HST)
    hstDsp = "{}".format(currencyFormat(hst))
    totalCostDsp = "{}".format(currencyFormat(totalCost))

    # Change the output look of date variable to desired one
    dateInvoiceDsp = "{}".format(DATE_INVOICE.strftime("%d-%b-%Y"))

    # ------------------------------
    # Show the output on the screen
    # ------------------------------
    print()
    print(f"{LINE_BORDER :<38s}")
    print()
    print(f"{LINE_BORDER_TITLE :^38s}")
    print(f"{HEADER_COMPANY :^38s}")
    print(f"{LINE_BORDER_TITLE :^38s}")
    print()
    print(f"{LINE_MAIN :<38s}")
    print(" Customer:")
    print()
    print(f"    {custFullNameDsp :<30s}")
    print(f"    {custStreet :<30s}")
    print(f"    {custCPPDsp :<30s}")
    print()
    print(f"    Phone: {custPhoneDsp :<14s}")
    print()
    print(f"{LINE_MAIN :<38s}")
    print(" Cars Insured #:", " " * 17, f"{numCarsInsured :>2d}")
    print()
    print(f" Extra Liab. up to {thresholdExtLiabDsp :<11s}    {optionExtLiabDsp :>3s}")
    print(f" Glass Coverage:                  {optionGlassDsp :>3s}")
    print(f" Loaner Car Coverage:             {optionLoanCarDsp :>3s}")
    print()
    print(f"{LINE_MAIN :<38s}")
    print(f" Insurance Premium:         {insurancePremiumDsp :>9s}")
    print()

    if coverageExtLiab > 0 :
    # Show the "Ex. Liab. Coverage" amount only in case "coverageExtLiab" > 0
        # Change the output look of currency related variable
        coverageExtLiabDsp = "{}".format(currencyFormat(coverageExtLiab))
        # Show the output on the screen
        print(f" Ex. Liab. Coverage:        {coverageExtLiabDsp :>9s}")

    if coverageGlass > 0 :
    # Show the "Glass Coverage" amount only in case "coverageGlass" > 0
        # Change the output look of currency related variable
        coverageGlassDsp = "{}".format(currencyFormat(coverageGlass))
        # Show the output on the screen
        print(f" Glass Coverage:              {coverageGlassDsp :>7s}")

    if coverageLoanCar > 0 :
    # Show the "Loaner Car Coverage" amount only in case "coverageLoanCar" > 0
        # Change the output look of currency related variable
        coverageLoanCarDsp = "{}".format(currencyFormat(coverageLoanCar))
        # Show the output on the screen
        print(f" Loaner Car Coverage:         {coverageLoanCarDsp :>7s}")

    print(f"{LINE_TOTAL_SUM :>37s}")
    print(f" Total Insurance Premium:  {totalInsuranceDsp :>10s}")
    print(f" HST{hstPercDsp :<6s}                  {hstDsp :>9s}")
    print(f"{LINE_TOTAL_SUM :>37s}")
    print(f" Total Cost:               {totalCostDsp :>10s}")
    print()
    print(f"{LINE_MAIN :<38s}")
    print()
    print(f" Invoice Date:            {dateInvoiceDsp :>11s}")
    print()

    if monthlyPayment > 0 :
    # Show "Monthly Payment" and "Next Payment Date" only in case "monthlyPayment" > 0
        # Change the output look of currency related variable
        monthlyPaymentDsp = "{}".format(currencyFormat(monthlyPayment))
        # Change the output look of date variable to desired one
        dateNextPaymentDsp = "{}".format(DATE_NEXT_PAYMENT.strftime("%d-%b-%Y"))

        print(f" Monthly Payment:           {monthlyPaymentDsp :>9s}")
        print(f"{LINE_TOTAL_SUM :>37s}")
        print(f" Next Payment Date:       {dateNextPaymentDsp :>11s}")
        print()

    print(f"{LINE_BORDER :<38s}")
    print()

    # -----------------------
    # Write data to the file
    # -----------------------
    # Open the file with Context Manager in write (appending) mode
    with open(FILE_OUTPUT, "a") as fhandle :
    # Write the data to the file in desired format
        fhandle.write("{}, ".format(idPolicy))
        fhandle.write("{}, ".format(DATE_INVOICE))
        fhandle.write("{}, ".format(custFN))
        fhandle.write("{}, ".format(custLN))
        fhandle.write("{}, ".format(custStreet))
        fhandle.write("{}, ".format(custCity))
        fhandle.write("{}, ".format(custProvince))
        fhandle.write("{}, ".format(custPostal))
        fhandle.write("{0}-{1}-{2}, ".format(custPhone[:3], custPhone[3:6], custPhone[6:]))
        fhandle.write("{}, ".format(numCarsInsured))
        fhandle.write("{}, ".format(optionExtLiab))
        fhandle.write("{}, ".format(optionGlass))
        fhandle.write("{}, ".format(optionLoanCar))
        fhandle.write("{}, ".format(optionPaymentType))
        fhandle.write("{:.2f}".format(totalInsurance))
        fhandle.write("\n")

        # Show a message after the information has been written to the file
        message = "Policy information processed and saved"

        print("*" * len(message))
        print(f"{message}")
        print("*" * len(message))
        print()

    # Increment "idPolicy" for future invoices
    idPolicy += 1

    # Re-assign the value of the constant "ID_POLICY" in the tuple or list to the new value "idPolicy"
    if type(LIST_CONSTANTS) == tuple :
        LIST_CONSTANTS[1][0] = idPolicy
    elif type(LIST_CONSTANTS) == list :
        LIST_CONSTANTS[0] = idPolicy