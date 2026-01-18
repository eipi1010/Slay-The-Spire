from cards.cards_class import Card
from effects.player_effects import CardEffects, DamageEffect, SelfDiscardEffect, SelfExhaustEffect

status_cards = {
    "Slimed": Card(name="Slimed",mana=1,effects=CardEffects(effects=[SelfExhaustEffect()]))
}


