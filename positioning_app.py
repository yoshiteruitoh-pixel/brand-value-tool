import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="ブランドポジショニングマップツール",
    page_icon="📍",
    layout="wide",
)

st.title("ブランドポジショニングマップツール")

st.write(
    "ブランドは単独で存在するのではなく、競合や市場との関係の中で位置づけられます。"
    "ブランドの立ち位置を2軸で可視化してみましょう。"
)

initial_data = [
    {"ブランド名": "UNIQLO", "X": 3, "Y": 4, "種類": "事例ブランド"},
    {"ブランド名": "GU", "X": 5, "Y": 2, "種類": "事例ブランド"},
    {"ブランド名": "ZARA", "X": 8, "Y": 5, "種類": "事例ブランド"},
    {"ブランド名": "CHANEL", "X": 9, "Y": 10, "種類": "事例ブランド"},
    {"ブランド名": "sacai", "X": 9, "Y": 9, "種類": "事例ブランド"},
    {"ブランド名": "BEAMS", "X": 8, "Y": 7, "種類": "事例ブランド"},
    {"ブランド名": "THE NORTH FACE", "X": 5, "Y": 7, "種類": "事例ブランド"},
    {"ブランド名": "無印良品", "X": 4, "Y": 5, "種類": "事例ブランド"},
]

st.subheader("ブランドを追加する")

brand_name = st.text_input("ブランド名")

x_value = st.slider(
    "X軸：機能価値 ←→ 感性価値",
    min_value=1,
    max_value=10,
    value=5,
)

y_value = st.slider(
    "Y軸：低価格 ←→ 高価格",
    min_value=1,
    max_value=10,
    value=5,
)

data = initial_data.copy()

if brand_name:
    data.append(
        {
            "ブランド名": brand_name,
            "X": x_value,
            "Y": y_value,
            "種類": "学生入力ブランド",
        }
    )

df = pd.DataFrame(data)

fig = px.scatter(
    df,
    x="X",
    y="Y",
    text="ブランド名",
    color="種類",
    range_x=[0, 11],
    range_y=[0, 11],
    title="ブランドポジショニングマップ",
)

fig.update_traces(
    textposition="top center",
    marker=dict(size=14),
)

fig.add_vline(x=5.5, line_dash="dash")
fig.add_hline(y=5.5, line_dash="dash")

fig.update_xaxes(
    title="機能価値 ←→ 感性価値",
    tickvals=[1, 5.5, 10],
    ticktext=["機能価値", "中間", "感性価値"],
)

fig.update_yaxes(
    title="低価格 ←→ 高価格",
    tickvals=[1, 5.5, 10],
    ticktext=["低価格", "中間", "高価格"],
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("4象限の見方")

st.write("左下：機能・低価格型")
st.write("右下：感性・低価格型")
st.write("左上：機能・高価格型")
st.write("右上：感性・高価格型")

if brand_name:
    if x_value <= 5.5 and y_value <= 5.5:
        quadrant = "機能・低価格型"
    elif x_value > 5.5 and y_value <= 5.5:
        quadrant = "感性・低価格型"
    elif x_value <= 5.5 and y_value > 5.5:
        quadrant = "機能・高価格型"
    else:
        quadrant = "感性・高価格型"

    st.subheader("診断結果")
    st.success(f"{brand_name} は「{quadrant}」に位置づけられます。")

    st.write(
        f"{brand_name} は、X軸では {x_value}、Y軸では {y_value} に位置します。"
        "この位置から、競合ブランドとの違いや市場での立ち位置を考えてみましょう。"
    )
