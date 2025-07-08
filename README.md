# 🖼️ Smart Auction AI - Price Estimator

An intelligent AI-powered auction system that analyzes images and provides accurate price estimates for various items. Built with FastAPI backend and Streamlit frontend, this system uses advanced computer vision models to identify objects and estimate their market value.

## ✨ Features

- **AI-Powered Image Analysis**: Upload images to automatically identify objects and estimate their value
- **Smart Price Estimation**: Advanced algorithms consider item condition, market trends, and confidence levels
- **Multi-Item Support**: Analyze multiple images simultaneously
- **Condition-Based Pricing**: Adjust prices based on item condition (New, Used, Heavily Used)
- **Real-Time Analysis**: Fast processing with detailed breakdown of price calculations
- **History Tracking**: View and compare previous analyses
- **RESTful API**: Clean API endpoints for integration with other systems
- **Modern UI**: Beautiful, responsive interface built with Streamlit

## 🏗️ Architecture

```
auction-website/
├── app.py                 # Streamlit frontend application
├── backend/
│   ├── main.py           # FastAPI backend server
│   ├── auth_utils.py     # Authentication utilities
│   ├── model/
│   │   ├── predictor.py      # AI prediction models
│   │   └── clean_predictor.py # Clean prediction interface
│   └── utils/
│       └── image_preprocess.py # Image preprocessing utilities
├── frontend/             # Frontend assets
├── requirements.txt      # Python dependencies
├── start_auction_system.bat  # Windows startup script
├── start_backend.py      # Backend startup script
└── start_frontend.py     # Frontend startup script
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Windows 10/11 (for batch script) or any OS with Python

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd auction-website
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Option 1: Automated Startup (Windows)
```bash
start_auction_system.bat
```

#### Option 2: Manual Startup

**Start Backend Server:**
```bash
python start_backend.py
```

**Start Frontend (in new terminal):**
```bash
python start_frontend.py
```

#### Option 3: Direct Commands

**Backend:**
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Frontend:**
```bash
streamlit run app.py --server.port 8501
```

## 🌐 Access Points

- **Frontend Application**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📖 Usage Guide

### 1. Upload Images
- Navigate to the "Estimate" page
- Upload one or more images (JPG, PNG, WebP supported)
- Select item condition from dropdown

### 2. Get Price Estimates
- Click "Estimate Price & Description"
- View detailed breakdown including:
  - Item identification
  - Base price calculation
  - Condition adjustments
  - Confidence-based modifications
  - Final estimated price

### 3. View History
- Switch to "History" page
- Review all previous analyses
- Compare results across different items

## 🔧 API Endpoints

### POST `/predict/`
Analyze an image and return price estimates

**Parameters:**
- `file`: Image file (multipart/form-data)
- `condition`: Item condition (New/Used/Heavily Used)

**Response:**
```json
{
  "name": "Item Name",
  "description": "Detailed description",
  "confidence": 95.5,
  "breakdown": {
    "base_price": 50000,
    "condition": "Used",
    "condition_adjustment": "-25%",
    "price_after_condition": 37500,
    "confidence": 95.5,
    "confidence_adjustment": "0%",
    "final_price": 37500
  }
}
```

### GET `/health`
Health check endpoint

### GET `/supported-formats`
Get supported image formats

## 🛠️ Technology Stack

- **Backend**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **AI/ML**: PyTorch, TensorFlow, OpenCLIP
- **Image Processing**: Pillow (PIL)
- **Data Processing**: NumPy
- **HTTP Client**: Requests

## 📊 Supported Categories

The system can analyze and price various categories including:
- 🚗 Cars (Sports cars, convertibles)
- 📱 Electronics (Phones, laptops, TVs, cameras)
- 👜 Luxury Items (Handbags, watches)
- 🪑 Furniture (Sofas, armchairs)
- And more...

## 🔒 Security Features

- CORS middleware for cross-origin requests
- Input validation for uploaded files
- Error handling for malformed images
- Session state management for history

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   - Kill existing processes on ports 8000/8501
   - Or change ports in startup scripts

2. **Model loading errors**
   - Ensure all dependencies are installed
   - Check internet connection for model downloads

3. **Image upload failures**
   - Verify image format (JPG, PNG, WebP)
   - Check file size (max 10MB)

### Logs
- Backend logs are displayed in the terminal
- Frontend logs appear in Streamlit interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with Streamlit and FastAPI
- Powered by PyTorch and TensorFlow
- Uses OpenCLIP for image recognition

---

**Smart Auction AI** - Making auction pricing intelligent and accessible! 🎯
