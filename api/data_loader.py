import pandas as pd


df = pd.read_csv("data/trustmesh_economic_data.csv")

df["month"] = pd.to_datetime(df["month"])

print("Dataset loaded:", df.shape)


recommendations = pd.read_csv("data/business_recommendations.csv")

print("Recommendations loaded:", recommendations.shape)


explanations = pd.read_csv("data/business_explanations.csv")

print("Explanations loaded:", explanations.shape)


profiles = (
    df.sort_values("month")
      .groupby("business_id")
      .tail(1)
      .reset_index(drop=True)
)

print("Business profiles loaded:", profiles.shape)


graph_data = profiles[
    [
        "business_id",
        "business_type",
        "environment_type",
        "location",
        "shock_type"
    ]
].copy()

print("Graph data loaded:", graph_data.shape)