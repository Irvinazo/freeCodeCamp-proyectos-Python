class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        if len(self.name)%2 == 0:
            title = '*'*((30-len(self.name))//2) \
            + str(self.name) + '*'*((30-len(self.name))//2)
     
        else:
            title = '*'*((30-len(self.name))//2+1) \
            + str(self.name) + '*'*((30-len(self.name))//2)
        
        deposit_string = [dicc['description'][0:23] \
                        + ' '*(23-len(dicc['description'][0:23])) \
                        + ' '*(7-len(f"{dicc['amount']:.2f}"[0:7])) \
                        + f"{dicc['amount']:.2f}"[0:7] \
                        for dicc in self.ledger]

        deposit_string.append( 'Total: ' \
                            + str(self.get_balance()))

        string = title + '\n' + '\n'.join(deposit_string)
        
        return string
    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount,\
        'description': description})
        return 
    
    def check_funds(self, amount):
        values = []
        for dicc in self.ledger:
            values.append(dicc['amount'])

        if sum(values)<amount:
            return False

        else:
            return True
                        
    def withdraw(self, amount, description = ''): 
        if self.check_funds(amount) == False:
            return False

        else: 
            self.ledger.append({'amount': (-1)*amount,\
            'description': description})
            return True

    def get_balance(self):
        values = []
        for dicc in self.ledger:
            values.append(dicc['amount'])

        return sum(values)

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + self.name)
            
            return True
        
        else:
        
            return False

def create_spend_chart(categories):
    spent_by_cat = [sum([ dicc['amount'] \
                    for dicc in cat.ledger \
                    if dicc['amount']<0 ]) for cat in categories] 
    
    total_spent = sum(spent_by_cat)
    
    percentage_by_cat = [spent_by_cat[i]*100/total_spent \
                        for i in range(len(categories))]
    print(percentage_by_cat)
    for i in range(len(percentage_by_cat)):
        percentage_by_cat[i] = (percentage_by_cat[i]//10)*10
        
    print(percentage_by_cat)

    title = 'Percentage spent by category'

    percentages = [' '*(3-len(str(i*10))) \
    + f'{i*10}|' for i in range(10,-1,-1)]

    balls = [''.join([' o ' if dec*10 <= (percentage_by_cat[i]+10) \
            else '   ' for i in range(len(categories))]) \
            for dec in range(11,0,-1)]
    
    lines_chart = [percentages[i] + balls[i] + ' ' for i in range(11)]

    bars = '\n'.join(lines_chart)
    
    dashed_line = ' '*4 + '---'*(len(categories)) +'-'
    
    max_len = max([len(str(cat.name)) for cat in categories])
    
    names = [' '*5 + '  '.join([f'{str(cat.name)[i]}' \
            if len(str(cat.name)) > i else ' ' \
            for cat in categories]) \
            for i in range(max_len)]

    names_final = [name + '  ' for name in names]
    
    names_chart = '\n'.join(names_final)

    chart_strings = [title, bars, dashed_line, names_chart]

    chart = '\n'.join(chart_strings)
    
    return chart


