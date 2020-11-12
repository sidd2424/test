income = 35000
if income < 10000:
    tax_percentage = 0.0
elif income < 20000:
    tax_percentage = 0.2
elif income < 30000:
    tax_percentage = 0.3
else:
    tax_percentage = 0.4

tax = income * tax_percentage

print('I will need to pay', tax, 'as tax.')

qualifier
