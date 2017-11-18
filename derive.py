import pandas as pd

df = pd.read_csv('pinball.csv')

# Figure out the score per ball from the end score
df['score'] = 0
for i, row in df.iterrows():
    prev = 0 if row['ball'] == 1 else df['score_at_end'][i-1]
    df['score'][i] = row['score_at_end'] - prev

# Wipe out our bonus if we tilted
df['effective_bonus'] = df['bonus'] * ~df['tilt']
df['effective_bonus_x'] = df['bonus_x'] * ~df['tilt']

del df['score_at_end']


df.to_csv('derived_pinball.csv', index=False)
