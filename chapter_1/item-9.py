# Item 9 - Consider match for Destructuring in Flow Control; Avoid When if Statements Are Sufficient
print("\n Item 9 - Consider match for Destructuring in Flow Control; Avoid When if Statements Are Sufficient \n")

# NOTES - 
# 1. match is for Destructuring


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
print("take_if_action")
take_if_action("red")
take_if_action("yellow")
take_if_action("green")

# def take_match_action(light):
#     match light:
#         case "red":
#             print("STOP")
#         case "green":
#             print("GO")
#         case "yellow":
#             print("SLOW DOWN")
#         case _:
#             raise RuntimeError("Unfamilier light color...")

# take_match_action("red")
# take_match_action("yellow")
# take_match_action("green")

print("=" * 30)


# Do
print("DO : ")
import enum

class ColorEnum(enum.Enum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"

def take_enum_action(light):
    match light:
        case ColorEnum.RED:
            print("STOP")
        case ColorEnum.GREEN:
            print("GO")
        case ColorEnum.YELLOW:
            print("SLOW DOWN")
        case _:
            RuntimeError

print("take_enum_action")
take_enum_action(ColorEnum.RED)
take_enum_action(ColorEnum.GREEN)
take_enum_action(ColorEnum.YELLOW)
print("-" * 30)

print("match expression with deserialization...")

from dataclasses import dataclass
import json

record1 = """{"customer": {"last": "Ross", "first": "Bob"}}"""
record2 = """{"customer": {"entity": "Steve's Painting Co."}}"""

@dataclass
class PersonCustomer:
    first_name: str
    last_name: str

@dataclass
class BusinessCustomer:
    compnay_name: str
    
def deserialize(data):
    record = json.loads(data)

    match record:
        case {"customer": {"last": first_name, "first": last_name}}:
            return PersonCustomer(first_name=first_name, last_name=last_name)
        case {"customer": {"entity": company_name}}:
            return BusinessCustomer(compnay_name=company_name)
        case _:
            ValueError
            
print(deserialize(record1))
print(deserialize(record2))
print("=" * 30)
