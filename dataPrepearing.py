import pandas as pd
music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
X
