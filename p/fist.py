
# python Word Analysis

print("------------! Word Analysis !-------------")

User_data = ("Hsv","Boot","root")
brek_flow = "Hsv"

for User_input in User_data:
    if brek_flow != User_data:
        print("User Entred Word : {}".format(User_input))
        # Count len
        print("Word len size : {}".format(len(User_input)))
        # word Fist word
        print("Word Fist word : {}".format(User_input[0]))
        # word mid word
        midword = len(User_input) // 2
        print("Word Middle Word: {}".format(User_input[midword]))
        # word last word
        print("Word Last word : {}".format(User_input[-1]))
        print("Word Upper  : {}".format(User_input.upper()))
        print("Word Lower  : {}".format(User_input.lower()))
        
        print("\n")
    else:
        break


print("------------! Word Analysis Complete.. !-------------")


