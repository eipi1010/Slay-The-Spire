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
        self._draw_discard_pile(player.discard_pile)
        self._draw_deck(player.deck)

        # 3. Draw UI (Energy, Draw/Discard Piles)
  #      self._draw_ui(player)

        pygame.display.flip()

    def _draw_player(self, player):
        img = self.assets.get('ironclad')
        scaled_width, scaled_height = 200,140
        scaled_img = pygame.transform.scale(img,(scaled_width,scaled_height))
        x,y = 150,200
        self.screen.blit(scaled_img, (x, y))
        # Add a Health Bar
        health_x,health_y = x+(scaled_width)/2,y+scaled_height
        pygame.draw.rect(self.screen,(0,0,0),(health_x, health_y,100,10))
        pygame.draw.rect(self.screen, (200, 0, 0), (health_x, health_y, 100*(player.health/player.max_health), 10))
        hp_text = self.font.render(f"{player.health}/{player.max_health}", True, (255, 255, 255))
        self.screen.blit(hp_text, (health_x, health_y))

        # Add a Mana Bar
        mana_x, mana_y = x+50,y+scaled_height
        pygame.draw.circle(self.screen,(200,100,0),(mana_x,mana_y),10)
        mana_text = self.font.render(f"{player.mana}/3",True,(255,255,255))
        self.screen.blit(mana_text,(mana_x,mana_y))

        #Add Blobk Bar
        if player.block > 0:
            block_x,block_y = x+(scaled_width)/2+100,y+scaled_height
            pygame.draw.rect(self.screen,(0,0,200),(block_x,block_y,20,20))
            block_text = self.font.render(f"{player.block}",True,(255,255,255))
            self.screen.blit(block_text,(block_x,block_y))
            

    def _draw_enemies(self, enemies):
        for i, enemy in enumerate(enemies):
            # Dynamic lookup based on monster name
            img = self.assets.get(enemy.name.lower().replace(" ", "_"))
            if img:
                x,y = 800, 100+i*150
                scaled_width,scaled_height = 130, 140
                scaled_img = pygame.transform.scale(img,(scaled_width,scaled_height))
                self.screen.blit(scaled_img, (x, y))
                
                #Add a Health Bar
                health_x,health_y = x+scaled_width/2,y+scaled_height
                pygame.draw.rect(self.screen,(0,0,0),(health_x,health_y,100,10))
                pygame.draw.rect(self.screen,(200,0,0),(health_x,health_y,100*(enemy.health/enemy.max_health),10))
                hp_text = self.font.render(f"{enemy.health}/{enemy.max_health}", True, (255,255,255))
                self.screen.blit(hp_text,(health_x,health_y))

    def _draw_hand(self, hand):
        if len(hand) == 0:
            return
        for i, card in enumerate(hand):
            # Draw card images at the bottom
            card_img = self.assets.get(card.name.lower())
            if card_img:
                # Scale cards slightly for the hand
                scaled_card = pygame.transform.scale(card_img, (100, 140))
                self.screen.blit(scaled_card, (300 + (i * 110), 520))

    def _draw_discard_pile(self, discard_pile):
        if len(discard_pile) == 0:
            return
        for i, card in enumerate(discard_pile):
            card_img = self.assets.get(card.name.lower())
            if card_img:
                scaled_card = pygame.transform.scale(card_img,(100,140))
                self.screen.blit(scaled_card,(1100, 25 + (i*50)))

    def _draw_deck(self,deck):
        if len(deck) == 0: return
        for i,card in enumerate(deck):
            card_img = self.assets.get(card.name.lower())
            if card_img:
                scaled_card = pygame.transform.scale(card_img,(100,140))
                self.screen.blit(scaled_card,(50, 25 + i*50))
