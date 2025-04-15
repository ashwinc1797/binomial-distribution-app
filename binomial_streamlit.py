import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

st.set_page_config(page_title="Coin Toss Binomial Distribution", layout="wide")

st.title("🪙 Coin Toss Binomial Distribution Simulator")

# Sidebar inputs
st.sidebar.header("Simulation Settings")
n = st.sidebar.slider("Number of Tosses (n)", min_value=10, max_value=1000, value=100, step=10)
p = st.sidebar.slider("Probability of Heads (p)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
k = st.sidebar.slider("Highlight Outcomes with This Many Heads (k)", min_value=0, max_value=n, value=n // 2)

st.write(f"### Tossing a coin {n} times with a {p:.2f} chance of heads")

# X-axis values
x = np.arange(0, n + 1)

# Binomial PMF
binomial_pmf = binom.pmf(x, n, p)

# Probability of getting exactly k heads
prob_k = binom.pmf(k, n, p)
st.markdown(f"#### Probability of getting exactly {k} heads: **{prob_k:.4f}**")

# Color setup
colors = ['red' if i == k else 'skyblue' for i in x]

# Hypothesis Testing Explanation
st.subheader("🧪 Hypothesis Testing")
st.markdown("""
- **Null Hypothesis (H₀):** The coin is fair → Probability of heads = Probability of tails = 0.5
- **Alternative Hypothesis (H₁):** The coin is biased → Probability of heads **>** 0.5
""")

# One-tailed test (right-tailed)
alpha = 0.05
p_null = 0.5

# Calculate critical value for one-tailed test
critical_value = binom.ppf(1 - alpha, n, p_null)

if k > critical_value:
    st.markdown(f"❌ **Result:** We reject the null hypothesis at α = 0.05. The observed number of heads ({k}) is significantly higher than expected under fairness.")
else:
    st.markdown(f"✅ **Result:** We fail to reject the null hypothesis. The observed number of heads ({k}) does not provide strong enough evidence against fairness.")

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(x, binomial_pmf, color=colors, edgecolor='black')
ax.set_title(f"Binomial Distribution: {n} Tosses, p = {p}")
ax.set_xlabel("Number of Heads")
ax.set_ylabel("Probability")
plt.tight_layout()

# Show plot in Streamlit
st.pyplot(fig)

# Info
st.markdown("""
This app simulates the **binomial distribution** of tossing a coin multiple times.

- **n** is the number of tosses.
- **p** is the probability of getting heads.
- **k** lets you highlight a specific number of heads in red.
- Includes a one-tailed hypothesis test assuming a fair coin (p = 0.5).
""")
