texto = "hola"
texto2="Mundoo!!"

textoFinal = texto + " "+texto2

print("El saludo es: %s %s"%(texto,texto2))



cadena= "Saludar dos: {1} {0}".format(texto,texto2)

print(cadena)


cadena= "Saludar dos: {x} {y}".format(x=texto,y=texto2)

print(cadena)



