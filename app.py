import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="ブランド価値診断ツール", layout="centered")

st.title("ブランド価値診断ツール")
st.write("ブランド価値創造論 授業用")
st.write(
    "ブランドは単一の要素ではなく、複数の価値の組み合わせによって成り立っています。"
    "好きなブランドを1つ選び、7つの軸で評価してみましょう。"
)

brand = st.text_input("ブランド名")

scores = {
    "機能性": st.slider("機能性", 1, 10, 5),
    "デザイン性": st.slider("デザイン性", 1, 10, 5),
    "世界観": st.slider("世界観", 1, 10, 5),
    "独自性": st.slider("独自性", 1, 10, 5),
    "体験価値": st.slider("体験価値", 1, 10, 5),
    "信頼性": st.slider("信頼性", 1, 10, 5),
    "価格価値": st.slider("価格価値", 1, 10, 5),
}

type_labels = {
    "機能性": "機能型ブランド",
    "デザイン性": "デザイン型ブランド",
    "世界観": "世界観型ブランド",
    "独自性": "創造型ブランド",
    "体験価値": "体験型ブランド",
    "信頼性": "信頼型ブランド",
    "価格価値": "価格価値型ブランド",
}

if st.button("診断する"):
    if not brand:
        st.warning("ブランド名を入力してください。")
    else:
        categories = list(scores.keys())
        values = list(scores.values())

        # レーダーチャートを閉じるために最初の値を最後に追加
        categories_closed = categories + [categories[0]]
        values_closed = values + [values[0]]

        fig = go.Figure()

        fig.add_trace(
            go.Scatterpolar(
                r=values_closed,
                theta=categories_closed,
                fill="toself",
                name=brand,
            )
        )

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )
            ),
            showlegend=False,
            title=f"{brand} のブランド価値チャート",
        )

        st.plotly_chart(fig, use_container_width=True)

        avg = sum(values) / len(values)
        max_item = max(scores, key=scores.get)
        min_item = min(scores, key=scores.get)
        brand_type = type_labels[max_item]

        st.subheader("診断結果")
        st.write(f"平均スコア：{avg:.1f} 点")
        st.write(f"最も高い評価項目：{max_item}（{scores[max_item]}点）")
        st.write(f"最も低い評価項目：{min_item}（{scores[min_item]}点）")
        st.success(f"ブランドタイプ：{brand_type}")

        st.subheader("考察")
        st.write(
            f"{brand} は、{max_item} の評価が特に高く、"
            f"{brand_type} としての特徴が見られます。"
            f"一方で、{min_item} の評価が低いため、"
            f"今後のブランド価値向上にはこの点をどう補うかが課題になります。"
        )
