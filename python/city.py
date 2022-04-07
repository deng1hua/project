def fun(city,country,population=0):
    if population:
        fullname = f'{city},{country}' + f' - population {population}'
    else:
        fullname=f'{city},{country}'
    return fullname.title()
