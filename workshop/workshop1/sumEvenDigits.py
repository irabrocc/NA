def even_sum(n): 
    total = 0 
    remain = n 
    while remain > 0:
        digit = remain % 10 
        if digit % 2 == 0: 
            total += digit 
        remain //= 10

    return total 