import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="ブランドポジショニングマップツール",
    page_icon="📍",
    layout="wide",
)


INITIAL_BRANDS = [
    {"ブランド名": "UNIQLO", "X": 3, "Y": 4, "種類": "事例ブランド"},
    {"ブランド名": "GU", "X": 5, "Y": 2, "種類": "事例ブランド"},
    {"ブランド名": "ZARA", "X": 8, "Y": 5, "種類": "事例ブランド"},
    {"ブランド名": "CHANEL", "X": 9, "Y": 10, "種類": "事例ブランド"},
    {"ブランド名": "sacai", "X": 9, "Y": 9, "種類": "事例ブランド"},
    {"ブランド名": "BEAMS", "X": 8, "Y": 7, "種類": "事例ブランド"},
    {"ブランド名": "THE NORTH FACE", "X": 5, "Y": 7, "種類": "事例ブランド"},
    {"ブランド名": "無印良品", "X": 4, "Y": 5, "種類": "事例ブランド"},
]


QUADRANT_DESCRIPTIONS = {
    "左下": "機能・低価格型",
    "右下": "感性・低価格型",
    "左上": "機能・高価格型",
    "右上": "感性・高価格型",
}


def judge_quadrant(x_value: int, y_value: int) -> tuple[str, str]:
    if x_value <= 5 and y_value <= 5:
        quadrant = "左下"
    elif x_value >= 6 and y_value <= 5:
        quadrant = "右下"
    elif x_value <= 5 and y_value >= 6:
        quadrant = "左上"
    else:
        quadrant = "右上"

    return quadrant, QUADRANT_DESCRIPTIONS[quadrant]


def build_chart(df: pd.DataFrame):
    fig = px.scatter(
        df,
        x="X",
        y="Y",
        text="ブランド名",
        color="種類",
        color_discrete_map={
            "事例ブランド": "#2F6B8F",
            "追加ブランド": "#D45A3C",
        },
        hover_data={
            "ブランド名": True,
            "X": True,
            "Y": True,
            "種類": True,
        },
    )

    fig.update_traces(
        marker=dict(size=18, line=dict(width=1.5, color="white")),
        textposition="top center",
        textfont=dict(size=13),
    )

    fig.add_vline(
        x=5.5,
        line_width=2,
        line_dash="dash",
        line_color="#777777",
    )
    fig.add_hline(
        y=5.5,
        line_width=2,
        line_dash="dash",
        line_color="#777777",
    )

    fig.add_annotation(x=3, y=3, text="機能・低価格型", showarrow=False, opacity=0.45)
    fig.add_annotation(x=8, y=3, text="感性・低価格型", showarrow=False, opacity=0.45)
    fig.add_annotation(x=3, y=8, text="機能・高価格型", showarrow=False, opacity=0.45)
    fig.add_annotation(x=8, y=8, text="感性・高価格型", showarrow=False, opacity=0.45)

    fig.update_layout(
        height=650,
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(l=30, r=30, t=30, b=30),
        legend_title_text="",
        xaxis_title="機能価値 ←→ 感性価値",
        yaxis_title="低価格 ←→ 高価格",
    )

    fig.update_xaxes(
        range=[0.5, 10.5],
