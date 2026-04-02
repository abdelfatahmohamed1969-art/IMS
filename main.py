import pandas as pd
from analyzer import analyze_kpi

# Read data
df = pd.read_csv("data/sample.csv")

for i, row in df.iterrows():
    call_psr, sms_psr, psi_psr, issues = analyze_kpi(row)

    print("========== KPI Analysis ==========")
    print(f"Call PSR: {call_psr:.2f}%")
    print(f"SMS PSR: {sms_psr:.2f}%")
    print(f"PSI PSR: {psi_psr:.2f}%")

    print("\nDetected Issues:")
    for key, value in issues.items():
        print(f"{key}: {value}")
