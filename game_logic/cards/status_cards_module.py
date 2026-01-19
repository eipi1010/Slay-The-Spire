from game_logic.cards.cards import Card
from game_logic.effects.player_effects import CardEffects, SelfExhaustEffect

status_cards = {
    "Slimed": Card(name="Slimed",mana=1,effects=CardEffects(effects=[SelfExhaustEffect()]))
}


