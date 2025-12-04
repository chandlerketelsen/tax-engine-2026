# 2025 General Business Credit (GBC) - Placeholder
# This script serves as a simple summation tool.

def gbc_calc():
    """A placeholder to sum estimated components of the GBC."""
    print("--- 2025 General Business Credit Sum ---")
    
    try:
        r_d_credit = float(input("R&D Credit Est.: "))
        hiring_credit = float(input("WOTC Credit Est.: "))
        energy_credit = float(input("Bus. Energy Cr. Est.: "))
        other_credits = float(input("Other Business Cr.: "))
    except ValueError:
        print("Invalid input.")
        return

    total_gbc = r_d_credit + hiring_credit + energy_credit + other_credits

    print("---------------------------------")
    print("Total General Business Credit:")
    print("$", round(total_gbc, 2))

gbc_calc()