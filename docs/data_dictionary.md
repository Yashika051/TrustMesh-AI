# TrustMesh AI — Data Dictionary

This document describes the fields contained in the synthetic TrustMesh AI economic dataset.

**Dataset:** `trustmesh_economic_data.csv`  
**Rows:** 12,000  
**Columns:** 32  

| Column | Data Type | Description | Category |
|---|---|---|---|
| `business_id` | string | Unique identifier assigned to each business. | Identity |
| `owner_id` | string | Unique identifier assigned to each business owner. | Identity |
| `business_type` | string | Type of informal business. | Identity |
| `environment_type` | string | Operating environment of the business. | Context |
| `location` | string | Geographic location assigned to the business. | Context |
| `month` | datetime | Monthly observation period. | Time |
| `monthly_income` | float | Simulated monthly business income before seasonal and shock adjustments. | Financial |
| `monthly_expenses` | float | Simulated monthly operating expenses. | Financial |
| `transaction_count` | integer | Approximate number of monthly business transactions. | Financial |
| `digital_payment_pct` | float | Estimated percentage of transactions conducted digitally. | Financial |
| `supplier_payment_amount` | float | Estimated monthly amount paid to suppliers. | Financial |
| `utility_payment_amount` | float | Estimated monthly utility payments. | Financial |
| `rent_payment` | float | Estimated monthly business-related rent payment. | Financial |
| `savings_amount` | float | Estimated monthly savings based on available cash. | Financial |
| `net_cash_flow` | float | Monthly income remaining after core expenses, rent, and utilities. | Financial |
| `payment_discipline_pct` | float | Estimated consistency of making expected payments on time. | Behavioral |
| `supplier_reliability_pct` | float | Estimated reliability of the business in supplier-related activity. | Behavioral |
| `business_continuity_pct` | float | Estimated consistency of business operations over time. | Behavioral |
| `demand_stability_pct` | float | Estimated stability of customer demand. | Behavioral |
| `seasonal_factor` | float | Monthly seasonal multiplier applied to income. | Temporal |
| `seasonally_adjusted_income` | float | Income adjusted according to the seasonal factor. | Derived |
| `shock_type` | string | Economic condition affecting the monthly observation. | Shock |
| `shock_factor` | float | Multiplier representing the effect of the economic shock. | Shock |
| `adjusted_income` | float | Income after applying seasonal and shock effects. | Derived |
| `adjusted_expenses` | float | Expenses after applying relevant operating-cost shock effects. | Derived |
| `adjusted_cash_flow` | float | Cash flow after adjusted income, expenses, rent, and utilities. | Derived |
| `cash_flow_margin_pct` | float | Adjusted cash flow expressed as a percentage of adjusted income. | Derived |
| `expense_burden_pct` | float | Adjusted expenses expressed as a percentage of adjusted income. | Derived |
| `operational_stability_pct` | float | Composite indicator based on payment discipline, supplier reliability, continuity, and demand stability. | Reputation |
| `financial_health_pct` | float | Composite indicator representing financial health using cash flow, expense burden, and payment discipline. | Reputation |
| `resilience_pct` | float | Composite indicator representing operational and economic resilience. | Reputation |
| `economic_reputation_index` | float | Explainable composite index combining financial health, operational stability, resilience, and payment discipline. | Reputation |
