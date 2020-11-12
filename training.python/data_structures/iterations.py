from datetime import (
    date,
    timedelta,
)
today = date.today()
tommorrow = today + timedelta(days=1)
products = [
    {
        'id': 111,
        'name': 'Apples',
        'price': 120,
        'expiry_date': today,
    },
    {
        'id': 112,
        'name': 'Oranges',
        'price': 150,
        'expiry_date': today + timedelta(days=2),
    },
    {
        'id': 113,
        'name': 'Mangoes',
        'price': 300,
        'expiry_date': today + timedelta(days=20),
    }
]
for product in products:
    if product['expiry_date'] <= today:
        product['expired'] = True
        continue
    elif product['expiry_date'] == today:
        product['price'] -= product['price']*0.2
    print(product['name'], 'is going for', product['price'], 'today')
