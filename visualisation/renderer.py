import pygame

class GameRenderer:
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        self.font = pygame.font.SysFont("Arial", 24)
        self.small_font = pygame.font.SysFont("Arial", 18)

    def draw_state(self, player, enemies):
        """Draws the entire game state in one call."""
        self.screen.fill((40, 40, 40)) # Background

        # 1. Draw Entities
        self._draw_player(player)
        self._draw_enemies(enemies)

        # 2. Draw Hand
        self._draw_hand(player.hand)

        # 3. Draw UI (Energy, Draw/Discard Piles)
  #      self._draw_ui(player)

        pygame.display.flip()

    def _draw_player(self, player):
        img = self.assets.get('ironclad')
        self.screen.blit(img, (150, 300))
        # Add a Health Bar
        pygame.draw.rect(self.screen, (200, 0, 0), (150, 280, 100, 10))
        hp_text = self.font.render(f"{player.health}/87", True, (255, 255, 255))
        self.screen.blit(hp_text, (150, 250))

    def _draw_enemies(self, enemies):
        for i, enemy in enumerate(enemies):
            # Dynamic lookup based on monster name
            img = self.assets.get(enemy.name.lower().replace(" ", "_"))
            if img:
                self.screen.blit(img, (800, 250 + (i * 150)))

    def _draw_hand(self, hand):
        for i, card in enumerate(hand):
            # Draw card images at the bottom
            card_img = self.assets.get(card.name.lower())
            if card_img:
                # Scale cards slightly for the hand
                scaled_card = pygame.transform.scale(card_img, (100, 140))
                self.screen.blit(scaled_card, (300 + (i * 110), 520))