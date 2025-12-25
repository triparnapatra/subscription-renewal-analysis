import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    df = pd.read_csv("data/subscriptions.csv")

    total_users = len(df)
    renewed = df["renewed"].sum()
    churned = total_users - renewed

    result = {
        "Total Users": total_users,
        "Renewed Users": renewed,
        "Churned Users": churned,
        "Renewal Rate (%)": round((renewed / total_users) * 100, 2)
    }

    labels = ["Renewed", "Churned"]
    values = [renewed, churned]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Subscription Renewal vs Churn")
    ax.set_xlabel("Status")
    ax.set_ylabel("Number of Users")

    return result, fig