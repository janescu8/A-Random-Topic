import streamlit as st
import os
import random
from PIL import Image

SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')

def get_image_files(folder_path):
    return [file for file in os.listdir(folder_path) if file.lower().endswith(SUPPORTED_FORMATS)]

def main():
    st.title("🎲 隨機圖片展示器")
    img_folder = "img"

    if not os.path.exists(img_folder):
        st.error(f"找不到資料夾: {img_folder}")
        return

    image_files = get_image_files(img_folder)

    if not image_files:
        st.warning("資料夾裡沒有支援的圖片格式。")
        return

    # 初始化 session_state
    if "selected_image" not in st.session_state or st.button("🔁 抽另一張圖片"):
        st.session_state.selected_image = random.choice(image_files)

    image_path = os.path.join(img_folder, st.session_state.selected_image)

    try:
        st.subheader(f"你抽到的圖片是：`{st.session_state.selected_image}`")
        st.image(Image.open(image_path), use_container_width=True)
    except Exception as e:
        st.error(f"圖片無法載入：{e}")

if __name__ == "__main__":
    main()
