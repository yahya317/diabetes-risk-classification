import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("diabetes_binary_health_indicators_BRFSS2015.csv")
target = "Diabetes_binary"

work, report = train_test_split(
    df, test_size=0.20, stratify=df[target], random_state=42
)

work.to_csv("working_set.csv", index=False)
report.to_csv("reporting_set.csv", index=False)

print(len(work), len(report)) 
print(work[target].mean(), report[target].mean()) 