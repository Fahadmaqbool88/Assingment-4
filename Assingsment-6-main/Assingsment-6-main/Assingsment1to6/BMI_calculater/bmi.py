import streamlit as st
st.title("BMI Calculater")
weight= st.number_input("inter your wait and kg")
hieght= st.number_input("inter your Hight in cm")
final_hight = hieght**2
if st.button("calculate BMI "):
    bmi= weight/final_hight
    st.success(f"your BMI is : {bmi:.2f}")
    if bmi<18.5:
        st.warning("you are underweight")
    elif 18.5<= bmi<24.9 :
        st.info("you have normal weight")
    elif 25<= bmi< 29.9 :
        st.warning("you are over weight")
    else :
        st.error("you are obese")

        

