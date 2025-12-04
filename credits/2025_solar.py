# 2025 Residential Clean Energy Credit (Solar, Wind, Geothermal, etc.)
# Credit: 30% of total cost. No annual cap.

def solar_calc():
    """Calculates the estimated 2025 Residential Clean Energy Credit."""
    print("--- 2025 Residential Clean Energy Credit ---")
    
    try:
        system_cost = float(input("Total System Cost: "))
    except ValueError:
        print("Invalid input.")
        return

    credit_percentage = 0.30
    
    # Calculation
    credit_amount = system_cost * credit_percentage
    
    print("---------------------------------")
    print("Credit Percentage: 30.0%")
    print("Estimated 2025 Credit (Nonrefundable, carryforward):")
    print("$", round(credit_amount, 2))

solar_calc()