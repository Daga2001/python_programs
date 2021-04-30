"""La pizzerìa Delicias tiene 3 sedes en la ciudad de Cali
y requiere un programa para llevar estadisticas de las ventas
del negocio durante el año 2020. El programa debe pedir las
ventas en cada sede durante cada mes del año, y debe calcular
la venta total en el año, la venta promedio del total de cada mes,
y que sede tuvo la mayor venta, durante que mes y cual fue el valor
de esta venta"""

#definition of variables
sedesValues = { "1": 0, "2": 0, "3": 0 } #valor de cada sede mensualmente
nameSedeWithBestSale = "" #nombre de la sede con la mayor venta
averageMonthSales = 0 #venta promedio del total de cada mes
totalSales = 0 #venta total en el año
monthBestSale = 0 #mes en que hubo la mayor venta
valueOfBestSale = 0 #valor de la mayor venta

for i in range(0,12):
    sedesValues["1"] = int(input("Ingrese el valor de la venta de la sede 1 en el mes "+str(i+1)+": "))
    sedesValues["2"] = int(input("Ingrese el valor de la venta de la sede 2 en el mes "+str(i+1)+": "))
    sedesValues["3"] = int(input("Ingrese el valor de la venta de la sede 3 en el mes "+str(i+1)+": "))

    sedesNames = { v:k for k,v in sedesValues.items() }

    sede1 = sedesValues["1"]
    sede2 = sedesValues["2"]
    sede3 = sedesValues["3"]

    if valueOfBestSale < max(sede1,sede2,sede3):
        nameSedeWithBestSale = sedesNames[max(sede1,sede2,sede3)]
        valueOfBestSale = max(sede1,sede2,sede3)
        monthBestSale = i+1
    
    averageMonthSales = (sede1+sede2+sede3)/3
    totalSales += sede1+sede2+sede3
    print("----------------------------------------------------------------------")
    print("La venta promedio del mes "+str(i+1)+" fue de: "+str(averageMonthSales))
    print("----------------------------------------------------------------------")

print("La sede "+nameSedeWithBestSale+", tuvo la mayor venta del año en el mes: "+str(monthBestSale)
+", la cual alcanzo un valor de: "+str(valueOfBestSale))