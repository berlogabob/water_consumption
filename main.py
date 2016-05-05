god = 365 #дней в году
vihodnie = 2*4*12 # количество выходных дней в году
rab_dni = god-vihodnie # количество рабочих дней в году
lpd = 5 ## количество литров воды в день  (per day)
litrov_v_god = rab_dni * lpd
print ("рабочих дней",rab_dni, '\n'"литров в год", litrov_v_god)
