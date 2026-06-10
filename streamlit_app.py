import streamlit as st
from snowflake.snowpark.functions import col

# Page Title
st.title("🥤 Custom Smoothie Order Form")
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
# Customer Name
name_on_order = st.text_input("Name on Smoothie:")

st.write("The name on your Smoothie will be:", name_on_order)

# Snowflake Session
session = get_active_session()
import requests  
smoothiefroot_response = requests.get("[https://my.smoothiefroot.com/api/fruit/watermelon](https://my.smoothiefroot.com/api/fruit/watermelon)")  
st.text(smoothiefroot_response)


# Get Fruit List
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))
editable_df = st.data_editor(my_dataframe)

submitted = st.button('Submit')

if submitted:
    st.success("Someone clicked the button.", icon="👍")



# Display Fruits
# st.dataframe(data=my_dataframe, use_container_width=True)

# # Multi-select Widget
# ingredients_list = st.multiselect(
#     "Choose up to 5 ingredients:",
#     my_dataframe.collect()
# )

# # Submit Button
# time_to_insert = st.button("Submit Order")

# # Process Order
# if time_to_insert:

#     ingredients_string = ""

#     for fruit_chosen in ingredients_list:
#         ingredients_string += str(fruit_chosen[0]) + " "

#     st.write("Ingredients Selected:")
#     st.write(ingredients_string)

#     my_insert_stmt = f"""
#     INSERT INTO smoothies.public.orders
#     (ingredients, name_on_order)
#     VALUES
#     ('{ingredients_string}', '{name_on_order}')
#     """

#     session.sql(my_insert_stmt).collect()

#     st.success("Your Smoothie is ordered! ✅")

# # Show Pending Orders
# st.subheader("🥤 Pending Smoothie Orders")

# pending_orders = (
#     session.table("smoothies.public.orders")
#     .filter(col("ORDER_FILLED") == False)
#     .collect()
# )

# st.dataframe(pending_orders, use_container_width=True)
