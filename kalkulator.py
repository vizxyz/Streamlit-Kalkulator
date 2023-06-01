import streamlit as st

def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

def main():
    st.title("Kalkulator Sederhana")

    num1 = st.number_input("Masukkan angka pertama", 0)
    num2 = st.number_input("Masukkan angka kedua", 0)

    operations = ['+', '-', '*', '/']
    operation = st.selectbox("Pilih operasi matematika", operations)

    calculate_button = st.button("Hitung")

    if calculate_button:
        result = calculator(num1, num2, operation)
        st.write("Hasil :", result)

if __name__ == "__main__":
    main()
