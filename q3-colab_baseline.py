# Run in Google Colab (Runtime > Change runtime type is optional; CPU is fine).
# Cell 1:  !pip -q install transformers torch
from transformers import pipeline
import pandas as pd

clf = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

messages = {
    "M1": "There is a water leak in Building C that has been running all morning.",
    "M2": "The accessible entrance near the main building has been blocked for two days.",
    "M3": "I want to report that one of our suppliers may not meet our sustainability policy.",
}
categories = ["Water", "Waste and recycling", "Energy",
              "Procurement and supplier governance", "Accessibility",
              "Health and safety", "Other"]
urgencies = ["LOW urgency", "MEDIUM urgency", "HIGH urgency", "CRITICAL urgency"]

rows = []
for mid, text in messages.items():
    c = clf(text, candidate_labels=categories)
    u = clf(text, candidate_labels=urgencies)
    rows.append({
        "message": mid,
        "baseline_category": c["labels"][0],
        "category_score": round(c["scores"][0], 2),
        "baseline_urgency": u["labels"][0].split()[0],
        "urgency_score": round(u["scores"][0], 2),
    })
df = pd.DataFrame(rows)
print(df.to_string(index=False))
df.to_csv("baseline_results.csv", index=False)
