# app.py (root folder)
import streamlit as st
import requests
from PIL import Image
import io

def format_price(val):
    try:
        return f"{int(val):,}"
    except (ValueError, TypeError):
        return "?"

def estimate_price(label, confidence):
    category = label_to_category.get(label, None)
    if category and category in category_price_ranges:
        min_price, max_price = category_price_ranges[category]
        price = int(min_price + (max_price - min_price) * float(confidence))
        # Luxury boost for high-confidence luxury items
        if category in ["car", "handbag", "watch", "laptop", "tv", "camera"] and confidence > 0.9:
            price = int(price * 1.2)
        return price
    else:
        # Fallback: use a generic range or a function of confidence
        fallback_min, fallback_max = 500, 5000
        return int(fallback_min + (fallback_max - fallback_min) * float(confidence))

# Page configuration
st.set_page_config(page_title="Price Estimator AI", layout="wide", initial_sidebar_state="expanded")

# Save history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar menu
with st.sidebar:
    st.header("Menu")
    page = st.radio("Choose a page:", ["Estimate", "History"])
    st.divider()
    api_url = st.text_input("API URL", value="http://localhost:8000", help="Backend API URL")

st.title("🖼️ Price Estimator AI")

if page == "Estimate":
    st.header("Upload Image(s) for Estimation")
    uploaded_files = st.file_uploader("Choose one or more image files", type=["jpg", "jpeg", "png", "webp"], accept_multiple_files=True)
    condition = st.selectbox(
        "Select item condition:",
        ["New", "Used", "Heavily Used"],
        help="Condition affects price: New (0%), Used (-25%), Heavily Used (-50%)"
    )
    if uploaded_files and st.button("Estimate Price & Description"):
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            with st.spinner(f"Analyzing {uploaded_file.name}..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    data = {"condition": condition}
                    response = requests.post(f"{api_url}/predict/", files=files, data=data, timeout=30)
                    if response.status_code == 200:
                        result = response.json()
                        breakdown = result.get("breakdown", {})
                        st.success("Analysis completed successfully!")
                        st.markdown(f"""
                        **Name:** {result['name']}  
                        **Description:** {result['description']}  
                        **Model Confidence:** {breakdown.get('confidence', '?')}%  
                        **Base Price:** ₹{format_price(breakdown.get('base_price'))}  
                        **Condition ({breakdown.get('condition', '?')}):** {breakdown.get('condition_adjustment', '?')}  
                        **Price after Condition:** ₹{format_price(breakdown.get('price_after_condition'))}  
                        **Confidence Adjustment:** {breakdown.get('confidence_adjustment', '?')}  
                        **Final Price:** <span style='font-size:1.2em;'>₹{format_price(breakdown.get('final_price'))}</span>
                        """, unsafe_allow_html=True)
                        st.session_state.history.append({
                            "image_bytes": uploaded_file.getvalue(),
                            "image_type": uploaded_file.type,
                            "name": result['name'],
                            "description": result['description'],
                            "breakdown": breakdown
                        })
                    else:
                        st.error(f"API Error: {response.status_code}")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

elif page == "History":
    st.header("Uploaded Images & Results History")
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history), 1):
            cols = st.columns([1, 2])
            with cols[0]:
                st.image(
                    Image.open(io.BytesIO(entry["image_bytes"])),
                    caption=f"Image #{len(st.session_state.history) - i + 1}",
                    use_column_width=True,
                    output_format=entry["image_type"].split("/")[-1]
                )
            with cols[1]:
                breakdown = entry.get("breakdown", {})
                st.markdown(f"""
                **Name:** {entry['name']}  
                **Description:** {entry['description']}  
                **Model Confidence:** {breakdown.get('confidence', '?')}%  
                **Base Price:** ₹{format_price(breakdown.get('base_price'))}  
                **Condition ({breakdown.get('condition', '?')}):** {breakdown.get('condition_adjustment', '?')}  
                **Price after Condition:** ₹{format_price(breakdown.get('price_after_condition'))}  
                **Confidence Adjustment:** {breakdown.get('confidence_adjustment', '?')}  
                **Final Price:** <span style='font-size:1.2em;'>₹{format_price(breakdown.get('final_price'))}</span>
                """, unsafe_allow_html=True)
            st.divider()
    else:
        st.info("No images have been analyzed yet. Upload an image on the Estimate page.")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>🖼️ Price Estimator AI | Built with Streamlit & FastAPI</p>",
    unsafe_allow_html=True
)

category_price_ranges = {
    "car": (5000, 2000000),
    "phone": (3000, 150000),
    "handbag": (500, 50000),
    "laptop": (10000, 300000),
    "furniture": (1000, 100000),
    "watch": (1000, 1000000),
    "tv": (5000, 500000),
    "camera": (2000, 500000),
    # ... add more as needed
}

label_to_category = {
    "sports_car": "car",
    "convertible": "car",
    "cellular_telephone": "phone",
    "laptop": "laptop",
    "handbag": "handbag",
    "sofa": "furniture",
    "armchair": "furniture",
    "digital_watch": "watch",
    "tv": "tv",
    "camera": "camera",
    # ... add more as needed
}

def predict_image(img, return_confidence=False):
    # ... (preprocessing and prediction)
    label = decoded[1].lower().replace(" ", "_")
    confidence = float(decoded[2])
    price = estimate_price(label, confidence)
    # ... (rest of your logic)