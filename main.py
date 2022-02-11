from tabulate import tabulate

rounds = {'ninguna_basa':'Ninguna Basa',
          'corazones': 'No Corazones',
          'j-k':'No J ni K', 
          'q': 'No Q', 
          'k_corazon': 'No K de Corazon',
          '2_ultimas': 'No 2 Ultimas',
          'positivas1': 'Positivas 1',
          'positivas2': 'Positivas 2',
          'positivas3': 'Positivas 3',
          'positivas4': 'Positivas 4'}


rounds_sum = {'ninguna_basa': -260,
              'corazones': -260,
              'j-k': -240,
              'q': -200,
              'k_corazon': -160,
              '2_ultimas': -180,
              'positivas1': 325,
              'positivas2': 325,
              'positivas3': 325,
              'positivas4': 325}

values = {'ninguna_basa': -20,
          'corazones': -20,
          'j-k': -30,
          'q': -50,
          'k_corazon':-160,
          '2_ultimas': -90,
          'positivas1': 25,
          'positivas2': 25,
          'positivas3': 25,
          'positivas4': 25}


def generate_scores():
    scores = {}
    for round_ in rounds:
        scores[round_] = None

    return scores


def get_players():
    print("Ingrese los jugadores en orden: \n")
    player1 = input("Jugador 1: ")
    player2 = input("Jugador 2: ")
    player3 = input("Jugador 3: ")
    player4 = input("Jugador 4: ")
    
    return [player1, player2, player3, player4]


def get_round_scores(players, round_):
    
    while True:
        print(f"\n---------{rounds[round_]}------------\n")
        print("Ingrese la cantidad para cada jugador: \n")
        scores = {}
        for player in players:
            scores[player] = int(input(f"{player}: "))*values[round_]
    
        if sum(list(scores.values())) == rounds_sum[round_]:
            while True:
                confirmation = input("Ingrese [c] para confirmar, o [r] para repetir conteo: ")
                if confirmation == 'c' or confirmation == 'r':
                    break
                
            if confirmation == 'c':
                break
        else:
            print("Porfavor verifique que los valores sean correctos y repita el conteo \n")
            
    
    return scores

def main():
    
    players = get_players()
    
    scores = generate_scores()
    
    for round_ in rounds.keys():
        
        if round_ in ['positivas1', 'positivas2', 'positivas3', 'positivas4']:
            reparte = int(round_[-1])-1
            muestra = int(round_[-1])
            if muestra == 4:
                muestra = 0
            print(f"\nReparte {players[reparte]}, pone la muestra {players[muestra]}")
        
        scores[round_] = get_round_scores(players, round_)
        
        if round_ == '2_ultimas':
            print("\n-------------- Resultados de las negativas ------------------\n")
            
            print(tabulate(list(scores.values())[:6], headers = "keys", tablefmt = "fancy_grid", showindex=list(rounds.values())[:6]))        
            
            valores = list(scores.values())[:6]
            negatives = {player:[sum([valor[player] for valor in valores])] for player in players}
            
            print(tabulate(negatives, headers = "keys", tablefmt = "fancy_grid", showindex=["Total"]))
            
            
            
            print("--------------- Empiezan las positias ----------------------\n")
            

    
    print("--------------------------- Resultados Finales ----------------------------------")
    
    print(tabulate(list(scores.values()), headers = "keys", tablefmt = "fancy_grid", showindex=list(rounds.values())))
    
    valores = list(scores.values())
    totales = {player:[sum([valor[player] for valor in valores])] for player in players}
    
    print(tabulate(totales, headers = "keys", tablefmt = "fancy_grid", showindex=["Total"]))

    
    print("----------Posiciones-----------")
    
    posiciones = sorted(totales, key = totales.get)[::-1]
    
    for i, player in enumerate(posiciones):
        print(f"{i+1}. {player}: {totales[player]}")
    
    
if __name__ == "__main__":
    main()