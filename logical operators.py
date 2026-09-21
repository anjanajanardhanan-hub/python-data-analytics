# LOGICAL OPERATORS
# | Operator | Meaning                             |
# | -------- | ----------------------------------- |
# | `and`    | Both conditions must be true        |
# | `or`     | At least one condition must be true |
# | `not`    | Reverses the result                 |


# and
a = 10
if a == 10 and a > 5:
    print("ok")

# or
a = 15
if a > 10 or a == 0:
    print("yes")

# not
a = 10
if not a > 15:
    print("yes")
