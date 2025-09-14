def product_fib(prod):
        
    temp = 0
    fi = 1
    bo = 0
    
    while fi * bo < prod:
        temp = fi
        fi = fi + bo
        bo = temp
    return [bo, fi, bo * fi == prod]