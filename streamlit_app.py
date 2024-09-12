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

# Material UI Colors and Styling
PRIMARY_COLOR = "#6200EE"
SECONDARY_COLOR = "#03DAC6"
BACKGROUND_COLOR = "#FFFFFF"  # App background to pure white
TEXT_COLOR = "#000000"  # Default black text
LIGHT_BACKGROUND = "#F5F5F5"
ACCENT_COLOR = "#BB86FC"
ERROR_COLOR = "#B00020"

# Status color logic
STATUS_COLOR = ERROR_COLOR if order_info['status'] in ['Pending', 'Processing', 'Shipped'] else SECONDARY_COLOR  # Green for delivered, red otherwise

# Apply Material Design-inspired styling
st.markdown(f"""
    <style>
    body {{
        background-color: {BACKGROUND_COLOR};  /* Set background to white */
        color: {TEXT_COLOR};
    }}
    .section-header {{
        font-size: 24px;
        font-weight: 600;
        color: {TEXT_COLOR};
        margin-bottom: 20px;
    }}
    .status-header {{
        font-size: 30px;
        font-weight: bold;
        color: {STATUS_COLOR};
        margin-bottom: 20px;
    }}
    .info-box {{
        background-color: {LIGHT_BACKGROUND};
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.12), 0px 1px 2px rgba(0, 0, 0, 0.24);
    }}
    .info-box div {{
        margin-bottom: 8px;
        color: {TEXT_COLOR};
    }}
    .right-align {{
        text-align: right;
    }}
    .order-items-table th, .order-items-table td {{
        padding: 12px;
        border: 1px solid #ddd;
    }}
    .order-items-table th {{
        background-color: {LIGHT_BACKGROUND};
        font-weight: bold;
    }}
    .totals-box {{
        margin-top: 20px;
        border-top: 1px solid #ddd;
        padding-top: 15px;
        text-align: right;
        color: {TEXT_COLOR};
    }}
    .totals-box strong {{
        color: {PRIMARY_COLOR};
    }}
    .button {{
        background-color: {PRIMARY_COLOR};
        color: {BACKGROUND_COLOR};
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        margin-top: 20px;
        display: inline-block;
    }}
    .good-status {{
        color: {SECONDARY_COLOR};
        font-weight: bold;
    }}
    .processing-status {{
        color: {ERROR_COLOR};
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
