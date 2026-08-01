# Brindar información (artista, película, serie – match-case con al menos 5 casos)
tipo = input("¿Quieres info de artista, película o serie? ").strip().lower()

if tipo == "artista":
    nombre = input("Escribe el nombre del artista: ").strip().lower()
elif tipo == "pelicula" or tipo == "película":
    nombre = input("Escribe el nombre de la película: ").strip().lower()
elif tipo == "serie":
    nombre = input("Escribe el nombre de la serie: ").strip().lower()
else:
    nombre = None
    print("Tipo inválido. Elige artista, película o serie.")

if nombre:
    match nombre:
        case "jennie kim":
            print("Artista: Jennie Kim, cantante y compositora surcoreana.")
        case "taylor swift":
            print("Artista: Taylor Swift, cantante y compositora estadounidense.")
        case "the great flood":
            print("Película: The Great Flood, película de 2023.")
        case "parasite":
            print("Película: Parasite, película surcoreana ganadora del Oscar 2020.")
        case "interstellar":
            print("Película: Interstellar, ciencia ficción de Christopher Nolan (2014).")
        case "stranger things":
            print("Serie: Stranger Things, serie de ciencia ficción de Netflix.")
        case _:
            print("No tengo información sobre ese nombre.")