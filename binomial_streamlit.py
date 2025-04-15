import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

st.set_page_config(page_title="Coin Toss Binomial Distribution", layout="wide")

st.title("🪙 Coin Toss Binomial Distribution Simulator")

# Sidebar inputs
st.sidebar.header("Simulation Settings")
n = st.sidebar.slider("Number of Tosses (n)", min_value=10, max_value=1000, value=100, step=10)
k = st.sidebar.slider("Highlight Outcomes with This Many Heads (k)", min_value=0, max_value=n, value=n // 2)
p = 0.5  # Fixed probability of heads

st.write(f"### Tossing a coin {n} times with a 0.50 chance of heads")

# X-axis values
x = np.arange(0, n + 1)

# Binomial PMF
binomial_pmf = binom.pmf(x, n, p)

# Probability of getting exactly k heads
prob_k = binom.pmf(k, n, p)
st.markdown(f"#### Probability of getting exactly {k} heads: **{prob_k:.4f}**")

# Color setup
colors = ['red' if i == k else 'skyblue' for i in x]

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
- **p** is fixed at 0.5 (fair coin).
- **k** lets you highlight a specific number of heads in red.

Use the sliders to adjust parameters and see how the distribution changes!
""")
