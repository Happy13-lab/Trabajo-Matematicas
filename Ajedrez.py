import chess

def jugar_ajedrez_consola():
    """
    Función principal para correr un juego de ajedrez en la consola.
    """
    # Inicializa el tablero
    board = chess.Board()

    # Bucle principal del juego
    while not board.is_game_over():
        # Imprime el tablero en formato ASCII
        print("\n" + "="*30)
        print(board)
        print("="*30)

        # Determina de quién es el turno
        if board.turn == chess.WHITE:
            print("\nTurno de las Blancas")
        else:
            print("\nTurno de las Negras")

        # Pide al usuario que ingrese una jugada
        # Usamos notación SAN (ej: "e4", "Nf3", "Qxd4", "O-O" para enroque)
        move_san = input("Ingresa tu jugada (en notación SAN): ")

        try:
            # Intenta realizar el movimiento
            board.push_san(move_san)
        except ValueError:
            # Captura si el movimiento es ilegal o inválido
            print("\n¡Movimiento ilegal o inválido! '{}' no es una jugada válida.".format(move_san))
            print("Intenta de nuevo.")
        except KeyboardInterrupt:
            # Permite salir del juego con Ctrl+C
            print("\nJuego interrumpido.")
            break

    # --- El juego ha terminado ---
    print("\n¡JUEGO TERMINADO!")
    print("="*30)
    print(board)
    print("="*30)
    
    # Imprime el resultado
    resultado = board.result()
    print(f"Resultado: {resultado}")

    if board.is_checkmate():
        print("¡Jaque Mate!")
    elif board.is_stalemate():
        print("¡Ahogado! (Tablas)")
    elif board.is_insufficient_material():
        print("¡Material insuficiente! (Tablas)")
    elif board.is_seventyfive_moves():
        print("Regla de los 75 movimientos (Tablas)")
    elif board.is_fivefold_repetition():
        print("Repetición quíntuple (Tablas)")

# --- Iniciar el juego ---
if __name__ == "__main__":
    jugar_ajedrez_consola()