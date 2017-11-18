import edpanalyst
import pandas as pd

ses = edpanalyst.Session('aslvrstn')
pm = ses.popmod('pm-qwkiu3a3nf65qajn')

def simulate_game():
  game = pm.simulate(given=pd.DataFrame({'ball': [str(b) for b in range(1, 6)]}), n=1)
  num_extra_balls = game['extra_balls'].astype(int).sum()
  num_extra_balls = min(num_extra_balls, 2)  # Cap this to 2 for now
  if num_extra_balls:
    extra_balls = pm.simulate(given=pd.DataFrame({'ball': [str(b) for b in range(6, 6 + num_extra_balls)]}), n=1)
    game = game.append(extra_balls)

  game = game.reset_index()
  del game['sim']
  del game['given_row']
  return game

for _ in range(50):
  game = simulate_game()
  score = game['score'].sum()
  if score > 1500000:
    print(game)
    print(score)
