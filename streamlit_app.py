import streamlit as st
import pandas as pd
from urllib.parse import urlparse, parse_qs

# Sample Data (replace this with real data source)
orders_data = pd.DataFrame([
    {"orderID": "0201001001274", "order_type": "Delivery", "order_date": "8/19/16", "origin": "201 Weiss Furs",
     "reference": "", "subtotal": 149.49, "freight": 13.90, "tax": 11.96, "total": 175.35, "status": "Open",
     "customer_name": "Sandy Gu", "customer_phone": "543-545-4354 x.35354", "address": "12345 Scofield Farms, Solon, OH 44139", 
     "items": [{"id": "1006", "description": "ROLL SLEEVE SWEATER DRESS", "unit_price": 79.99, "quantity": 1, "net_amount": 79.99, "status": "Unfulfillable"},
               {"id": "1004", "description": "BLK WHITE CAP SLEEVE DRESS", "unit_price": 69.50, "quantity": 1, "net_amount": 69.50, "status": "Polled"}]
    }
])

# Get URL parameter ?orderID=xxxx
query_params = st.experimental_get_query_params()

if 'orderID' in query_params:
    order_id = query_params['orderID'][0]
    filtered_order = orders_data[orders_data['orderID'] == order_id]
else:
    st.write("No orderID provided in the URL.")
    st.stop()

if filtered_order.empty:
    st.write(f"No order found for Order ID: {order_id}")
    st.stop()

# Extract the first (and only) order row
order_info = filtered_order.iloc[0]

# Display Order Details
st.title("Unfulfillable Order Status")
st.write(f"**Order ID:** {order_info['orderID']}")
st.write(f"**Order Type:** {order_info['order_type']}")
st.write(f"**Order Date:** {order_info['order_date']}")
st.write(f"**Order Origin:** {order_info['origin']}")
st.write(f"**Order Status:** {order_info['status']}")
st.write(f"**Reference #:** {order_info['reference']}")
st.write(f"**Subtotal:** ${order_info['subtotal']:.2f}")
st.write(f"**Freight:** ${order_info['freight']:.2f}")
st.write(f"**Tax:** ${order_info['tax']:.2f}")
st.write(f"**Total:** ${order_info['total']:.2f}")
st.write("---")

# Display Customer Info
st.subheader("Customer")
st.write(f"**Name:** {order_info['customer_name']}")
st.write(f"**Phone:** {order_info['customer_phone']}")
st.write(f"**Address:** {order_info['address']}")

# Display Items Table
st.subheader("Order Items")
order_items = pd.DataFrame(order_info['items'])
st.table(order_items[['description', 'unit_price', 'quantity', 'net_amount', 'status']])

# Run the app with the following command in terminal
# streamlit run app.py
