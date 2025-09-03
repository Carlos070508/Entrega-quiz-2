base = float(input("Digite a base do terreno em metros: "))
altura = float(input("Digite a altura do terreno em metros: "))

Area_Triangulo = (base * altura) / 2
Area_Rectangulo = base * base

#Area do terreno
area_Total = Area_Rectangulo + Area_Rectangulo

Area_Total = Area_Triangulo + Area_Rectangulo

Precio_metro_cuadrado = 4400000
Precio_Total_terreno = Area_Total * Precio_metro_cuadrado

print(f"Area total del terreno es: {Area_Total} mts^2")
print(f"El precio total del terreno es: {Precio_Total_terreno} COP")