pregunta1 = input("¿El paciente responde a estímulos? [S / N]: ").lower()
if pregunta1 == 'n':
    print("Abra la vía aérea")
    pregunta2 = input("¿El paciente respira? [S / N]: ").lower()
    if pregunta2 == 'n':
        print("Administrar 5 ventilaciones y llamar a la ambulancia")
        pregunta4 = 'n'
        while pregunta4 == 'n':
            pregunta3 = input("¿El paciente presenta signos vitales? [S / N]: ").lower()
            if pregunta3 == 'n':
                print("Administrar Compresiones Torácicas hasta que llegue la ambulancia")
            else:
                print("Reevaluar hasta que llegue la ambulancia")
            pregunta4 = input("¿Llegó la ambulancia? [S / N]: ").lower()
    else:
        print("Permitirle posición de suficiente ventilación")
else:
    print("Valorar la necesidad de llevarlo al hospital más cercano")
    
print("FIN DEL PROGRAMA")