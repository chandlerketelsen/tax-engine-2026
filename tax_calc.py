# 2026 Federal Tax Liability Calculator (Pre-Credits)
# All data is estimated 2026 inflation-adjusted values.

# 1. HARDCODED 2026 TAX DATA (Standard Deduction)
DEDUCTIONS = {
    "SINGLE": 15350,
    "MFJ": 30700,
    "HOH": 23050,
    "MFS": 15350
}

# 2. HARDCODED 2026 TAX DATA (Brackets)
# Keys: r=Rate, t=Threshold (start of the bracket)
BRACKETS = {
    "SINGLE": [
      {"r": 0.10, "t": 0},
      {"r": 0.12, "t": 12000},
      {"r": 0.22, "t": 50000},
      {"r": 0.24, "t": 110000},
      {"r": 0.32, "t": 190000},
      {"r": 0.35, "t": 240000},
      {"r": 0.37, "t": 600000}
    ],
    "MFJ": [
      {"r": 0.10, "t": 0},
      {"r": 0.12, "t": 24000},
      {"r": 0.22, "t": 100000},
      {"r": 0.24, "t": 220000},
      {"r": 0.32, "t": 380000},
      {"r": 0.35, "t": 480000},
      {"r": 0.37, "t": 720000}
    ],
    "HOH": [
      {"r": 0.10, "t": 0},
      {"r": 0.12, "t": 17000},
      {"r": 0.22, "t": 67000},
      {"r": 0.24, "t": 140000},
      {"r": 0.32, "t": 215000},
      {"r": 0.35, "t": 270000},
      {"r": 0.37, "t": 600000}
    ],
    "MFS": [
      {"r": 0.10, "t": 0},
      {"r": 0.12, "t": 12000},
      {"r": 0.22, "t": 50000},
      {"r": 0.24, "t": 110000},
      {"r": 0.32, "t": 190000},
      {"r": 0.35, "t": 240000},
      {"r": 0.37, "t": 360000}
    ]
}

def gross_tax_calc(tax_inc, status):
    """Calculates gross federal income tax."""
    tax_brackets = BRACKETS.get(status)
    if not tax_brackets:
        return 0.0

    tax_due = 0.0
    
    # Sort brackets by threshold 't' for safety
    tax_brackets.sort(key=lambda x: x['t'])

    for i in range(len(tax_brackets)):
        bracket = tax_brackets[i]
        rate = bracket['r']
        threshold = bracket['t']
        
        # Determine the upper limit of the current bracket
        if i + 1 < len(tax_brackets):
            top_limit = tax_brackets[i+1]['t']
        else:
            top_limit = float('inf')

        # Check if any income falls into this bracket
        if tax_inc > threshold:
            # Amount of income taxed at this rate
            income_in_bracket = min(tax_inc, top_limit) - threshold
            tax_due += income_in_bracket * rate
            
    return tax_due

def run_calc():
    """Main function to run the tax calculation process."""
    print("--- 2026 Tax Liability ---")
    
    # 1. Get Inputs (short prompts)
    try:
        g_inc = float(input("Gross Income: "))
        adj = float(input("Adjustments: "))
        s_in = input("Status (S/M/H/F): ").upper()
        
        # Map input to full status string
        status_map = {"S": "SINGLE", "M": "MFJ", "H": "HOH", "F": "MFS"}
        status = status_map.get(s_in, "SINGLE")
            
    except ValueError:
        print("Invalid number.")
        return
        
    # 2. AGI
    agi = g_inc - adj
    
    # 3. Taxable Income (using Standard Deduction only)
    deduction = DEDUCTIONS.get(status, 0)
    taxable_inc = max(0.0, agi - deduction)
    
    # 4. Gross Tax Liability
    gross_tax_liab = gross_tax_calc(taxable_inc, status)
    
    # 5. Display Results
    print("\n--- Summary ---")
    print(f"AGI: {round(agi, 0)}")
    print(f"Deduction: {round(deduction, 0)}")
    print(f"Taxable: {round(taxable_inc, 0)}")
    print("-----------------")
    print(f"Gross Tax: ${round(gross_tax_liab, 2)}")

run_calc()