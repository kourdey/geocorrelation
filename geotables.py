
def alfa (PI):
    if PI<= 15:
        return 0.06 *60/73
    elif PI > 15 and PI <= 20:
        return (-0.0026*60/73)*(PI-15)+ 0.068 * 60/73
    elif PI > 20 and PI <= 25:
        return (-0.0014*60/73)* (PI-20) + 0.055 * 60/73
    elif PI > 25 and PI <= 30:
        return (-0.0006 * 60/73)*(PI-25)+0.048 * 60/73
    elif PI > 30 and PI <= 40:
        return (-0.0001 * 60/73) * (PI-30)+0.045 * 60/73
        
    elif PI > 40 and PI <=60:
        return (-0.00005*60/73)*(PI-40)+0.044*60/73
    elif PI > 60:
        return 0.043 *60/73

print (alfa(40))
