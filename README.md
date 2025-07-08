# 🖼️ Smart Auction AI System

A modern AI-powered auction system that analyzes uploaded images to provide item descriptions, names, and price estimates using machine learning.

## 🚀 Features

- **AI-Powered Image Analysis**: Uses TensorFlow with MobileNetV2 for accurate image classification
- **Automatic Price Estimation**: Intelligent price estimates based on item recognition
- **Real-time Bidding System**: Interactive bidding with real-time updates
- **Modern UI**: Beautiful Streamlit interface with responsive design
- **Auction History**: Track all bids and auction activities
- **Multi-format Support**: Supports JPG, PNG, WebP image formats

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: FastAPI (High-performance API framework)
- **AI Model**: TensorFlow with MobileNetV2 for image classification
- **Image Processing**: PIL (Python Imaging Library)
- **Styling**: Custom CSS for modern UI

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🔧 Installation

1. **Clone or download the project**
   
bash
   git clone <repository-url>
   cd auction-website


2. **Create a virtual environment (recommended)**
   
bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate


3. **Install dependencies**
   
bash
   pip install -r requirements.txt


## 🚀 Running the Application

### Option 1: Using Startup Scripts (Recommended)

1. **Start the Backend Server**
   
bash
   python start_backend.py

   The backend will be available at: http://localhost:8000

2. **Start the Frontend (in a new terminal)**
   
bash
   python start_frontend.py

   The frontend will be available at: http://localhost:8501

### Option 2: Manual Startup

1. **Start Backend**
   
bash
   python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000


2. **Start Frontend (in a new terminal)**
   
bash
   streamlit run app.py


## 📖 How to Use

1. **Upload Image**: Select an image file (JPG, PNG, WebP) from your device
2. **Analyze**: Click "Analyze Image" to get AI predictions
3. **Review Results**: View the item name, estimated price, and description
4. **Place Bid**: Enter your name and bid amount
5. **Track Bids**: Monitor current bids and auction history

## 🏗️ Project Structure

auction-website/
├── app.py                 # Main Streamlit frontend application
├── start_backend.py       # Backend startup script
├── start_frontend.py      # Frontend startup script
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── backend/
│   ├── main.py           # FastAPI backend server
│   ├── model/
│   │   └── predictor.py  # AI model for image prediction
│   └── utils/
│       └── image_preprocess.py  # Image preprocessing utilities
└── frontend/
    └── app.py            # Legacy frontend (not used)


## 🔍 API Endpoints

- GET / - Health check
- GET /health - Detailed health status
- POST /predict/ - Analyze uploaded image
- GET /supported-formats - List supported image formats

## 🎯 Supported Items

The AI model can recognize and price various categories of items:

- **Electronics**: Laptops, phones, cameras, TVs, etc.
- **Clothing & Accessories**: Shoes, bags, watches, etc.
- **Home & Kitchen**: Appliances, furniture, utensils, etc.
- **Sports & Recreation**: Bicycles, sports equipment, etc.
- **Books & Stationery**: Books, pens, notebooks, etc.
- **Toys & Games**: Board games, video games, etc.

## 🐛 Troubleshooting

### Common Issues

1. **Backend Connection Error**
   - Ensure the backend server is running on port 8000
   - Check if the API URL in the frontend settings is correct

2. **Model Loading Issues**
   - Ensure TensorFlow is properly installed
   - Check internet connection for model download

3. **Image Upload Issues**
   - Verify the image format is supported (JPG, PNG, WebP)
   - Check file size (max 10MB)

### Error Messages

- **"Cannot connect to backend server"**: Start the backend server first
- **"Model not loaded"**: Check TensorFlow installation
- **"Invalid image file"**: Try a different image format

## 🔧 Configuration

### Environment Variables

You can customize the application by setting environment variables:

- API_URL: Backend API URL (default: http://localhost:8000)
- PORT: Frontend port (default: 8501)
- BACKEND_PORT: Backend port (default: 8000)

### Customization

- **Add new items**: Edit price_map and desc_map in backend/model/predictor.py
- **Modify UI**: Edit CSS styles in app.py
- **Change model**: Replace MobileNetV2 with other TensorFlow models

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For technical support or questions:
- Create an issue in the repository
- Contact the development team

## 🔄 Updates

Stay updated with the latest features and improvements by regularly pulling from the repository.

---

**Happy Bidding! 🎉** 

## 2️⃣ **frontend/app.py** (Streamlit)

```python
import streamlit as st
import requests
from PIL import Image
import io

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
    st.header("Upload Image for Estimation")
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "webp"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("Estimate Price & Description"):
            with st.spinner("Analyzing image..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    response = requests.post(f"{api_url}/predict/", files=files, timeout=30)
                    if response.status_code == 200:
                        result = response.json()
                        st.success("Analysis completed successfully!")
                        st.markdown(f"""
                        **Name:** {result['name']}  
                        **Estimated Price:** ₹{result['price']}  
                        **Description:** {result['description']}
                        """)
                        # Save to history (image bytes, result)
                        st.session_state.history.append({
                            "image_bytes": uploaded_file.getvalue(),
                            "image_type": uploaded_file.type,
                            "name": result['name'],
                            "price": result['price'],
                            "description": result['description']
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
                st.markdown(f"""
                **Name:** {entry['name']}  
                **Estimated Price:** ₹{entry['price']}  
                **Description:** {entry['description']}
                """)
            st.divider()
    else:
        st.info("No images have been analyzed yet. Upload an image on the Estimate page.")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>🖼️ Price Estimator AI | Built with Streamlit & FastAPI</p>",
    unsafe_allow_html=True
)