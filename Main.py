import pygame
import requests 
import rembg
from io import BytesIO

pygame.init()

Width = 1000
Height = 900

screen = pygame.display.set_mode([Width,Height])
pygame.display.set_caption("chess Game")

font = pygame.font.Font("freesansbold.ttf", 20)
medium_font = pygame.font.Font("freesansbold.ttf", 40)
big_font= pygame.font.Font("freesansbold.ttf", 50)

timer = pygame.time.Clock()
fps = 60

white_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "kinght", "rook",
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]

white_locations = [(0,0), (1,0),(2,0),(3,0), (4,0), (5,0),(6,0), (7,0),
                   (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

black_pieces =  ["rook", "knight", "bishop", "king", "queen", "bishop", "kinght", "rook",
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]

black_locations = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)
                   (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]

captured_pieces_white = []
captured_pieces_black = []

#Ve los turnos y quien empieza 

turns_step = 0
selection = 100
valid_moves = []

# Imagenes de las piezas

image_urls = ['https://media.geeksforgeeks.org/wp-content/uploads/20240302025946/black_queen.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025948/black_king.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025345/black_rook.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025951/black_bishop.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025947/black_knight.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025945/black_pawn.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025952/white_queen.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025943/white_king.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025949/white_rook.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025944/white_bishop.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025325/white_knight.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025953/white_pawn.png']

# Cargar imagenes 

black_queen = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[0]).content)))
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[1]).content)))
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[2]).content)))
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[3]).content)))
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[4]).content)))
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[5]).content)))
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[6]).content)))
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[7]).content)))
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[8]).content)))
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[9]).content)))
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[10]).content)))
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[11]).content)))
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

# Cargar imagenes a las piezas

white_images = [white_pawn, white_queen, white_king,
                white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]

small_black_images = [black_knight_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list = ["pawn", "queen", "king", "knight", "rook", "bishop"]

# Chequeo

counter = 0
winner = ""
game_over = False

# main game

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, "light gray", [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, "light gray", [700 - (column * 200), row * 100, 100,100])
            pygame.draw.rect(screen, "gray", [0,800, Width, 100])
            pygame.draw.rect(screen, "gold", [0, 800 , Width, 100], 5)
            pygame.draw.rect(screen, "gold", [800, 0, 200, Height], 5)
            status_text = ["White: Select a Piece to Move!", "White: select a Destination!", "Black: select a piece to move!", "Black: selelct a destination!"]
            screen.blit(big_font.render(status_text[turns_step], True, "black"), (20, 820))
            for i in range(9):
                pygame.draw.line(screen, "black", (0,100 * i),(800, 100 * i),2)
                pygame.draw.line(screen, "black", (100 * i, 0), (100 * i, 800), 2)
                screen.blit(medium_font.render("Forfeit", True, "black"),(810, 830))

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == "pawn":
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        
        
                            
                        
