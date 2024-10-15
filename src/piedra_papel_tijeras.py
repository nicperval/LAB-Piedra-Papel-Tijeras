import random

def ordenador_decide_jugada():
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijera" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    print('Bienvenido a "Piedra, Papel o Tijeras"')
    ord = ordenador_decide_jugada()
    per = usuario_decide_jugada()
    print(f'El ordenador ha sacado {ord}')
    resultado = determina_ganador(per,ord)
    if resultado == "Ganaste":
        print('Has ganado')
    if resultado == "Perdiste":
        print('Has perdido')
    if resultado == "Empate":
        print('Habeis empatado')

def jugar_torneo():
    print('Bienvenido a "Piedra, Papel o Tijeras"')
    og = 0
    jg = 0
    while jg or og < 3:
        ord = ordenador_decide_jugada()
        per = usuario_decide_jugada()
        print(f'El ordenador ha sacado {ord}')
        resultado = determina_ganador(per,ord)
        if resultado == "Ganaste":
            jg += 1
        if resultado == "Perdiste":
            og += 1
        if resultado == "Empate":
            print('Empate')
        print(f'{jg} - {og}')
        if jg == 3:
            break
        if og == 3:
            break
    if jg == 3:
        print('Has ganado')
    else:
        print('Has perdido')
    
if __name__ == '__main__':
    jugar_torneo()