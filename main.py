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

    selected_image = random.choice(image_files)
    image_path = os.path.join(img_folder, selected_image)

    st.subheader(f"你抽到的圖片是：`{selected_image}`")
    st.image(Image.open(image_path), use_container_width=True)

    if st.button("🔁 抽另一張圖片"):
        st.experimental_rerun()
