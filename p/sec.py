# Python Table negerator



# table  no
Value = 2

# table end no
End_value = 50

# Generate Table
print("------------! Table Generator !-------------")

print("Table of {} from {} to {}".format(Value, Value, End_value))

while True:
    print("2 X {} = {}".format(Value, Value))
    Value = Value + 2
    if Value > End_value:
        break