# SkyCast - Premium Weather Experience 🌤️

SkyCast is a modern, responsive, and premium weather dashboard built with **Django** and **OpenWeatherMap API**. It features a stunning glassmorphic UI, real-time weather data, and robust error handling.

![SkyCast Preview](weatherapp/weather/static/css/style.css) 

## ✨ Features

- **Glassmorphic UI**: A beautiful, translucent interface with backdrop-blurs and smooth animations.
- **Real-time Data**: Accurate weather information including Temperature, Humidity, Wind Speed, and "Feels Like" conditions.
- **Direct Metric Integration**: All data is fetched directly in Celsius for maximum accuracy.
- **Robust Error Handling**: Friendly user feedback when cities are not found or API limits are reached.
- **Fully Responsive**: Optimized for Mobile, Tablet, and Desktop screens.
- **Modern Tech Stack**: Built using Python, Django, CSS3, and FontAwesome.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- An OpenWeatherMap API Key (Sign up at [openweathermap.org](https://openweathermap.org/api))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/eswar-87/WeatherApp.git
   cd WeatherApp
   ```

2. **Initialize Environment Variables:**
   Create a `.env` file in the `weatherapp` directory and add your API key:
   ```env
   WEATHER_API_KEY=your_api_key_here
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Server:**
   ```bash
   cd weatherapp
   python manage.py runserver
   ```

5. **Open in Browser:**
   Navigate to `http://127.0.0.1:8000/`

## 🛠️ Project Structure

- `weather/`: The main Django app containing weather logic.
- `static/`: CSS and styling assets.
- `templates/`: HTML templates for the dashboard.
- `weatherapp/`: Project configuration and settings.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

Developed with ❤️ by [Eswar](https://github.com/eswar-87)
