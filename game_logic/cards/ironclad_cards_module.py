from game_logic.cards.cards import Card
from game_logic.effects.player_effects import CardEffects, DamageEffect, SelfDiscardEffect, BlockEffect, VulnerableEffect,DuplicateToDiscardPileEffect

ironclad_cards = {

    "Strike": Card(name="Strike",mana=1,effects = CardEffects([DamageEffect(6),SelfDiscardEffect()])),
    "Defend": Card(name="Defend",mana=1,effects=CardEffects([BlockEffect(5),SelfDiscardEffect()])),
    "Bash": Card(name="Bash",mana=1,effects=CardEffects([DamageEffect(8),VulnerableEffect(2),SelfDiscardEffect()])),
    "Anger": Card(name="Anger",mana=0,effects=CardEffects([DamageEffect(6),DuplicateToDiscardPileEffect(1),SelfDiscardEffect()])),
    "Armaments": Card(name="Armaments",mana=1,effects=CardEffects([BlockEffect(5),UpgradeRandomCardInHandEffect(1),SelfDiscardEffect()])),
    
   # "Shrug It Off": Card(name="Shrug It Off",damage=0,block=8,mana=1,draw=1),
   # "Twin Strike": Card(name="Twin Strike",damage=10,block=0,mana=1),
   # "Sword Boomerang": Card(name="Sword Boomerang",damage=9,block=0,mana=1),
   # "strike": Card(damage=6,block=0,mana=1),
   # "strike": Card(damage=6,block=0,mana=1)
}

