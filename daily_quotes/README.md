# Daily Quotes API

A lightweight, database-free FastAPI application that serves a daily inspirational quote.

## Features

- **Deterministic**: Returns the same quote for everyone on the same day.
- **Database-free**: Quotes are stored in a static file (`data.py`).
- **Lightweight**: Built with FastAPI.
- **Keep-alive**: Includes a script to prevent free-tier hosting from sleeping.

## Setup & Run Locally

1.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Server**:

    ```bash
    uvicorn main:app --reload
    ```

3.  **Access the API**:
    Open `http://127.0.0.1:8000` in your browser.

## Deployment (Render)

1.  Push this repository to GitHub.
2.  Create a new **Web Service** on [Render](https://render.com/).
3.  Connect your GitHub repository.
4.  Render will automatically detect the `Procfile` and `requirements.txt`.
5.  Deploy!

## Keep Alive Script

Free-tier services often spin down after inactivity. You can use the `keep_alive.py` script to ping your API every 14 minutes.

**Usage:**

```bash
python keep_alive.py https://your-app-name.onrender.com/health
```

_Note: For best results on free hosting, it is recommended to run this script from a different machine (e.g., a local Raspberry Pi, a VPS, or use an external uptime monitor service)._

## React Native Connection Guide

Here is how to connect to this API from a React Native application.

### 1. Install Dependencies (if needed)

You can use the built-in `fetch` API, so no extra dependencies are strictly required.

### 2. Example Component

```javascript
import React, { useEffect, useState } from "react";
import { View, Text, ActivityIndicator, StyleSheet } from "react-native";

const DailyQuote = () => {
  const [quote, setQuote] = useState(null);
  const [loading, setLoading] = useState(true);

  // Replace with your deployed API URL
  const API_URL = "https://your-app-name.onrender.com/";

  useEffect(() => {
    fetchDailyQuote();
  }, []);

  const fetchDailyQuote = async () => {
    try {
      const response = await fetch(API_URL);
      const json = await response.json();
      setQuote(json.quote);
    } catch (error) {
      console.error("Error fetching quote:", error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.container}>
        <ActivityIndicator size="large" color="#0000ff" />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Quote of the Day</Text>
      <Text style={styles.quoteText}>"{quote}"</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
    backgroundColor: "#f5f5f5",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
  },
  quoteText: {
    fontSize: 18,
    fontStyle: "italic",
    textAlign: "center",
    color: "#333",
  },
});

export default DailyQuote;
```
