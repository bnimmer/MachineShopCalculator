
import streamlit as st

st.title("Segment Length Calculator with Cut Loss")

D = st.number_input("Enter total distance (D):", min_value=0.0, value=1000.0)
n = st.number_input("Enter number of segments (n):", min_value=1, value=5)
L = st.number_input("Enter loss per cut (L):", min_value=0.0, value=2.0)

if n > 0:
    total_loss = (n - 1) * L
    if D < total_loss:
        st.error("Total loss exceeds the given distance. Please adjust your inputs.")
    else:
        segment_length = (D - total_loss) / n
        st.success(f"Each segment will be {segment_length:.2f} units long.")
