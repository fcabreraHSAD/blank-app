import streamlit as st
import pandas as pd

# Continue with the rest of the application (e.g., search functionality)
order_id = st.text_input("Search for Order ID:", value="000000285")

# Example data for orders (replace with actual data source)
orders_data = pd.DataFrame([
    {"orderID": "000000285", "order_type": "Delivery", "order_date": "Jun 11, 2021, 8:17:48 AM", "status": "Pending",
     "origin": "Main Website", "account_name": "Sandy Gu", "email": "sandy.gu@example.com", "group": "General",
     "billing_address": "123 Main Street, Some City, ST 12345", "shipping_address": "456 Other Street, Another City, ST 54321",
     "payment_method": "Credit Card (Braintree)", "shipping_method": "Flat Rate - Fixed $50.00",
     "subtotal": 40.00, "shipping": 50.00, "tax": 8.00, "total": 98.00,
     "items": [{"id": "1006", "description": "swatch-S500-purple", "item_status": "Ordered", "price": 2.00, "qty": 20, "subtotal": 40.00, "tax": 8.00, "tax_percent": 20, "discount": 0.00, "row_total": 48.00}]
    }
])

# Filter based on order_id
filtered_order = orders_data[orders_data['orderID'] == order_id]

if filtered_order.empty:
    st.write(f"No order found for Order ID: {order_id}")
    st.stop()

# Extract order information
order_info = filtered_order.iloc[0]

# LG brand colors
LG_RED = "#CE0031"
LG_GREEN = "#008A00"
LG_GRAY = "#f2f2f2"

# Styling
st.markdown(f"""
    <style>
    .section-header {{
        font-size: 18px;
        font-weight: bold;
        color: {LG_RED};
        margin-bottom: 10px;
    }}
    .info-box {{
        background-color: {LG_GRAY};
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }}
    .info-box div {{
        margin-bottom: 5px;
    }}
    .right-align {{
        text-align: right;
    }}
    .order-items-table th, .order-items-table td {{
        padding: 10px;
        border: 1px solid #ddd;
    }}
    .order-items-table th {{
        background-color: {LG_GRAY};
        font-weight: bold;
    }}
    .totals-box {{
        margin-top: 20px;
        border-top: 1px solid #ddd;
        padding-top: 10px;
        text-align: right;
    }}
    .totals-box strong {{
        color: {LG_RED};
    }}
    .status-dropdown {{
        margin-top: 20px;
    }}
    .green-text {{
        color: {LG_GREEN};
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

# Order & Account Information
st.markdown("<div class='section-header'>Order & Account Information</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class="info-box">
    <div><strong>Order #:</strong> {order_info['orderID']} (The order confirmation email is not sent)</div>
    <div><strong>Order Date:</strong> {order_info['order_date']}</div>
    <div><strong>Order Status:</strong> {order_info['status']}</div>
    <div><strong>Purchased From:</strong> {order_info['origin']}</div>
</div>
<div class="info-box">
    <div><strong>Customer Name:</strong> {order_info['account_name']}</div>
    <div><strong>Email:</strong> {order_info['email']}</div>
    <div><strong>Customer Group:</strong> {order_info['group']}</div>
</div>
""", unsafe_allow_html=True)

# Address Information
st.markdown("<div class='section-header'>Address Information</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class="info-box">
    <div><strong>Billing Address:</strong> {order_info['billing_address']}</div>
</div>
<div class="info-box">
    <div><strong>Shipping Address:</strong> {order_info['shipping_address']}</div>
</div>
""", unsafe_allow_html=True)

# Payment & Shipping Method
st.markdown("<div class='section-header'>Payment & Shipping Method</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class="info-box">
    <div><strong>Payment Information:</strong> {order_info['payment_method']}</div>
</div>
<div class="info-box">
    <div><strong>Shipping & Handling Information:</strong> {order_info['shipping_method']}</div>
</div>
""", unsafe_allow_html=True)

# Items Ordered
st.markdown("<div class='section-header'>Items Ordered</div>", unsafe_allow_html=True)
st.markdown("""
<table class="order-items-table" width="100%">
    <thead>
        <tr>
            <th>Product</th>
            <th>Item Status</th>
            <th>Original Price</th>
            <th>Price</th>
            <th>Qty</th>
            <th>Subtotal</th>
            <th>Tax Amount</th>
            <th>Tax Percent</th>
            <th>Discount Amount</th>
            <th>Row Total</th>
        </tr>
    </thead>
    <tbody>
""", unsafe_allow_html=True)

for item in order_info['items']:
    st.markdown(f"""
        <tr>
            <td>{item['description']}</td>
            <td>{item['item_status']}</td>
            <td>${item['price']:.2f}</td>
            <td>${item['price']:.2f}</td>
            <td>{item['qty']}</td>
            <td>${item['subtotal']:.2f}</td>
            <td>${item['tax']:.2f}</td>
            <td>{item['tax_percent']}%</td>
            <td>${item['discount']:.2f}</td>
            <td>${item['row_total']:.2f}</td>
        </tr>
    """, unsafe_allow_html=True)

st.markdown("</tbody></table>", unsafe_allow_html=True)

# Order Totals
st.markdown("<div class='section-header'>Order Totals</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class="totals-box">
    <div><strong>Subtotal:</strong> ${order_info['subtotal']:.2f}</div>
    <div><strong>Shipping & Handling:</strong> ${order_info['shipping']:.2f}</div>
    <div><strong>Tax:</strong> ${order_info['tax']:.2f}</div>
    <div><strong>Grand Total:</strong> ${order_info['total']:.2f}</div>
</div>
""", unsafe_allow_html=True)

# Status Dropdown
st.markdown("<div class='section-header'>Notes for this Order</div>", unsafe_allow_html=True)
st.selectbox('Status', ['Pending', 'Closed'])

