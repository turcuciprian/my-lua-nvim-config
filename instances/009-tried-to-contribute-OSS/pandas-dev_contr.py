import pandas as pd

df = pd.DataFrame({"ticker": ["#1234#"], "name": [None]})

#df.replace({col: {r"^#": "$"} for col in df.columns}, regex=True)  # raises
df = df.replace({col: {"123": "x"} for col in df.columns}, regex=True)  # raises
breakpoint()
df = df.fillna("").replace({col: {r"^#": "$"} for col in df.columns}, regex=True)  # works
df= df.astype(str).replace({col: {r"^#": "$"} for col in df.columns}, regex=True)  # works
breakpoint()
df.astype(pd.StringDtype()).replace({col: {r"^#": "$"} for col in df.columns}, regex=True)  # works
breakpoint()
