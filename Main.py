# import pygame
# import requests 
# import rembg
# from io import BytesIO

# pygame.init()

# Width = 1000
# Height = 900

# screen = pygame.display.set_mode([Width,Height])
# pygame.display.set_caption("chess Game")

# font = pygame.font.Font("freesansbold.ttf", 20)
# medium_font = pygame.font.Font("freesansbold.ttf", 40)
# big_font= pygame.font.Font("freesansbold.ttf", 50)

# timer = pygame.time.Clock()
# fps = 60

# white_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "kinght", "rook",
#                 "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]

# white_locations = [(0,0), (1,0),(2,0),(3,0), (4,0),(5,0),(6,0), (7,0),
#                    (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

# black_pieces =  ["rook", "knight", "bishop", "king", "queen", "bishop", "kinght", "rook",
#                 "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]

# black_locations = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
#                    (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]

# captured_pieces_white = []
# captured_pieces_black = []

# #Ve los turnos y quien empieza 

# turns_step = 0
# selection = 100
# valid_moves = []

# # Imagenes de las piezas

# image_urls = ['https://media.geeksforgeeks.org/wp-content/uploads/20240302025946/black_queen.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025948/black_king.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025345/black_rook.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025951/black_bishop.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025947/black_knight.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025945/black_pawn.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025952/white_queen.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025943/white_king.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025949/white_rook.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025944/white_bishop.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025325/white_knight.png',
#               'https://media.geeksforgeeks.org/wp-content/uploads/20240302025953/white_pawn.png']

# # Cargar imagenes 

# black_queen = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[0]).content)))
# black_queen = pygame.transform.scale(black_queen, (80, 80))
# black_queen_small = pygame.transform.scale(black_queen, (45, 45))
# black_king = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[1]).content)))
# black_king = pygame.transform.scale(black_king, (80, 80))
# black_king_small = pygame.transform.scale(black_king, (45, 45))
# black_rook = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[2]).content)))
# black_rook = pygame.transform.scale(black_rook, (80, 80))
# black_rook_small = pygame.transform.scale(black_rook, (45, 45))
# black_bishop = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[3]).content)))
# black_bishop = pygame.transform.scale(black_bishop, (80, 80))
# black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
# black_knight = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[4]).content)))
# black_knight = pygame.transform.scale(black_knight, (80, 80))
# black_knight_small = pygame.transform.scale(black_knight, (45, 45))
# black_pawn = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[5]).content)))
# black_pawn = pygame.transform.scale(black_pawn, (65, 65))
# black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
# white_queen = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[6]).content)))
# white_queen = pygame.transform.scale(white_queen, (80, 80))
# white_queen_small = pygame.transform.scale(white_queen, (45, 45))
# white_king = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[7]).content)))
# white_king = pygame.transform.scale(white_king, (80, 80))
# white_king_small = pygame.transform.scale(white_king, (45, 45))
# white_rook = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[8]).content)))
# white_rook = pygame.transform.scale(white_rook, (80, 80))
# white_rook_small = pygame.transform.scale(white_rook, (45, 45))
# white_bishop = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[9]).content)))
# white_bishop = pygame.transform.scale(white_bishop, (80, 80))
# white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
# white_knight = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[10]).content)))
# white_knight = pygame.transform.scale(white_knight, (80, 80))
# white_knight_small = pygame.transform.scale(white_knight, (45, 45))
# white_pawn = pygame.image.load(
#     BytesIO(rembg.remove(requests.get(image_urls[11]).content)))
# white_pawn = pygame.transform.scale(white_pawn, (65, 65))
# white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

# # Cargar imagenes a las piezas

# white_images = [white_pawn, white_queen, white_king,
#                 white_knight, white_rook, white_bishop]
# small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]

# black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]

# small_black_images = [black_knight_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

# piece_list = ["pawn", "queen", "king", "knight", "rook", "bishop"]

# # Chequeo

# counter = 0
# winner = ""
# game_over = False

# # main game

# def draw_board():
#     for i in range(32):
#         column = i % 4
#         row = i // 4
#         if row % 2 == 0:
#             pygame.draw.rect(screen, "light gray", [600 - (column * 200), row * 100, 100, 100])
#         else:
#             pygame.draw.rect(screen, "light gray", [700 - (column * 200), row * 100, 100,100])
#             pygame.draw.rect(screen, "gray", [0,800, Width, 100])
#             pygame.draw.rect(screen, "gold", [0, 800 , Width, 100], 5)
#             pygame.draw.rect(screen, "gold", [800, 0, 200, Height], 5)
#             status_text = ["White: Select a Piece to Move!", "White: select a Destination!", "Black: select a piece to move!", "Black: selelct a destination!"]
#             screen.blit(big_font.render(status_text[turns_step], True, "black"), (20, 820))
#             for i in range(9):
#                 pygame.draw.line(screen, "black", (0,100 * i),(800, 100 * i),2)
#                 pygame.draw.line(screen, "black", (100 * i, 0), (100 * i, 800), 2)
#                 screen.blit(medium_font.render("Forfeit", True, "black"),(810, 830))

# def draw_pieces():
#     for i in range(len(white_pieces)):
#         index = piece_list.index(white_pieces[i])
#         if white_pieces[i] == "pawn":
#             screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        
        
                            
                        
import pygame
import chess

# --- 1. CONFIGURACIÓN INICIAL ---
ANCHO = 800
ALTO = 800
DIMENSION = 8  # El ajedrez es 8x8
TAMANO_CASILLA = ALTO // DIMENSION

FPS = 60

COLOR_CLARO = (234, 235, 200)  # Crema
COLOR_OSCURO = (119, 154, 88)  # Verde oscuro

# Diccionario para mapear las letras de las piezas a sus nombres de archivo
MAPA_PIEZAS = {
    'p': 'n_peon', 'r': 'n_torre', 'n': 'n_caballo', 'b': 'n_alfil', 'q': 'n_dama', 'k': 'n_rey',
    'P': 'b_peon', 'R': 'b_torre', 'N': 'b_caballo', 'B': 'b_alfil', 'Q': 'b_dama', 'K': 'b_rey'
}

IMAGENES_PIEZAS = {} # Aquí cargaremos las imágenes

def cargar_imagenes():
    """Carga todas las imágenes de las piezas y las escala al tamaño de la casilla."""
    for pieza in MAPA_PIEZAS.values():
        path = f"piezas/{pieza}.png" # Asegúrate que las imágenes están en la carpeta 'piezas'
        try:
            IMAGENES_PIEZAS[pieza] = pygame.transform.scale(
                pygame.image.load(path).convert_alpha(),
                (TAMANO_CASILLA, TAMANO_CASILLA)
            )
        except pygame.error as e:
            print(f"Error cargando la imagen {path}: {e}")
            print("Asegúrate de tener la carpeta 'piezas' con las imágenes correctas.")
            pygame.quit()
            exit()


def dibujar_tablero(pantalla):
    """Dibuja las casillas del tablero."""
    for fila in range(DIMENSION):
        for columna in range(DIMENSION):
            color = COLOR_CLARO if (fila + columna) % 2 == 0 else COLOR_OSCURO
            pygame.draw.rect(pantalla, color, (columna * TAMANO_CASILLA, fila * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA))

def dibujar_piezas(pantalla, tablero, pieza_seleccionada=None, pos_mouse=None):
    """
    Dibuja las piezas en el tablero, excluyendo la que está siendo arrastrada.
    Si hay una pieza seleccionada, la dibuja en la posición actual del ratón.
    """
    for fila in range(DIMENSION):
        for columna in range(DIMENSION):
            # Obtiene la casilla de ajedrez (ej: a1, b2)
            square_name = chess.square_name(chess.square(columna, 7 - fila)) # Pygame dibuja de arriba a abajo, chess.Board de abajo a arriba

            # Obtiene la pieza en esa casilla del objeto chess.Board
            piece = tablero.piece_at(chess.square(columna, 7 - fila))

            if piece:
                pieza_id = MAPA_PIEZAS[piece.symbol()]
                
                # No dibujamos la pieza si es la que estamos arrastrando
                if pieza_seleccionada and pieza_seleccionada['pieza_id'] == pieza_id and \
                   pieza_seleccionada['fila'] == fila and pieza_seleccionada['columna'] == columna:
                    continue # Saltamos esta pieza, la dibujaremos por separado

                pantalla.blit(IMAGENES_PIEZAS[pieza_id], (columna * TAMANO_CASILLA, fila * TAMANO_CASILLA))
    
    # Dibuja la pieza seleccionada en la posición del ratón si existe
    if pieza_seleccionada and pos_mouse:
        pieza_id = pieza_seleccionada['pieza_id']
        # Centra la pieza en el ratón para una mejor sensación de arrastre
        pantalla.blit(IMAGENES_PIEZAS[pieza_id], (pos_mouse[0] - TAMANO_CASILLA // 2, pos_mouse[1] - TAMANO_CASILLA // 2))


def obtener_fila_columna_desde_coords(pos_x, pos_y):
    """Convierte coordenadas de píxeles a fila y columna del tablero."""
    columna = pos_x // TAMANO_CASILLA
    fila = pos_y // TAMANO_CASILLA
    return fila, columna

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Ajedrez con Pygame y python-chess")
    reloj = pygame.time.Clock()

    cargar_imagenes() # Carga las imágenes al inicio

    tablero = chess.Board() # Nuestro tablero lógico de python-chess
    
    pieza_seleccionada = None # Guarda información de la pieza que estamos arrastrando
    origen_fila, origen_columna = None, None # La casilla de donde se tomó la pieza
    
    pos_mouse_actual = (0, 0) # Posición del ratón para arrastrar la pieza

    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            
            # --- MANEJO DE ARRASTRAR PIEZAS ---
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: # Botón izquierdo del ratón
                    pos_mouse_actual = evento.pos
                    fila, columna = obtener_fila_columna_desde_coords(*pos_mouse_actual)
                    
                    # chess.Board usa un sistema de coordenadas diferente:
                    # 'a1' es (0,0), 'h8' es (7,7)
                    # Pygame dibuja '0,0' arriba izquierda
                    # Convertimos la fila de Pygame (0-7 de arriba a abajo) a la fila de chess (0-7 de abajo a arriba)
                    origen_square = chess.square(columna, 7 - fila)
                    
                    piece = tablero.piece_at(origen_square)
                    
                    if piece and piece.color == tablero.turn: # Solo puedes mover tus propias piezas en tu turno
                        pieza_seleccionada = {
                            'pieza_id': MAPA_PIEZAS[piece.symbol()],
                            'pieza_obj': piece, # Guardamos el objeto Piece de python-chess
                            'fila': fila,
                            'columna': columna
                        }
                        origen_fila, origen_columna = fila, columna
            
            if evento.type == pygame.MOUSEMOTION:
                if pieza_seleccionada: # Si estamos arrastrando una pieza
                    pos_mouse_actual = evento.pos
            
            if evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1 and pieza_seleccionada:
                    destino_x, destino_y = evento.pos
                    destino_fila, destino_columna = obtener_fila_columna_desde_coords(destino_x, destino_y)
                    
                    # Convertir a la representación de casilla de python-chess
                    destino_square = chess.square(destino_columna, 7 - destino_fila)
                    origen_square = chess.square(origen_columna, 7 - origen_fila)

                    # Construir el movimiento
                    move = chess.Move(origen_square, destino_square)
                    
                    # ¡Importante! Manejar la promoción de peones
                    if pieza_seleccionada['pieza_obj'].piece_type == chess.PAWN and (destino_fila == 0 or destino_fila == 7):
                        # Asumimos promoción a Dama por simplicidad en este ejemplo
                        move = chess.Move(origen_square, destino_square, promotion=chess.QUEEN)


                    # Intentar hacer el movimiento
                    if move in tablero.legal_moves:
                        tablero.push(move)
                        print(f"Movimiento legal: {tablero.san(move)}")
                        if tablero.is_game_over():
                            print(f"¡Juego terminado! Resultado: {tablero.result()}")
                            running = False # O puedes mostrar un mensaje y reiniciar
                    else:
                        print(f"Movimiento ilegal: {tablero.san(move)} desde {origen_square} a {destino_square}")
                    
                    pieza_seleccionada = None # Liberar la pieza
                    origen_fila, origen_columna = None, None

        # --- DIBUJAR TODO ---
        pantalla.fill((0, 0, 0)) # Fondo negro
        dibujar_tablero(pantalla)
        dibujar_piezas(pantalla, tablero, pieza_seleccionada, pos_mouse_actual if pieza_seleccionada else None)

        pygame.display.flip() # Actualiza la pantalla
        reloj.tick(FPS) # Controla la velocidad de fotogramas

    pygame.quit()

if __name__ == "__main__":
    main()