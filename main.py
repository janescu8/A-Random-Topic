import streamlit as st
import os
import random
from PIL import Image

# 支援的圖片格式
SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')

# 取得 img 資料夾內所有圖片檔案
def get_image_files(folder_path):
    return [file for file in os.listdir(folder_path) if file.lower().endswith(SUPPORTED_FORMATS)]

# 主程式
def main():
    st.title("🎲 隨機挑選主題")
    img_folder = "img"

    # 檢查資料夾是否存在
    if not os.path.exists(img_folder):
        st.error(f"找不到資料夾: {img_folder}")
        return

    image_files = get_image_files(img_folder)

    if not image_files:
        st.warning("資料夾裡沒有支援的圖片格式。")
        return

    # 隨機選取一張圖片
    selected_image = random.choice(image_files)
    image_path = os.path.join(img_folder, selected_image)

    st.subheader(f"你抽到的主題是：`{selected_image}`")
    st.image(Image.open(image_path), use_column_width=True)

    # 加一個按鈕重新抽
    if st.button("🔁 抽另一個主題"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
