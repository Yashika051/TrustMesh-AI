from fastapi import FastAPI
import pandas as pd
from api.data_loader import df, recommendations, explanations, graph_data, profiles

app = FastAPI(title="TrustMesh AI API")


@app.get("/")
def home():
    return {"message": "TrustMesh AI API is running"}


@app.get("/businesses")
def get_businesses():
    businesses = df[
        [
            "business_id",
            "owner_id",
            "business_type",
            "environment_type",
            "location"
        ]
    ].drop_duplicates("business_id")

    return businesses.to_dict(orient="records")


@app.get("/businesses/{business_id}")
def get_business(business_id: str):
    business = df[df["business_id"] == business_id]

    if business.empty:
        return {"message": "Business not found"}

    latest = business.sort_values("month").tail(1)

    latest = latest.astype(object).where(pd.notna(latest), None)

    return latest.to_dict(orient="records")[0]


@app.get("/businesses/{business_id}/reputation")
def get_reputation(business_id: str):
    business = df[df["business_id"] == business_id]

    if business.empty:
        return {"message": "Business not found"}

    latest = business.sort_values("month").tail(1).iloc[0]

    return {
        "business_id": latest["business_id"],
        "economic_reputation_index": latest["economic_reputation_index"],
        "financial_health_pct": latest["financial_health_pct"],
        "operational_stability_pct": latest["operational_stability_pct"],
        "resilience_pct": latest["resilience_pct"]
    }


@app.get("/businesses/{business_id}/recommendations")
def get_recommendations(business_id: str):
    business = recommendations[
        recommendations["business_id"] == business_id
    ]

    if business.empty:
        return {"message": "Business not found"}

    return business.to_dict(orient="records")[0]


@app.get("/businesses/{business_id}/explanation")
def get_explanation(business_id: str):
    business = explanations[
        explanations["business_id"] == business_id
    ]

    if business.empty:
        return {"message": "Business not found"}

    return business.to_dict(orient="records")[0]


@app.get("/businesses/{business_id}/simulate")
def simulate_business(business_id: str, scenario: str):
    business = profiles[profiles["business_id"] == business_id]

    if business.empty:
        return {"message": "Business not found"}

    business = business.iloc[0]

    baseline_cash_flow = business["net_cash_flow"]

    if scenario == "demand_drop":
        simulated_cash_flow = baseline_cash_flow * 0.80

    elif scenario == "supply_disruption":
        simulated_cash_flow = baseline_cash_flow * 0.85

    elif scenario == "operating_cost_increase":
        simulated_cash_flow = (
            baseline_cash_flow - (business["monthly_expenses"] * 0.15)
        )

    else:
        return {"message": "Invalid scenario"}

    impact = simulated_cash_flow - baseline_cash_flow
    impact_pct = (impact / baseline_cash_flow) * 100

    return {
        "business_id": business_id,
        "scenario": scenario,
        "baseline_cash_flow": round(baseline_cash_flow, 2),
        "simulated_cash_flow": round(simulated_cash_flow, 2),
        "impact": round(impact, 2),
        "impact_pct": round(impact_pct, 2)
    }


@app.get("/businesses/{business_id}/graph")
def get_business_graph(business_id: str):
    business = graph_data[
        graph_data["business_id"] == business_id
    ]

    if business.empty:
        return {"message": "Business not found"}

    business = business.iloc[0]

    return {
        "business_id": business["business_id"],
        "business_type": business["business_type"],
        "environment": business["environment_type"],
        "location": business["location"],
        "shock": None if pd.isna(business["shock_type"]) else business["shock_type"]
    }


@app.get("/businesses/{business_id}/overview")
def get_business_overview(business_id: str):
    business = profiles[
        profiles["business_id"] == business_id
    ]

    if business.empty:
        return {"message": "Business not found"}

    business = business.iloc[0]

    recommendation = recommendations[
        recommendations["business_id"] == business_id
    ]

    explanation = explanations[
        explanations["business_id"] == business_id
    ]

    return {
        "business_id": business_id,
        "business_type": business["business_type"],
        "environment": business["environment_type"],
        "location": business["location"],
        "economic_reputation_index": business["economic_reputation_index"],
        "reputation_status": explanation.iloc[0]["reputation_status"],
        "recommendation_priority": recommendation.iloc[0]["recommendation_priority"],
        "recommendations": recommendation.iloc[0]["recommendations"],
        "explanation": explanation.iloc[0]["explanation"]
    }