import re

bci_rules = [
    {"value": "First_Time_Buyer", "condition": "Yes"},
    {"value": "Age", "condition": ">40"},
    {"value": "OEM_Loyalty_Program", "condition": "Yes"},
    {"value": "CIBIL_Score", "condition": ">650"},
    {"value": "Down_Payment", "condition": ">100000"},
    {"value": "Special_Occasions", "condition": "Wedding/Festival"},
    {"value": "Needs_Match", "condition": "Medium/High"},
    {
        "value": "Add_Ons",
        "condition": "Extended Warranty; Floor Mats; Upgraded Sound System",
    },
    {"value": "Dealership_Engagement", "condition": "Medium/High"},
    {"value": "Experience_With_Sales_Rep", "condition": "Positive"},
    {"value": "Delivery_Date_Status", "condition": "On-Time"},
    {"value": "Customer_Satisfaction_Score", "condition": ">6"},
]

def evaluate_condition(value, condition):
    isMathOperator = condition[0] in ['>', '<', '>=', '<=']
    conditions = re.split(r'[><\/;]', condition)
    if isinstance(value, str) and len(conditions) == 1 and conditions[0] == value:
        return True
    elif isinstance(value, str) and len(conditions) > 0 and value in conditions[0:]:
        return True
    elif isMathOperator:
        try:
            num_value = int(value)
            if ">" in condition:
                return num_value > int(conditions[1])
            elif "<" in condition:
                return num_value < int(conditions[1])
            elif ">=" in condition:
                return num_value >= int(conditions[1])
            elif "<=" in condition:
                return num_value <= int(conditions[1])
        except ValueError:
            return False
    return False