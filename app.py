
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LuxeCart | Online Shopping",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: #f7f8fc;
}
.block-container {
    padding-top: 1.5rem;
    max-width: 1400px;
}
.hero {
    background: linear-gradient(120deg, #111827, #4338ca);
    color: white;
    padding: 42px 32px;
    border-radius: 22px;
    margin-bottom: 25px;
}
.hero h1 {
    color: white;
    font-size: 42px;
}
.hero p {
    color: #e0e7ff;
    font-size: 17px;
}
div.stButton > button {
    border-radius: 10px;
    font-weight: 600;
}
.product-card {
    background: white;
    padding: 14px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
}
.price {
    font-size: 23px;
    font-weight: bold;
    color: #4338ca;
}
.small-text {
    color: #64748b;
}
</style>
""", unsafe_allow_html=True)

# ---------- PRODUCT DATA ----------
products = [
    {
        "id": 1, "name": "Wireless Headphones",
        "category": "Electronics", "price": 1499,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700"
    },
    {
        "id": 2, "name": "Smart Watch",
        "category": "Electronics", "price": 2299,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=700"
    },
    {
        "id": 3, "name": "Casual Sneakers",
        "category": "Shoes", "price": 1799,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=700"
    },
    {
        "id": 4, "name": "Classic Backpack",
        "category": "Accessories", "price": 999,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=700"
    },
    {
        "id": 5, "name": "Running Shoes",
        "category": "Shoes", "price": 1999,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=700"
    },
    {
        "id": 6, "name": "Premium Sunglasses",
        "category": "Accessories", "price": 799,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=700"
    },
    {
        "id": 7, "name": "Modern Camera",
        "category": "Electronics", "price": 4999,
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=700"
    },
    {
        "id": 8, "name": "Travel Watch",
        "category": "Accessories", "price": 1299,
        "rating": 4.2,
        "image": "https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=700"
    },
    {
        "id": 9, "name": "Designer T-Shirt",
        "category": "Clothing", "price": 599,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=700"
    },
    {
        "id": 10, "name": "Leather Handbag",
        "category": "Accessories", "price": 1899,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=700"
    },
    {
        "id": 11, "name": "Portable Speaker",
        "category": "Electronics", "price": 1199,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=700"
    },
    {
        "id": 12, "name": "Classic Sneakers",
        "category": "Shoes", "price": 1599,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1495555961986-6d4c1ecb7be3?w=700"
    },
]

# ---------- SESSION STATE ----------
if "cart" not in st.session_state:
    st.session_state.cart = {}

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# ---------- HEADER ----------
left, right = st.columns([3, 1])

with left:
    st.markdown("# 🛍️ LuxeCart")
    st.caption("Discover products. Shop smarter. Live better.")

with right:
    total_items = sum(st.session_state.cart.values())
    st.metric("🛒 Cart Items", total_items)

st.divider()

# ---------- SIDEBAR ----------
st.sidebar.title("🔎 Shop Filters")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "All Products", "My Cart", "Wishlist", "About Us"]
)

category_options = [
    "All", "Electronics", "Clothing", "Shoes", "Accessories"
]

selected_category = st.sidebar.selectbox(
    "Category", category_options
)

max_price = st.sidebar.slider(
    "Maximum price (₹)",
    min_value=500,
    max_value=5000,
    value=5000,
    step=100
)

sort_by = st.sidebar.selectbox(
    "Sort products",
    ["Featured", "Price: Low to High",
     "Price: High to Low", "Highest Rated"]
)

search = st.sidebar.text_input(
    "Search product", placeholder="Type a product name..."
)

# ---------- HELPERS ----------
def get_product(product_id):
    return next(p for p in products if p["id"] == product_id)

def add_to_cart(product_id):
    cart = st.session_state.cart
    cart[product_id] = cart.get(product_id, 0) + 1

def money(value):
    return f"₹{value:,.0f}"

# ---------- HERO ----------
if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Find Your Everyday Favourite.</h1>
        <p>Explore trending electronics, fashion, shoes and accessories.</p>
        <p>✨ Fresh styles • Great value • Easy shopping</p>
    </div>
    """, unsafe_allow_html=True)

    a, b, c = st.columns(3)
    a.info("🎧 Trending Electronics")
    b.info("👟 Everyday Fashion")
    c.info("🎒 Lifestyle Accessories")

# ---------- PRODUCT FILTERING ----------
filtered = products.copy()

if selected_category != "All":
    filtered = [
        p for p in filtered
        if p["category"] == selected_category
    ]

filtered = [
    p for p in filtered
    if p["price"] <= max_price
    and search.lower() in p["name"].lower()
]

if sort_by == "Price: Low to High":
    filtered.sort(key=lambda p: p["price"])
elif sort_by == "Price: High to Low":
    filtered.sort(key=lambda p: p["price"], reverse=True)
elif sort_by == "Highest Rated":
    filtered.sort(key=lambda p: p["rating"], reverse=True)

# ---------- ALL PRODUCTS ----------
if page in ["Home", "All Products"]:
    st.header("✨ Featured Products" if page == "Home"
              else "🛒 Explore All Products")
    st.caption(f"{len(filtered)} products available")

    if not filtered:
        st.warning("No products found. Change your filters.")
    else:
        columns_per_row = 4

        for start in range(0, len(filtered), columns_per_row):
            row_products = filtered[start:start + columns_per_row]
            cols = st.columns(columns_per_row)

            for col, product in zip(cols, row_products):
                with col:
                    with st.container(border=True):
                        st.image(
                            product["image"],
                            use_container_width=True
                        )
                        st.caption(product["category"])
                        st.subheader(product["name"])
                        st.write(f"⭐ {product['rating']} / 5")
                        st.markdown(
                            f"<div class='price'>{money(product['price'])}</div>",
                            unsafe_allow_html=True
                        )

                        qty = st.session_state.cart.get(product["id"], 0)
                        st.caption(f"In cart: {qty}")

                        if st.button(
                            "➕ Add to Cart",
                            key=f"add_{product['id']}",
                            use_container_width=True
                        ):
                            add_to_cart(product["id"])
                            st.rerun()

                        wishlisted = (
                            product["id"] in st.session_state.wishlist
                        )

                        if st.button(
                            "❤️ Saved" if wishlisted else "♡ Wishlist",
                            key=f"wish_{product['id']}",
                            use_container_width=True
                        ):
                            if wishlisted:
                                st.session_state.wishlist.remove(product["id"])
                            else:
                                st.session_state.wishlist.append(product["id"])
                            st.rerun()

# ---------- CART ----------
elif page == "My Cart":
    st.title("🛒 Your Shopping Cart")

    if not st.session_state.cart:
        st.info("Your cart is empty. Visit All Products to shop.")
    else:
        total = 0

        for product_id in list(st.session_state.cart):
            product = get_product(product_id)
            qty = st.session_state.cart[product_id]

            c1, c2, c3 = st.columns([2, 2, 1])

            with c1:
                st.image(product["image"], width=110)
            with c2:
                st.subheader(product["name"])
                st.write(money(product["price"]))
                st.write(f"Quantity: {qty}")
            with c3:
                st.write(" ")
                if st.button("➕", key=f"plus_{product_id}"):
                    st.session_state.cart[product_id] += 1
                    st.rerun()

                if st.button("➖", key=f"minus_{product_id}"):
                    st.session_state.cart[product_id] -= 1
                    if st.session_state.cart[product_id] <= 0:
                        del st.session_state.cart[product_id]
                    st.rerun()

                if st.button("🗑️ Remove", key=f"remove_{product_id}"):
                    del st.session_state.cart[product_id]
                    st.rerun()

            total += product["price"] * qty
            st.divider()

        st.subheader(f"Subtotal: {money(total)}")
        st.caption("Shipping and applicable taxes are not included.")

        if st.button("Proceed to Checkout", type="primary"):
            st.session_state.checkout_total = total
            st.info("Checkout demo: payment is not collected.")

        if st.button("Clear Entire Cart"):
            st.session_state.cart = {}
            st.rerun()

# ---------- WISHLIST ----------
elif page == "Wishlist":
    st.title("❤️ My Wishlist")

    if not st.session_state.wishlist:
        st.info("Your wishlist is empty.")
    else:
        for product_id in st.session_state.wishlist:
            product = get_product(product_id)
            c1, c2 = st.columns([1, 3])

            with c1:
                st.image(product["image"], width=140)
            with c2:
                st.subheader(product["name"])
                st.write(money(product["price"]))

                if st.button("Add to Cart", key=f"wishcart_{product_id}"):
                    add_to_cart(product_id)
                    st.success("Added to cart!")

# ---------- ABOUT ----------
elif page == "About Us":
    st.title("About LuxeCart")
    st.write("""
    LuxeCart is a sample online shopping project built with Python
    and Streamlit.

    Our demo includes:
    - Product catalog with images
    - Search and category filters
    - Price sorting
    - Shopping cart and quantity controls
    - Wishlist

    This version uses sample product data and a session-based cart.
    It does not yet include persistent database storage, customer
    accounts, stock validation or real payment processing.
    """)

st.divider()
st.caption("LuxeCart | Python + Streamlit | Educational E-commerce Demo")
