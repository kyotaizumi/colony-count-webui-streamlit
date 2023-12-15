import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Streamlitのタイトル
st.title('Colony Counter')

# 画像のアップロード
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# 閾値のスライダー
threshold_value = st.slider('Threshold value', min_value=0, max_value=255, value=128)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image.convert('L'))  # グレースケールに変換

    # 二値化処理
    _, binary = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY_INV)

    # コロニーを検出
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # コロニーの数をカウント（面積が100以上のもののみ）
    colony_count = sum(1 for contour in contours if cv2.contourArea(contour) >= 10)
    st.write(f"コロニーの数: {colony_count}")

    # 結果を表示する
    col1, col2 = st.columns(2)
    col1.image(image, caption='Uploaded Image', use_column_width=True)
    col2.image(binary, caption='Colonies', use_column_width=True)