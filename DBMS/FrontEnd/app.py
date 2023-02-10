import streamlit as st
import mysql.connector

from helper import *



st.title("Customer Loyalty Rewardal System")
menu = ["View Users","View Products","View Rewards","View Cart","View CartItems","Add User","Add Product","Add Reward","Add Cart","Add CartItem","Update User","Update Product","Update Reward","Update Cart"]
choice = st.sidebar.selectbox("Menu", menu)


if choice == "View Users":
    st.subheader("View User Details:")
    read('User')
elif choice == "View Products":
    st.subheader("View Product Details:")
    read('Product')
elif choice == "View Rewards":
    st.subheader("View Reward Details:")
    read('Reward')
elif choice == "View Cart":
    st.subheader("View Cart Details:")
    read('Cart')
elif choice == "View CartItems":
    st.subheader("View CartItems Details:")
    read('CartItem')


elif choice == "Add User":
    st.subheader("Add User Details")
    add_User()
elif choice == "Add Product":
    st.subheader("Add Product Details:")
    add_Product()
elif choice == "Add Reward":
    st.subheader("Add Reward Details:")
    add_Reward()
elif choice == "Add Cart":
    st.subheader("Add Cart Details:")
    add_Cart()
elif choice == "Add CartItem":
    st.subheader("Add CartItems Details:")
    add_CartItem()



elif choice == "Update User":
    st.subheader("Update User Details")
    update_User()
elif choice == "Update Product":
    st.subheader("Update Product Details:")
    update_Product()
elif choice == "Update Reward":
    st.subheader("Update Reward Details:")
    update_Reward()
elif choice == "Update Cart":
    st.subheader("Update Cart Details:")
    update_Cart()
