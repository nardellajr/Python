
def calculate_tax(income, brackets):
    tax = 0
    # Ensure the brackets are sorted by their upper limit
    brackets.sort(key=lambda x: x[1])

    for bracket in brackets:
        lower, upper, rate = bracket

        if income > upper:
            tax += (upper - lower) * rate
        else:
            tax += (income - lower) * rate
            break

    return tax


def calculate_multiyear_tax(income, withdrawal_amounts, brackets):
    total_tax = 0
    for withdrawal in withdrawal_amounts:
        yearly_income = income + withdrawal
        yearly_tax = calculate_tax(yearly_income, brackets)
        total_tax += yearly_tax

    return total_tax


if __name__ == '__main__':

    # 2024 new brackets
    # tax_brackets = [
    #     (0, 23200, 0.10),
    #     (23201, 94300, 0.12),
    #     (94301, 201050, 0.22),
    #     (201051, 383900, 0.24),
    #     (383901, 487450, 0.32),
    # ]

    # 2023
    tax_brackets = [
        (0, 22000, 0.10),
        (22001, 89450, 0.12),
        (89451, 190750, 0.22),
        (190751, 364200, 0.24),
        (364201, 462500, 0.32),
    ]

    # Define the withdrawal strategies: 100k over 1 year, 100k over 2 years, 100k over 3 years,
    # and similarly for 200k and 300k.
    withdrawal_strategies = {
        '100k over 1 year': [100000],
        '100k over 2 years': [50000, 50000],
        '100k over 3 years': [33333, 33333, 33333],
        '200k over 1 year': [200000],
        '200k over 2 years': [100000, 100000],
        '200k over 3 years': [66666, 66666, 66666],
        '300k over 1 year': [300000],
        '300k over 2 years': [150000, 150000],
        '300k over 3 years': [100000, 100000, 100000]
    }

    current_income = [100000, 60000]
    standard_dec = 27700

    for i in current_income:
        after_dec_income = i - standard_dec
        tax_results = {}
        print(f'Income: {i}')

        for strategy, amounts in withdrawal_strategies.items():
            if len(amounts) == 1:
                print(f'  Taxable Income : {after_dec_income + amounts[0]}')

            tax_results[strategy] = calculate_multiyear_tax(after_dec_income, amounts, tax_brackets)

        for tr in tax_results.items():
            desc, value = tr
            print(f'{desc}, tax amount: {value}')
