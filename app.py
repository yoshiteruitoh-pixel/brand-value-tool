import streamlit as st

st.title("ブランド価値診断ツール")

st.write("ブランド価値創造論 授業用")

brand = st.text_input("ブランド名")

function = st.slider("機能性", 1, 10, 5)
design = st.slider("デザイン性", 1, 10, 5)
worldview = st.slider("世界観", 1, 10, 5)
originality = st.slider("独自性", 1, 10, 5)
experience = st.slider("体験価値", 1, 10, 5)
trust = st.slider("信頼性", 1, 10, 5)

if st.button("診断する"):
    avg = (
        function
        + design
        + worldview
        + originality
        + experience
        + trust
    ) / 6

    st.success(f"{brand} の平均スコアは {avg:.1f} 点です")
