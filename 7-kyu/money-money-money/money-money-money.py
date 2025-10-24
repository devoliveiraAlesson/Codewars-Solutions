def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        
        juros = principal * interest
        imposto = juros * tax
        principal += juros - imposto
        y += 1
    
    return y
    
​