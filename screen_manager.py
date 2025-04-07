class ScreenManager:
    def __init__(self):
        self.current_screen = None

    def change_screen(self, new_screen):
        self.current_screen = new_screen

    def handle_events(self, events):
        if self.current_screen:
            self.current_screen.handle_events(events)

    def update(self):
        if self.current_screen:
            self.current_screen.update()

    def draw(self, surface):
        if self.current_screen:
            self.current_screen.draw(surface)
