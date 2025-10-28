# Item 9 - Consider match for Destructuring in Flow Control; Avoid When if Statements Are Sufficient
print("\n Item 9 - Consider match for Destructuring in Flow Control; Avoid When if Statements Are Sufficient \n")

# Vehicle assistant program that reacts to a traffic light’s color.

# Don't
print("DON'T : ")
def take_if_action(light):
    if light == "red":
        print("STOP")
    elif light == "green":
        print("GO")
    elif light == "yellow":
        print("SLOW DOWN")
    else:
        raise RuntimeError("Unfamilier light color...")

take_if_action("red")
take_if_action("yellow")
take_if_action("green")

def take_match_action(light):
    match light:
        case "red":
            print("STOP")
        case "green":
            print("GO")
        case "yellow":
            print("SLOW DOWN")
        case _:
            raise RuntimeError("Unfamilier light color...")

take_match_action("red")
take_match_action("yellow")
take_match_action("green")

print("=" * 30)

    
