from cards.cards_class import Card
from effects.player_effects import CardEffects, DamageEffect, SelfDiscardEffect, SelfExhaustEffect

status_cards = {
    "Slimed": Card(name="Slimed",mana=1,effects=CardEffects(effects=[SelfExhaustEffect()]))
}

ironclad_cards = {
    "Strike": Card(name="Strike",mana=1,effects = CardEffects(effects=[DamageEffect(amount=5),SelfDiscardEffect()]))
   # "Defend": Card(name="Defend",damage=0,block=5,mana=1),
   # "Bash": Card(name="Bash",damage=6,block=0,mana=2),
   # "Shrug It Off": Card(name="Shrug It Off",damage=0,block=8,mana=1,draw=1),
   # "Twin Strike": Card(name="Twin Strike",damage=10,block=0,mana=1),
   # "Sword Boomerang": Card(name="Sword Boomerang",damage=9,block=0,mana=1),
   # "strike": Card(damage=6,block=0,mana=1),
   # "strike": Card(damage=6,block=0,mana=1)
}
