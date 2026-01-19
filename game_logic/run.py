from cards.ironclad_cards_module import ironclad_cards
from entities.players.player import Player
import copy
from game_events.fight_all_event import FightAll
from entities.creatures.monster_pool_module import monster_pool



card_names = ["Strike"]*5 + ["Defend"]*4 + ["Bash"]
deck = [copy.deepcopy(ironclad_cards[name]) for name in card_names]
player = Player(deck,87)
Event = FightAll(monster_pool)

Event.execute(player,100)





