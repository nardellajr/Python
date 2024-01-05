
# Federal tax calculation for a married couple filing jointly with regular income and long-term capital gains

# Income details
current_income = 4000
standard_dec = 27700

regular_income = current_income - standard_dec
capital_gains = 80000   # Long-term capital gains

# 2023 Tax Brackets for Ordinary Income for Married Filing Jointly
ordinary_tax_brackets = [
    (0, 22250, 0.10),       # 10% for income between $0 and $22,250
    (22251, 89150, 0.12),   # 12% for income between $22,251 and $89,150
    (89151, 190750, 0.22),  # 22% for income between $89,151 and $190,750
    # Higher brackets are not applicable for $84,000 income
]

# 2023 Long-Term Capital Gains Tax Brackets for Married Filing Jointly
ltcg_tax_brackets = [
    (0, 83350, 0.0),        # 0% for capital gains with total income up to $83,350
    (83351, 517200, 0.15),  # 15% for capital gains with total income between $83,351 and $517,200
    # Higher brackets are not applicable for this scenario
]

# Function to calculate tax based on brackets
def calculate_tax(income, brackets):
    tax = 0
    for bracket in brackets:
        lower, upper, rate = bracket
        if income > upper:
            tax += (upper - lower) * rate
        else:
            tax += (income - lower) * rate
            break
    return tax

# Calculate the tax on regular income
tax_on_regular_income = calculate_tax(regular_income, ordinary_tax_brackets)

# Calculate combined income to determine the rate for capital gains
combined_income = regular_income + capital_gains

# Calculate the tax on capital gains
tax_on_capital_gains = calculate_tax(combined_income, ltcg_tax_brackets) - calculate_tax(regular_income, ltcg_tax_brackets)

total_tax = tax_on_regular_income + tax_on_capital_gains
print(total_tax)
