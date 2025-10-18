import streamlit as st

# -------------------------------
# 🎯 عنوان المشروع
# -------------------------------
st.title("🎁 نظام نقاط العملاء - Customer Points System")

# -------------------------------
# 🔢 تعريف المتغير العام للنقاط
# -------------------------------
if "total_points" not in st.session_state:
    st.session_state.total_points = 0

# -------------------------------
# 💬 إدخال بيانات العميل
# -------------------------------
st.subheader("أدخل بياناتك 👇")
customer_name = st.text_input("اسم العميل:")
new_points = st.number_input("عدد النقاط المكتسبة:", min_value=0, step=1)

# -------------------------------
# 🔘 زر لإضافة النقاط
# -------------------------------
if st.button("إضافة النقاط"):
    if customer_name.strip() == "":
        st.warning("من فضلك أدخل اسم العميل أولاً.")
    else:
        st.session_state.total_points += new_points
        st.success(f"أهلاً بك {customer_name}! 🎉 تمت إضافة {new_points} نقطة.")
        st.info(f"إجمالي النقاط في النظام الآن: {st.session_state.total_points}")

# -------------------------------
# 📊 عرض الإجمالي النهائي
# -------------------------------
st.divider()
st.write(f"**إجمالي النقاط النهائي:** {st.session_state.total_points} ⭐")
