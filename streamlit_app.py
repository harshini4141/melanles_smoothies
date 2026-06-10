import streamlit as st
import requests
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Page Title
st.title("🥤 Custom Smoothie Order Form")
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")

# Snowflake Session
session = get_active_session()

# Customer Name
name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your Smoothie will be:", name_on_order)

# Get Fruit List from Snowflake
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))

fruit_list = [row["FRUIT_NAME"] for row in my_dataframe.collect()]

# Multi-select Widget
ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    fruit_list
)

# Display Selected Ingredients
if ingredients_list:
    ingredients_string = ""

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + " "

    st.write("Ingredients Selected:")
    st.write(ingredients_string)

# Submit Button
time_to_insert = st.button("Submit Order")

# Insert Order into Snowflake
if time_to_insert:

    ingredients_string = ""

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + " "

    my_insert_stmt = f"""
    INSERT INTO smoothies.public.orders
    (ingredients, name_on_order)
    VALUES
    ('{ingredients_string}', '{name_on_order}')
    """

    session.sql(my_insert_stmt).collect()

    st.success("Your Smoothie is ordered! ✅")

# Show Pending Orders
st.subheader("🥤 Pending Smoothie Orders")

pending_orders = (
    session.table("smoothies.public.orders")
    .filter(col("ORDER_FILLED") == False)
    .collect()
)

st.dataframe(pending_orders, use_container_width=True)
