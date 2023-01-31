import os

import pandas as pd

os.chdir()

all_filenames = ["RecipeDataDirty(1).csv","RecipeDataDirty(2).csv","RecipeDataDirty(3).csv"]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')