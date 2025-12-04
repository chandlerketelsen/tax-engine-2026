# 2025 Earned Income Tax Credit (EITC) - Simplified Model
# EITC is highly complex, this is a basic estimate for instructional use only.

def eitc_calc():
    """Provides a very simplified EITC estimate based on max values."""
    print("--- 2025 EITC Simplified ---")
    
    # Get user inputs
    try:
        earned_income = float(input("Earned Income: "))
        agi = float(input("Enter AGI: "))
        num_children = int(input("Children (0-3+): "))
    except ValueError:
        print("Invalid input.")
        return

    # Max EITC values (Approximate 2025 values)
    max_credit = {
        0: 632,    # No children
        1: 4210,   # One child
        2: 6990,   # Two children
        3: 7830    # Three or more children
    }
    
    children_key = min(num_children, 3)
    
    estimated_credit = max_credit.get(children_key, 0)

    # Simple check for eligibility (AGI must be below limits)
    if agi > 70000:
        estimated_credit = 0

    if earned_income <= 0:
        estimated_credit = 0

    print("---------------------------------")
    if estimated_credit == 0:
        print("Estimated Credit: $0 (Check income/eligibility)")
    else:
        print("Estimated Max Potential EITC:")
        print("$", round(estimated_credit, 0))

eitc_calc()