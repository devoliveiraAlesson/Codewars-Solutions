def human_years_cat_years_dog_years(human_years):
    catyears = 0
    dogyears = 0
    if human_years == 1:
        catyears = 15
        dogyears = 15
    elif human_years == 2:
        catyears = 24
        dogyears = 24
    else:
        catyears = 24 + ((human_years - 2)*4)
        dogyears = 24 + ((human_years - 2)*5)    
    
    return [human_years,catyears,dogyears]