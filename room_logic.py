from datos_juego import game_room_items, room_1_items, room_2_items, salon_items

def add_item(inventory, item_name):
    inventory.add(item_name)
    print(f"-> ¡Has encontrado: {item_name}!")


def game_room_eleccion(inventory):
       
    print("Te encuentras despertando en un sofá desconocido, en una casa inquietante y sin ventanas. Tu memoria no te explica cómo llegaste allí ni qué ocurrió antes. Presientes una amenaza inminente acechando en alguna parte: ¡tu instinto te dice que escapes de la casa inmediatamente!")

    while True:
        eleccion_game_room = input(f"En la sala hay {game_room_items}. ¿Qué investigas? ").lower()

        if eleccion_game_room == "piano":
            print("Hay una llave!! Quizas sirva para abrir la puerta.")
            add_item(inventory, "llave a")
            return inventory 
            
        elif eleccion_game_room == "puerta":
            print("La puerta parece cerrada, pero tiene cerradura. Debería de haber una llave escondida.")
            
        elif eleccion_game_room not in game_room_items:
            print("Escoge alguna cosa de la sala.")
            
        else: 
            print("No hay nada...")


def room1_eleccion(inventory):
        
    print("Te dijires a la única puerta de la sala, la abres con cuidado y encuentras otra habitación con una cama, las puertas A (por la que has venido), la B y la C.")

    while True:
        eleccion_room1 = input(f"¿Qué investigas? {room_1_items}").lower()

        if eleccion_room1 == "cama":
            if "llave b" not in inventory: 
                print("Hay una segunda llave!! Pero dos puertas.")
                add_item(inventory, "llave b")
                break        
            return inventory 
        elif eleccion_room1 == "puerta a":
            print("Ya has encontrado todos los objetos de esa sala. Es hora de intentar una de las otras puertas.")
            return inventory             
        elif eleccion_room1 not in room_1_items:
            print("Escoge alguna cosa de la sala.")            
        else: 
            print("La puerta no se abre...")


def puerta_eleccion(inventory):
    while True:
        eleccion_puerta = input("¿Qué puerta intentas abrir, la B o la C? ").lower()

        if eleccion_puerta == "b":
            if "llave b" in inventory: 
                print("Se ha abierto! Puedes pasar.")
                return inventory, "room_2"
            else:
                print("La llave B no encaja o no la tienes.")
        
        elif eleccion_puerta == "c":
            print("La llave no encaja.")
            
        else:
            print("Elige solo 'b' o 'c'.")


def room2_eleccion(inventory):
        
    print("Entras en el dormitorio 2.")
    print("Encuentras una cama doble y un armario.")

    while True:
        eleccion_room2 = input(f"¿Qué investigas la cama o el armario? ").lower()        
        if eleccion_room2 == "cama":
            if "llave c" not in inventory:
                 print("Has encontrado otra llave! ")
                 add_item(inventory, "llave c")                 
            dificil_eleccion = input("Quieres probar la puerta de la habitación anterior? SI/NO ").lower()
            if dificil_eleccion == "si":
                print("Cruzas la habitación y te diriges a la puerta. Cuando pruebas la llave la puerta se abre lentamente.")
                return inventory, "salir al salón"             
        elif eleccion_room2 == "armario":
            if "llave d" not in inventory:
                 print("Has encontrado otra llave! ")
                 add_item(inventory, "llave d")                 
            dificil_eleccion2 = input("Quieres probar la puerta de la habitación anterior? SI/NO ").lower()
            if dificil_eleccion2 == "si":
                if "llave c" in inventory:
                    print("Se ha abierto la que podría ser la última puerta.")
                    return inventory, "salir al salon"
                else:
                    print("La llave no encaja... te toca volver a la sala en la que estabas.")                    
        elif eleccion_room2 not in room_2_items:
            print("Escoge alguna cosa de la sala.")
            

def salon_eleccion(inventory):
    

    print("Entras en el salon.")
    print("A pesar de su tamaño lo único que hay en la sala es una mesa y una puerta. No se ve el exterior.")

    while True:
        eleccion_salon = input(f"¿Qué investigas la mesa o la puerta? ").lower()

        if eleccion_salon == "mesa":
            print("No hay nada...")

        elif eleccion_salon == "puerta":
            if "llave d" in inventory:
                print("¡HAS CONSEGUIDO SALIR AL EXTERIOR! ¡Felicidades!")
                return inventory, "end_game" 
            else:
                print("Por mucho que lo intentas ninguna de las llaves encaja en la cerradura.")
                print("Deberías volver a la última sala, te queda algo por revisar.")
                room2_eleccion(inventory)
        elif eleccion_salon not in salon_items:
            print("Escoge alguna cosa de la sala.")            
        else:
            print("Opción no válida.")