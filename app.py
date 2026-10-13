import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tao du lieu 10 sinh vien
data = {
    "Họ tên": [
        "Nguyễn Văn An", "Trần Thị Bình", "Lê Hoàng Nam",
        "Phạm Minh Anh", "Hoàng Đức Huy", "Võ Thị Lan",
        "Đặng Quốc Bảo", "Bùi Ngọc Mai", "Đỗ Thành Long",
        "Phan Thu Hà"
    ],
    "Chuyên cần": [9, 8, 10, 7, 8, 9, 6, 10, 7, 8],
    "Giữa kỳ": [8, 7, 9, 6, 8, 9, 7, 8, 6, 9],
    "Cuối kỳ": [9, 8, 9, 7, 7, 10, 8, 9, 7, 8]
}

df = pd.DataFrame(data)

# 2. Tinh diem tong ket
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
)

# 3. Xep loai
df["Xếp loại"] = "Yếu"
df.loc[df["Tổng kết"] >= 5, "Xếp loại"] = "Trung bình"
df.loc[df["Tổng kết"] >= 7, "Xếp loại"] = "Khá"
df.loc[df["Tổng kết"] >= 8.5, "Xếp loại"] = "Giỏi"

# 4. Tieu de va bang diem
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Bảng điểm của 10 sinh viên")
st.dataframe(df, hide_index=True)

# 5. Diem trung binh
print("Điểm trung bình:", df["Tổng kết"].mean())
st.write("Điểm trung bình của lớp là:", round(df["Tổng kết"].mean(), 2))

# 6. Sinh vien diem cao nhat
diem_cao = df["Tổng kết"].max()
st.write("Sinh viên có điểm cao nhất:")
st.write(df[df["Tổng kết"] == diem_cao]["Họ tên"])

# 7. Sinh vien diem thap nhat
diem_thap = df["Tổng kết"].min()
st.write("Sinh viên có điểm thấp nhất:")
st.write(df[df["Tổng kết"] == diem_thap]["Họ tên"])

# 8. Dem sinh vien dat
so_sinh_vien = (df["Tổng kết"] >= 5).sum()
st.write("Số sinh viên đạt là:", so_sinh_vien)

# 9. Chon sinh vien
st.write("Tra cứu điểm sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Họ tên"])

# Tim thong tin sinh vien duoc chon
sv = df[df["Họ tên"] == ten]

st.write("Điểm chuyên cần:", sv["Chuyên cần"].values[0])
st.write("Điểm giữa kỳ:", sv["Giữa kỳ"].values[0])
st.write("Điểm cuối kỳ:", sv["Cuối kỳ"].values[0])
st.write("Điểm tổng kết:", round(sv["Tổng kết"].values[0], 2))
st.write("Xếp loại:", sv["Xếp loại"].values[0])

# 10. Ve bieu do cot
plt.bar(df["Họ tên"], df["Tổng kết"])
plt.title("Điểm tổng kết của 10 sinh viên")
plt.xlabel("Họ tên sinh viên")
plt.ylabel("Điểm tổng kết")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(plt.gcf())
plt.close()

# 11. Thong tin nguoi tao
st.write("---")
st.caption("Người tạo: Trần Thị Minh Phương | MSSV: 033308000314")
