'''
Problem 3. Fraud Detection
'''

with open('transactions.txt') as f:
    transactions = []
    for line in f:
        name, amount, location, interval = line.split('|')
        amount = int(amount)
        interval = int(interval.rstrip())
        
        data = {
            'name': name,
            'amount': amount,
            'location': location,
            'interval': interval
        }
        
        # Spent $ > 3000
        if amount > 3000:
            print(name)
        
        # Check transactions for this person in a different place
        for transaction in transactions:
            if transaction['name'] == name and transaction['location'] != location and abs(interval - transaction['interval']) < 60:
                print(name)
        
        transactions.append(data)