# 🌿 EcoMind AI - Sustainable Living Copilot

EcoMind AI is a minimalist, AI-powered web application designed to help users make more sustainable choices in their daily lives. Instead of being a general-purpose chatbot, it provides targeted, actionable advice in three specific areas: sustainable swaps, waste management, and daily eco-challenges.

## 🚀 What this program does

1.  **Green Swap**: Suggests an eco-friendly alternative to a common product or habit (e.g., "Plastic straws" $\rightarrow$ "Bamboo or stainless steel straws").
2.  **Waste Wizard**: Helps you sort your trash. Tell it what you have, and it tells you if it belongs in the **Recycle**, **Compost**, or **Landfill** bin.
3.  **Eco-Challenge**: Provides a random, simple, and impactful daily micro-challenge to encourage a sustainable lifestyle.

## 🛠️ Technical Stack

-   **Frontend**: HTML5, Tailwind CSS (Minimalist Green Theme).
-   **Backend**: Python FastAPI.
-   **AI Engine**: Gemma 4B (running locally via Ollama).

## 📖 How to Use

### 1. Prerequisites
-   **Ollama installed**: [Download Ollama](https://ollama.com/)
-   **Gemma 4B model**: Run the following command in your terminal to download the model:
    ```bash
    ollama run gemma:4b
    ```
-   **Python 3.9+** installed.

### 2. Installation & Setup

1.  **Clone/Download** this project folder.
2.  **Install dependencies**:
    ```bash
    pip install fastapi uvicorn requests
    ```
3.  **Start the Backend**:
    ```bash
    python main.py
    ```
    The server will start at `http://localhost:8000`.

### 3. Running the App
-   Open `index.html` in any modern web browser.
-   Select a mode (Swap, Waste, or Challenge).
-   Type your query and click the green button!

## 🎨 Design Philosophy
The UI follows a **minimalist, nature-inspired aesthetic** using a light mint green background and forest green accents to evoke a feeling of calm and environmental consciousness.
