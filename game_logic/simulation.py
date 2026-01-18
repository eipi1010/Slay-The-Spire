
from battle import Battle   
from cards.ironclad_cards_module import ironclad_cards
from entities.players.player import Player
from entities.creatures.monster_types.slimeboss import SlimeBoss

def run_simulation(iterations=100):
    win_count = 0

    for i in range(iterations):
    # Pass the class SlimeBoss, not an instance, to the Battle
        deck = [ironclad_cards[name] for name in ["Strike"]*5 + ["Defend"]*4 + ["Bash"]]
        player = Player(deck,87)
        enemies = [SlimeBoss( )]
        battle = Battle(player, enemies, verbose=i == 0)
        if battle.run():
            win_count += 1
    
    print(f"Results after {iterations} simulations:")
    print(f"Wins: {win_count} | Losses: {iterations - win_count}")
    print(f"Win Rate: {(win_count/iterations)*100}%")

if __name__ == "__main__":
    run_simulation(100)