meses = {
    "01" : "Enero",
    "02" : "Febrero",
    "03" : "Marzo",
    "04" : "Abril",
    "05" : "Mayo",
    "06" : "Junio",
    "07" : "Julio",
    "08" : "Agosto",
    "09" : "Septiembre",
    "10" : "Octubre",
    "11" : "Noviembre",
    "12" : "Diciembre"
}
def fecha_completa(d,m,a):
    return (f'{d} de {meses[m]} de {a}')
dia = input("Ingrese el dia:")
mes = input("Ingrese el mes:")
año = input("Ingrese el año:")
print(fecha_completa(dia,mes,año))