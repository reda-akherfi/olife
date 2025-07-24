import dotenv
dotenv.load_dotenv()

import streamlit as st
import pandas as pd
from core import db, insights

st.set_page_config(page_title="Weight & Mood Tracker", layout="centered")

st.header("📈 Weight / Mood Logger")

with st.form("log"):
    w = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, step=0.1)
    m = st.slider("Mood (1=bad, 5=great)", 1, 5, 3)
    if st.form_submit_button("Save"):
        db.add_entry(w, m)
        st.success("Saved!")

data = pd.DataFrame([e.__dict__ for e in db.get_entries()])
if not data.empty:
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    st.dataframe(data.sort_values("timestamp", ascending=False))

    # insights
    ins = insights.generate_insights(data)
    st.write(f"Spearman weight↔mood correlation: **{ins['corr']:.2f}**")
    st.line_chart(ins["forecast"].set_index("ds")["y"])
else:
    st.info("No entries yet. Add one above!")

# mnemonic banner
st.caption("💡 RF‑MD5 = RandomForest with max_depth 5 (safe default)")
