años = int(input("Introduce tus años "))
if años >= 100:
    respuesta = input("Quieres ver tu tiempo vivido en meses o en días ")
    meses = (años*12)
    dias = (años*365)
    while True:
        if respuesta.lower() == "días":
            print(f"Tienes {años} años, por lo tanto has vivido {dias} días ")
            break
        elif respuesta.lower() == "meses":
            print(f"Tienes {años} años, por lo tanto has vivido {meses} meses ")
            break
        else:
            print("escribe bien como quieres que te calcule tu tiempo vivido ")
            respuesta = input("Quieres ver tu tiempo vivido en meses o en días ")
else:
    print("eres autista o que")
    while True:
        print("FUCK NIGGERS")
