# 2025 Child and Dependent Care Credit
# Max expenses: $3,000 (1 person) / $6,000 (2+ people)
# Credit Rate: 35% (AGI < $15k) down to 20% (AGI > $43k)

def child_care_calc():
    """Calculates the estimated 2025 Child and Dependent Care Credit."""
    print("--- 2025 Child/Dependent Care Credit ---")
    
    # Get user inputs
    try:
        agi = float(input("Enter AGI: "))
        num_qualifying = int(input("Qualify Count (1/2+): "))
        total_expenses = float(input("Expenses Paid: "))
    except ValueError:
        print("Invalid input.")
        return

    # 1. Determine maximum expenses
    if num_qualifying >= 2:
        max_expenses = 6000
    elif num_qualifying == 1:
        max_expenses = 3000
    else:
        print("Error: Need at least 1 qualifying individual.")
        return

    # Cap expenses at the statutory maximum
    capped_expenses = min(total_expenses, max_expenses)

    # 2. Determine credit percentage (Based on AGI)
    if agi <= 15000:
        percent = 0.35
    elif agi > 43000:
        percent = 0.20
    else:
        reduction_steps = (agi - 15000) // 2000
        percent = 0.35 - (reduction_steps * 0.01)
        
        # Ensure percentage does not drop below 20%
        percent = max(percent, 0.20)

    # 3. Calculate final credit
    credit_amount = capped_expenses * percent

    print("---------------------------------")
    print("Credit Percentage:", round(percent * 100, 1), "%")
    print("Expenses Used:", round(capped_expenses, 2))
    print("Estimated 2025 Credit:")
    print("$", round(credit_amount, 2))

child_care_calc()