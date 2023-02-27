Sueldo_Bruto_Anual = [312500, 300000, 200000, 500000, 512500, 287500, 112500, 437500, 300000, 350000, 312500,
                      200000, 287500, 109375, 200000, 287500, 109375, 187500, 200000, 275000, 171875, 212500,
                      106250, 171875, 103750, 168750, 175000, 225000, 250000, 100000, 162500, 250000, 93750,
                      247500, 175000]

def sat(sueldo):
    sueldonanual = []
    for anual in sueldo:
        if anual <= 100000:
            imp = .1
        elif 100000 < anual <= 125000:
            imp = .12
        elif 125000 < anual <= 150000:
            imp = .14
        elif 150000 < anual <= 175000:
            imp = .16
        elif 175000 < anual <= 200000:
            imp = .17
        elif 200000 < anual <= 250000:
            imp = .19
        elif 250000 < anual <= 300000:
            imp = .21
        elif 300000 < anual <= 350000:
            imp = .23
        elif 350000 < anual <= 400000:
            imp = .25
        elif anual > 400000:
            imp = .3
        multiplicador = 1-imp
        netoanual = anual * multiplicador
        sueldonanual.append(netoanual)
        print('El sueldo es {}, el multiplicador es {} y el neto es {}'.format(anual, multiplicador, netoanual))
        print(sueldonanual)


sat(Sueldo_Bruto_Anual)
