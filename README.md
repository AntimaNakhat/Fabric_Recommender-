# 🌤️ Fabric Recommender Web App

This Flask-based web application recommends suitable fabrics based on real-time weather data and user-selected activities. It fetches weather information from the OpenWeatherMap API and matches conditions with a dataset of fabric preferences to provide smart textile suggestions.


---

## 📦 Features

- 🔍 Get current weather data by city
- 🎯 Input your activity to get personalized fabric suggestions
- 📚 Search fabric information manually by name
- 🧵 Dataset-driven logic for fabric suitability based on:
  - Temperature
  - Humidity level
  - Activity type

---



![Screenshot 2025-05-31 170929](https://github.com/user-attachments/assets/c537e45a-2fb5-4890-ac53-fa0bd6e92b89)

![Screenshot 2025-05-31 170956](https://github.com/user-attachments/assets/5f47934f-0cbf-4fd4-b188-915f51b6cef2)

![Screenshot 2025-05-31 171037](https://github.com/user-attachments/assets/1da20bf4-171f-4c9b-b108-65f96835af00)




## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, Jinja2 (via Flask templates)
- **API:** OpenWeatherMap
- **Data Handling:** Pandas
- **Deployment:** Render

---

## 📁 Project Structure

```bash
.
├── fabric_data.csv
├── templates/
│   ├── index.html
│   └── fabric_info.html
├── .env
├── app.py
├── requirements.txt
└── README.md

```

## 🔗 Live Demo

> 🚀 Deployed on [Render](https://render.com/) — [Visit the live app](https://smart-fabric-recommender.onrender.com)

⚠️ Note on Deployment
While this application is deployed on Render for quick access, there may be occasional issues with API response, UI rendering, or output visibility due to hosting limitations or configuration differences.

If the hosted version does not function as expected, we recommend cloning the repository and running the application locally to ensure full functionality. Please follow the setup instructions below to deploy the project on your local system.
### 🚀 Setup & Deployment

---

1. Clone the Repository
   
```git clone https://github.com/your-username/fabric-recommender.git```
```cd fabric-recommender```

2. Create and Activate Virtual Environment

```python -m venv venv```
```source venv/bin/activate```  # On Windows: venv\Scripts\activate

3. Install Dependencies

```pip install -r requirements.txt```

4. Create .env File

Create a .env file in the root directory and add your OpenWeatherMap API key:

```API_KEY=your_openweathermap_api_key```

5. Run the Application Locally

```python app.py```

Visit http://127.0.0.1:5000/ in your browser.



