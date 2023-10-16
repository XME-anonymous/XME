import os
import pandas as pd
from rich.pretty import pprint

LOG = "/home/anonymous-xme/mend/mend/logs/exp_1_mbert_finetuned_gujarati_all"
MODEL = "mbert-uncased-gujarati-all"

l1_list = ["english", "hindi", "spanish", "french", "bengali", "gujarati"]

data = []
for row in l1_list:
    r_dt = {"-": row.capitalize()}
    # print(row)
    for col in l1_list:
        # print(col, end="\t")
        with open(f"{LOG}/{row}/mend-mbert-{row}-{col}-{MODEL}.txt", "r") as f:
            for line in f:
                if "edit/acc_val        :  " in line:
                    val = line.strip().split("edit/acc_val        :  ")[1]
                    # print(val)
                    break
        r_dt[col.capitalize()] = val
        del val
    data.append(r_dt)

df = pd.DataFrame(data)
df.index = df["-"]
df = df.drop("-", axis=1)
# print dataframe with tab spacing
print(df.to_string(float_format=lambda x: "%.3f" % x))
# print dataframe to clipboard
