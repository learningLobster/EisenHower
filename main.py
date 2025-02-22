import sys
import pygame
import utils
import config
import pyautogui as popup






class Window:
    def __init__(self):
        pygame.init()

        self.width = utils.WIDTH
        self.height = utils.HEIGHT

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('EisenHower')  # sets the window title

        self.top_left = pygame.Surface(
            [
                config.width_prct(self.width, 50),
                config.height_prct(self.height, 50)
            ]
        )
        self.top_right = pygame.Surface(
            [
                config.width_prct(self.width, 50),
                config.height_prct(self.height, 50)
            ]
        )
        self.bottom_left = pygame.Surface(
            [
                config.width_prct(self.width, 50),
                config.height_prct(self.height, 50)
            ]
        )
        self.bottom_right = pygame.Surface(
            [
                config.width_prct(self.width, 50),
                config.height_prct(self.height, 50)
            ]
        )

        self.all_frames_array = [self.top_left, self.top_right, self.bottom_left, self.bottom_right]

        # TEXT
        pygame.font.init()
        self.HEADER_TEXT_SIZE = int(config.width_prct(self.screen.get_width() // 2, 5))
        self.BODY_TEXT_SIZE = int(config.width_prct(self.screen.get_width() // 2, 3))

        self.header_font = pygame.font.SysFont("arial", self.HEADER_TEXT_SIZE)  # Font
        self.body_font = pygame.font.SysFont("lucidasans", self.BODY_TEXT_SIZE)  # Font

        # SURFACE FILL
        gray_shade_rgb = (105, 101, 101)
        self.top_left.fill('midnightblue')
        self.top_right.fill(gray_shade_rgb)
        self.bottom_left.fill('dimgray')
        self.bottom_right.fill('darkblue')

        self.HINT = "Press 'a' to add an new element"

        self.clock = pygame.time.Clock()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.add_to_matrix()

    def add_to_matrix(self):
        element = popup.prompt(text="...", title="User Input")
        # importance = None
        importance_popup = popup.confirm(
            text="Is it important?",
            title="Importance",
            buttons=['Yes', 'No', 'Exit']
        )
        match importance_popup:
            case 'Yes':
                importance = "Important"
            case 'No':
                importance = "Not important"
            case _:
                return

        urgency = None
        urgency_popup = popup.confirm(
            text="Is it urgent?",
            title="Urgency",
            buttons=['Yes', 'No', 'Exit']
        )
        match urgency_popup:
            case 'Yes':
                urgency = "Urgent"
            case 'No':
                urgency = "Not urgent"
            case _:
                return

        importance = importance.lower(); urgency = urgency.lower()
        config.add_element(utils.MATRIX, element, importance, urgency)

    def display_box_label(self, screen, text_list, font):
        # Paragraphs elements
        for index, text in enumerate(text_list):
            frame = screen[index]
            x = config.width_prct(frame.get_width(), 50)  # x coords
            y = config.height_prct(frame.get_height(), 5)  # y coords
            paragraph_text = font.render(text, True, 'white')
            paragraph_rect = paragraph_text.get_rect()
            paragraph_rect.center = (x, y)
            frame.blit(paragraph_text, paragraph_rect)

    def display_hint_text(self, screen, text, percentage_height, percentage_width, font, color='white'):
        # Paragraphs elements
        x = config.width_prct(screen.get_width(), percentage_width)  # x coords
        y = config.height_prct(screen.get_height(), percentage_height)  # y coords
        paragraph_text = font.render(text, True, color)
        paragraph_rect = paragraph_text.get_rect()
        paragraph_rect.center = (x, y)
        screen.blit(paragraph_text, paragraph_rect)

    def display_matrix_elements(self, frames_list, font):
        for index1, frame in enumerate(frames_list):
            for index2, element in enumerate(utils.MATRIX[index1]):
                x = config.width_prct(frame.get_width(), 10)  # x coords
                y = config.height_prct(frame.get_height(), 15 + (10 * index2))  # y coords
                frame_text = font.render(element, True, 'white')
                frame_rect = frame_text.get_rect()
                frame_rect.topleft = (x, y)
                frame.blit(frame_text, frame_rect)

    def mainloop(self):
        while True:
            self.event_handler()
            self.screen.blit(self.top_left, (0, 0))
            self.screen.blit(self.top_right, (config.width_prct(self.height, 50), 0))
            self.screen.blit(self.bottom_left, (0, config.height_prct(self.height, 50)))
            self.screen.blit(self.bottom_right, (config.width_prct(self.width, 50), config.height_prct(self.width, 50)))
            self.display_box_label(self.all_frames_array, utils.TEXT_LIST, self.header_font)
            self.display_hint_text(self.screen, self.HINT, 95, 50, self.header_font)
            self.display_matrix_elements(self.all_frames_array, self.body_font)

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    window = Window()
    window.mainloop()
