# 2025 Self-Employed Sick and Family Leave Credit (COVID-Related, Extended)
# Max sick leave: $511/day for 10 days ($5,110).
# Max family leave: $200/day for 50 days ($10,000).

def self_leave_calc():
    """Calculates the estimated Self-Employed Sick/Family Leave Credit."""
    print("--- 2025 Self-Employed Leave Credit ---")
    
    try:
        sick_days = int(input("Sick Days (Max 10): "))
        family_days = int(input("Family Days (Max 50): "))
        avg_daily_income = float(input("Avg Daily SE Income: "))
    except ValueError:
        print("Invalid input.")
        return

    # 1. Sick Leave Credit
    sick_days_capped = min(sick_days, 10)
    sick_rate = min(avg_daily_income, 511.0)
    sick_credit = sick_days_capped * sick_rate
    
    # 2. Family Leave Credit
    family_days_capped = min(family_days, 50)
    family_rate = min(avg_daily_income * 0.67, 200.0)
    family_credit = family_days_capped * family_rate
    
    total_credit = sick_credit + family_credit

    print("---------------------------------")
    print("Sick Leave Portion:", round(sick_credit, 2))
    print("Family Leave Portion:", round(family_credit, 2))
    print("Estimated 2025 Total Credit:")
    print("$", round(total_credit, 2))

self_leave_calc()