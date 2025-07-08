#!/usr/bin/env python3
"""
Startup script for the Smart Auction AI Frontend
"""

import subprocess
import sys
import os

def main():
    """Start the Streamlit frontend"""
    print("🎨 Starting Smart Auction AI Frontend...")
    print("📍 Frontend will be available at: http://localhost:8501")
    print("🔧 Press Ctrl+C to stop the frontend")
    print("-" * 50)
    
    try:
        # Start Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Frontend stopped by user")
    except Exception as e:
        print(f"❌ Error starting frontend: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 