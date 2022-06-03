import pandas as pd


def read_from_csv():
    data = pd.read_csv("./test.csv")
    return data


df = read_from_csv()
df["result"] = df.a + df.b
all_sum = df.result.sum()
print("sum:", all_sum)
