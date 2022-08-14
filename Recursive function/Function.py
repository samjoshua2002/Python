def name(x):
    if x==1:
        return 1
    else:
        return x+name(x-1)
        
