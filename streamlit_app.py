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

# Colors to match the LG cart page theme
WHITE = "rgb(255, 255, 255)"  # App background
LIGHT_GRAY = "#F2F2F2"
DARK_TEXT = "#1B1A1E"
ACCENT_COLOR = "#A50034"
BUTTON_COLOR = ACCENT_COLOR
BUTTON_TEXT_COLOR = WHITE

# Status color logic
STATUS_COLOR = ACCENT_COLOR if order_info['status'] in ['Pending', 'Processing', 'Shipped'] else "#148F29"  # Green for delivered, red otherwise

# Styling
st.markdown(f"""
    <style>
    body {{
        background-color: {WHITE};  /* Set background to white */
        color: {DARK_TEXT};
    }}
    .section-header {{
        font-size: 24px;
        font-weight: bold;
        color: {DARK_TEXT};
        margin-bottom: 10px;
    }}
    .status-header {{
        font-size: 30px;
        font-weight: bold;
        color: {STATUS_COLOR};
        margin-bottom: 10px;
    }}
    .info-box {{
        background-color: {LIGHT_GRAY};
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
        background-color: {LIGHT_GRAY};
        font-weight: bold;
    }}
    .totals-box {{
        margin-top: 20px;
        border-top: 1px solid #ddd;
        padding-top: 10px;
        text-align: right;
    }}
    .totals-box strong {{
        color: {ACCENT_COLOR};
    }}
    .button {{
        background-color: {BUTTON_COLOR};
        color: {BUTTON_TEXT_COLOR};
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
    }}
    .good-status {{
        color: #148F29;
        font-weight: bold;
    }}
    .processing-status {{
        color: {ACCENT_COLOR};
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

# Order Status
st.markdown(f"<div class='status-header'>Order Status: {order_info['status']}</div>", unsafe_allow_html=True)

# Order & Account Information
st.markdown("<div class='section-header'>Order & Account Information</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class="info-box">
    <div><strong>Order #:</strong> {order_info['orderID']} (The order confirmation email is not sent)</div>
    <div><strong>Order Date:</strong> {order_info['order_date']}</div>
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
st.markdown("""<table class="order-items-table" width="100%">
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
    <tbody>""", unsafe_allow_html=True)

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
        </tr>""", unsafe_allow_html=True)

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
