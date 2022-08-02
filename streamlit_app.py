import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.scatter(np.random.normal(0,100,100),np.random.normal(0,100,100))
st.pyplot(fig)
