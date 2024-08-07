import pandas as pd
import numpy as np

df = pd.read_csv("test.csv")
for i in range(3000):
    df += pd.read_csv("test.csv")

df.to_csv("big.csv")
