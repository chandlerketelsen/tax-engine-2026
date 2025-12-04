# 2025 U.S. Federal Tax Data
# Defined as a Python dictionary literal for TI-84 compatibility (no JSON import)
# (Uses 2025 indexed rates and standard deduction amounts)

TAX_DATA = {
    "DEDUCTIONS": {
        "SINGLE": 14600.00,
        "MARRIED_JOINT": 29200.00,
        "HEAD_OF_HOUSEHOLD": 21900.00
    },
    "BRACKETS": {
        "SINGLE": [
            {"rate": 0.10, "max": 11600.00, "base_tax": 0.00},
            {"rate": 0.12, "max": 47150.00, "base_tax": 1160.00},
            {"rate": 0.22, "max": 100000.00, "base_tax": 6415.50},
            {"rate": 0.24, "max": 191950.00, "base_tax": 17892.50},
            {"rate": 0.32, "max": 243975.00, "base_tax": 40062.50},
            {"rate": 0.35, "max": 609350.00, "base_tax": 56066.50}
        ],
        "MARRIED_JOINT": [
            {"rate": 0.10, "max": 23200.00, "base_tax": 0.00},
            {"rate": 0.12, "max": 94300.00, "base_tax": 2320.00},
            {"rate": 0.22, "max": 200000.00, "base_tax": 12830.00},
            {"rate": 0.24, "max": 383900.00, "base_tax": 35785.00},
            {"rate": 0.32, "max": 487950.00, "base_tax": 80125.00},
            {"rate": 0.35, "max": 731925.00, "base_tax": 112133.00}
        ],
        "HEAD_OF_HOUSEHOLD": [
            {"rate": 0.10, "max": 16550.00, "base_tax": 0.00},
            {"rate": 0.12, "max": 65500.00, "base_tax": 1655.00},
            {"rate": 0.22, "max": 100000.00, "base_tax": 8099.00},
            {"rate": 0.24, "max": 191950.00, "base_tax": 17892.50},
            {"rate": 0.32, "max": 243975.00, "base_tax": 40062.50},
            {"rate": 0.35, "max": 609350.00, "base_tax": 56066.50}
        ]
    }
}