import pandas as pd
import streamlit as st
import plotly.express as px
from database import *


#==============================================================================================
#                                   VIEW
#=============================================================================================


def read(tabl):
    result = view_all_data(tabl)
    # st.write(result)
    cl = []
    if tabl == 'User':cl = ['Name','Age','Number','Visits']
    elif tabl == 'Product':cl = ['Name','Price','Supplier']
    elif tabl == 'Reward':cl = ['Token','Discount','User_Name','Date_Allocated','Date_Claimed']
    elif tabl == 'Cart':cl = ['CartID','Total','User_Name','Reward_Allocated','Reward_Claimed']
    elif tabl == 'CartItem':cl = ['Quantity','SubTotal','ProductName','CartID']
    df = pd.DataFrame(result, columns=cl)
    with st.expander(str("Details from Table:"+tabl)):
        st.dataframe(df)


#==============================================================================================
#                                   ADD
#=============================================================================================


def add_User():
    col1, col2 = st.columns(2)
    with col1:
        new_userName = st.text_input("Name:")
        new_userNumber = st.text_input("Number:")
    with col2:
        new_Age = int(st.number_input("Age:"))
        new_Visits = int(st.number_input("Visits:"))

    if st.button("Add User"):
        add_user(new_userName,new_Age,new_userNumber,new_Visits)
        st.success("Successfully added User:{}".format(new_userName))

def add_Product():
    col1, col2 = st.columns(2)
    with col1:
        new_Name = st.text_input("Name:")
        new_supplier = st.text_input("Supplier:")
    with col2:
        new_Price = int(st.number_input("Price:"))

    if st.button("Add Product"):
        add_product(new_Name,new_Price,new_supplier)
        st.success("Successfully added Product: {}".format(new_Name))

def add_Reward():
    col1, col2 = st.columns(2)
    with col1:
        new_token = st.text_input("Token:")
        new_userName = st.text_input("User Name:")
        new_discount = int(st.number_input("Discount %:"))
    with col2:
        new_dat1 = st.date_input("Date Allocated:")
        new_dat2 = st.date_input("Date Claimed:")

    if st.button("Add User"):
        add_reward(new_token,new_discount,new_userName,new_dat1,new_dat2)
        st.success("Successfully added Reward: {}".format(new_token))

def add_Cart():
    col1, col2 = st.columns(2)
    with col1:
        new_cartID = st.text_input("Cart ID:")
        new_userName = st.text_input("User Name:")
        new_total = int(st.number_input("Total :"))
    with col2:
        new_re1 = st.text_input("Reward Allocated:")
        new_re2 = st.text_input("Reward Claimed:")
        if new_re2 == "None":new_re2 = None

    if st.button("Add User"):
        add_cart(new_cartID,new_total,new_userName,new_re1,new_re2)
        st.success("Successfully added Cart: {}".format(new_cartID))

def add_CartItem():
    col1, col2 = st.columns(2)
    with col1:
        new_productName = st.text_input("Product Name:")
        new_cartID = st.text_input("Cart ID:")
    with col2:
        new_quantity = int(st.number_input("Quantity:"))
        new_Subtotal = int(st.number_input("Subtotal:"))

    if st.button("Add User"):
        add_cartitem(new_quantity,new_Subtotal,new_productName,new_cartID)
        st.success("Successfully added CartItem for: {}".format(new_productName))  

#================================================================================================
#                               UPDATE
#================================================================================================


def update_User():
    result = view_all_data('User')
    df = pd.DataFrame(result, columns=['Name','Age','Number','Visits'])
    list_of_users = [i for i in df['Name']]
    selected_user = st.selectbox("User to Edit", list_of_users)
    df_new = df.loc[df['Name'] == selected_user]
    old_userName = df_new['Name'].to_string()
    #old_userAge = int(df_new['Age'])  # type: ignore
    #old_userNumber = df_new['Number']
    #old_Visits = int(df_new['Visits'])  # type: ignore
    print(type(old_userName))

    col1, col2 = st.columns(2)
    with col1:
        new_userName = st.text_input("Name:")
        new_userNumber = st.text_input("Number:")
    with col2:
        new_Age = int(st.number_input("Age:"))
        new_Visits = int(st.number_input("Visits:"))

    if st.button("Update User"):
        update_user(old_userName, new_userName,new_Age,new_userNumber,new_Visits)
        st.success("Successfully updated User:{}".format(new_userName))

def update_Product():
    result = view_all_data('Product')
    df = pd.DataFrame(result, columns=['Name','Price','Supplier'])
    list_of_products = [i for i in df['Name']]
    selected_products = st.selectbox("Product to Edit", list_of_products)
    [old_productName,old_Price,old_supplier] = df.loc[df['Name'] == selected_products]

    col1, col2 = st.columns(2)
    with col1:
        new_Name = st.text_input("Name:",old_productName)
        new_supplier = st.text_input("Supplier:",old_supplier)
    with col2:
        new_Price = int(st.number_input("Price:",int(old_Price)))

    if st.button("Update Product"):
        update_product(old_productName, new_Name,new_Price,new_supplier)
        st.success("Successfully updated Product: {}".format(old_productName))

def update_Reward():
    result = view_all_data('Reward')
    df = pd.DataFrame(result, columns=['Token','Discount','User_Name','Date_Allocated','Date_Claimed'])
    list_of_rewards = [i for i in df['Token']]
    selected_reward = st.selectbox("Reward to Edit", list_of_rewards)
    [old_token,old_discount,old_userName,old_date1,old_date2] = df.loc[df['Token'] == selected_reward]
    col1, col2 = st.columns(2)
    with col1:
        new_token = st.text_input("Token:",old_token)
        new_userName = st.text_input("User Name:",old_userName)
        new_discount = int(st.number_input("Discount %:",int(old_discount)))
    with col2:
        new_dat1 = st.date_input("Date Allocated:",old_date1)  # type: ignore
        new_dat2 = st.date_input("Date Claimed:",old_date2)  # type: ignore

    if st.button("Update Reward"):
        update_reward(old_token, new_token,new_discount,new_userName,new_dat1,new_dat2)
        st.success("Successfully updated Reward: {}".format(old_token))

def update_Cart():
    result = view_all_data('Cart')
    df = pd.DataFrame(result, columns=['CartID','Total','User_Name','Reward_Allocated','Reward_Claimed'])
    list_of_cart = [i for i in df['CartID']]
    selected_cart = st.selectbox("Cart to Edit", list_of_cart)
    [old_cartID,old_total,old_UserName,old_Re1,old_re2] = df.loc[df['CartID'] == selected_cart]
    
    col1, col2 = st.columns(2)
    with col1:
        new_cartID = st.text_input("Cart ID:",old_cartID)
        new_userName = st.text_input("User Name:",old_UserName)
        new_total = int(st.number_input("Total :",int(old_total)))
    with col2:
        new_re1 = st.text_input("Reward Allocated:",old_Re1)
        new_re2 = st.text_input("Reward Claimed:",old_re2)
        if new_re2 == "None":new_re2 = None

    if st.button("Update Cart"):
        update_cart(old_cartID, new_cartID,new_total,new_userName,new_re1,new_re2)
        st.success("Successfully updated Cart: {}".format(old_cartID))
