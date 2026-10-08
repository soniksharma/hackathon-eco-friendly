# 🌿 EcoMind AI: Sustainable Living Copilot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI: Gemma 4B](https://img.shields.io/badge/AI-Gemma--4B-blue)](https://ollama.com)
[![Backend: FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688)](https://fastapi.tiangolo.com/)
[![Frontend: Tailwind CSS](https://img.shields.io/badge/Frontend-Tailwind--CSS-38B2AC)](https://tailwindcss.com/)

**EcoMind AI** is a minimalist, purpose-built AI companion designed to bridge the gap between environmental awareness and daily action. It transforms the overwhelming task of "living sustainably" into three simple, actionable tools.

---

## 🌟 Features: How it Works

EcoMind AI is designed for simplicity. Each tool serves a specific purpose:

### 1. 🔄 Green Swap
**The Goal:** Replace polluting habits with sustainable ones.
*   **How it works:** The user inputs a common product (e.g., "Plastic wrap"). The AI analyzes the material and suggests a high-impact, sustainable alternative (e.g., "Beeswax wraps").
*   **User Experience:** `Input Product` $\rightarrow$ `Instant Green Alternative`.

### 2. 🧙 Waste Wizard
**The Goal:** Eliminate recycling confusion and reduce landfill contamination.
*   **How it works:** The user describes an item they are disposing of. The AI determines the correct waste stream—**Recycle, Compost, or Landfill**—and provides a brief explanation why.
*   **User Experience:** `Input Item` $\rightarrow$ `Correct Disposal Bin`.

### 3. 🎯 Eco-Challenge
**The Goal:** Build sustainable habits through gamification.
*   **How it works:** With a single click, the AI generates a random, achievable "micro-mission" for the day (e.g., "Take a 5-minute shower").
*   **User Experience:** `Click Button` $\rightarrow$ `Daily Green Mission`.

---

## 🛠️ Technical Architecture

### 🧠 The Intelligence: Local LLM
Unlike traditional AI apps that rely on cloud-based APIs, EcoMind AI is powered by **Gemma 4B running locally via Ollama**. 

**Why Local AI?**
*   **Zero Carbon Cloud Cost:** By processing requests locally, we reduce the massive energy consumption associated with cloud data centers, aligning the technology with the project's mission.
*   **Total Privacy:** User queries never leave the machine.
*   **Offline Capability:** The core intelligence works without an internet connection once the model is downloaded.

### ⚙️ The Backend: FastAPI
We used **FastAPI** for the server because of its extreme speed and asynchronous capabilities. 
*   **Expert Prompting**: The backend uses specialized prompt templates to ensure the LLM provides concise, actionable answers rather than long-winded conversational text.
*   **CORS Integration**: Seamlessly connects the Python logic to the web-based frontend.

### 🎨 The Frontend: Minimalist Design
The UI is built with **Tailwind CSS**, focusing on a "Nature-Inspired" aesthetic.
*   **Color Palette**: Mint Green (`#f0fff4`) for serenity, Forest Green (`#2f855a`) for action.
*   **Glassmorphism**: Uses blurred, semi-transparent cards to create a modern, airy feel.
*   **Responsiveness**: Fully optimized for both desktop and mobile browsers.

---

## 🚀 Getting Started

### Prerequisites
- [Ollama](https://ollama.com/) installed.
- Gemma 4B model downloaded: `ollama run gemma4:e4b`
- Python 3.9+

### Installation
1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/EcoMind-AI.git
   cd EcoMind-AI
   ```

2. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn requests
   ```

3. **Run the Backend:**
   ```bash
   python main.py
   ```

4. **Launch the App:**
   Open `index.html` in your preferred web browser.

---

## 📈 Future Roadmap
- [ ] **Vision AI**: Integrate a camera to identify waste materials automatically.
- [ ] **Local Database**: Use RAG (Retrieval Augmented Generation) to connect to specific city recycling guidelines.
- [ ] **Progress Tracking**: A dashboard to track completed Eco-Challenges.

---
*Built with 🌿 for a better planet.*
