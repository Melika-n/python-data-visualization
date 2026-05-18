import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Ali", "Zahra", "Mehdi", "Sara", "Narges"],
    "Study Hours": [4, 6, 2, 7, 3],
    "Score": [65, 85, 50, 90, 60],
    "Daily Study (%)": [30, 40, 20, 50, 25],
    "Fun (%)": [25, 20, 30, 15, 35],
    "Sleep (%)": [45, 40, 50, 35, 40],
}

df = pd.DataFrame(data)
print(df)

# نمودار خطی

plt.plot(
    df["Name"],
    df["Study Hours"],
    marker="o",
    color="steelblue",
    linestyle="dashed",
    linewidth=2,
)
plt.title("Study Hours per Student")
plt.xlabel("Student Name")
plt.ylabel("Study Hours per Week")
plt.grid(True, alpha=0.3)
plt.show()


# نمودار ستونی

plt.bar(
    df["Name"], df["Score"], color="lightcoral", edgecolor="black", width=0.1, alpha=0.3
)
plt.title("Students Scores")
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.show()


# نمودار دایره ای

narges_data = df[df["Name"] == "Narges"]
study_pct = narges_data["Daily Study (%)"].values[0]
fun_pct = narges_data["Fun (%)"].values[0]
sleep_pct = narges_data["Sleep (%)"].values[0]

labels = ["sleep", "fun", "study"]
sizes = [sleep_pct, fun_pct, study_pct]
explode = [0, 0, 0.1]

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    explode=explode,
    startangle=90,
)
plt.title("Narges's day")
plt.show()

# نمودار پراکندگی
colors = ["blue", "green", "red", "orange", "purple"]

plt.scatter(
    df["Study Hours"],
    df["Score"],
    alpha=0.7,
    marker="s",
    c=colors,
    edgecolors="black",
)
plt.title("Results")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.show()
