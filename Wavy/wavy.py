import numpy as np
import pandas as pd
import wavy
from wavy import models

# Start with any time-series dataframe:
df = pd.DataFrame({'price': np.random.randn(1000)}, index=range(1000))

# Create panels. Each panel is a frame collection.
x, y = wavy.create_panels(df, lookback=3, horizon=1)

# x and y contain the past and corresponding future data.
# lookback and horizon are the number of timesteps.
print("Lookback:", x.num_timesteps)
print("Horizon:", y.num_timesteps)

# Set train-val-test split. Defaults to 0.7, 0.2 and 0.1, respectively.
wavy.set_training_split(x, y)

# Instantiate a model:
model = models.LinearRegression(x, y)
model.score()
