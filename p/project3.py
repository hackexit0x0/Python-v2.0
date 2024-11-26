## Result Calculation Program

# Dictionary to store marks for different subjects
Subject = {"Math": 0, "Physics": 0, "Chemistry": 0, "Biology": 0, "English": 0}

# Function to calculate the percentage and determine result status
def Percentage():
    # Calculate total percentage from marks in all subjects
    TotalPercentage = (Subject["Math"] + Subject["Physics"] + Subject["Chemistry"] + Subject["Biology"] + Subject["English"]) / 5
    
    # Determine and display the result status based on the percentage
    if TotalPercentage < 56:
        print("Result Status: :( Fail")
    elif TotalPercentage < 75:
        print("Result Status: :) Average")
    elif TotalPercentage < 90:
        print("Result Status: :) Good")
    elif TotalPercentage <= 100:  # Ensure the percentage is within valid range
        print("Result Status: :) Excellent")
    
    # Display the total percentage of the student
    print("Total Percentage: " + str(TotalPercentage) + "%")

# Function to take user input for marks and validate the input
def UserDataInput(UserName):
    for subject in Subject:

            # Prompt user for marks for each subject
            Subject[subject] = int(input(f"Enter {subject} marks: "))
            
            # Check if marks are within the valid range (0-100)
            if Subject[subject] < 0 or Subject[subject] > 100:
                print("Error: Enter marks between 0 to 100 only.")
                exit()  # Stop execution if invalid marks are entered
    
    # Print the name of the student
    print("Student Name: " + UserName)

# Main loop to handle user input and process results
while True:
    # Prompt user to enter a student's name or exit the program
    UserName = input("Enter Student Name (or type 'EXIT' to quit): ")
    
    # Check if the user wants to exit the program
    if UserName.upper() == "EXIT":
        print("Exiting the program. Goodbye!")
        break
    
    # Collect user data and calculate the result
    UserDataInput(UserName)
    Percentage()
