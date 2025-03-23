import pygame
import sys
from classes import TextAnalyzer,Stack,Queue

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Analysis Tool")

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)  # Light Blue for buttons
GREEN = (144, 238, 144)  # Light Green for input box

# Fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 48)
comment_font = pygame.font.Font(None, 28)

# Input Box
input_box = pygame.Rect(50, 90, 700, 50)
text_input = ""
results = ""

# Button Setup
buttons = [
    {"label": "Character Analysis", "rect": pygame.Rect(50, 150, 250, 50), "color": LIGHT_BLUE},
    {"label": "Word Analysis", "rect": pygame.Rect(300, 150, 250, 50), "color": LIGHT_BLUE},
    {"label": "Reverse Text (Stack)", "rect": pygame.Rect(550, 150, 250, 50), "color": LIGHT_BLUE},
    {"label": "FIFO Words", "rect": pygame.Rect(50, 210, 250, 50), "color": LIGHT_BLUE},
    {"label": "Word Count", "rect": pygame.Rect(300, 210, 250, 50), "color": LIGHT_BLUE},
]

# Title
title_text = "Text Analysis Tool"
title_surface = title_font.render(title_text, True, BLACK)
title_rect = title_surface.get_rect(center=(WIDTH // 2, 50))

#  comment
comment_text = "Just Click on the textbox and start typing, click on any button to analyze your text 🙌"
comment_surface = comment_font.render(comment_text, True, BLACK)
comment_rect = comment_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))

# Main Loop
running = True
while running:
    screen.fill(WHITE)

    # Draw title
    screen.blit(title_surface, title_rect)
    screen.blit(comment_surface, comment_rect)
    # Draw Input Box (with green color)
    pygame.draw.rect(screen, GREEN, input_box, 0)  # fill the input box with green
    pygame.draw.rect(screen, BLACK, input_box, 2)  # border in black
    input_text_surface = font.render(text_input, True, BLACK)
    screen.blit(input_text_surface, (input_box.x + 10, input_box.y + 10))

    # Draw Buttons with different colors
    for button in buttons:
        pygame.draw.rect(screen, button["color"], button["rect"])  # fill button with its color
        pygame.draw.rect(screen, BLACK, button["rect"], 2)  # border for button
        label_surface = font.render(button["label"], True, BLACK)
        screen.blit(label_surface, (button["rect"].x + 10, button["rect"].y + 10))

    # Draw Results Area
    results_surface = font.render(results, True, BLUE)
    screen.blit(results_surface, (50, 300))

    # Event Handling
    try:
        textanalyze = TextAnalyzer(text_input)
    except ValueError:
        results = "Error: Please enter valid text."

    stack = Stack()
    queue = Queue()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
            else:
                text_input += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["label"] == "Character Analysis":
                            results = str(textanalyze.character_analysis())
                        elif button["label"] == "Word Analysis":
                            results = str(textanalyze.word_analysis())
                        elif button["label"] == "Reverse Text (Stack)":
                            results = stack.reverse_text(text_input)
                        elif button["label"] == "FIFO Words":
                            results = queue.reverse_word(text_input)
                        elif button["label"] == "Word Count":
                            results = f"Word Count: {textanalyze.word_count()}"

    # Update Display
    pygame.display.flip()

pygame.quit()
sys.exit()
