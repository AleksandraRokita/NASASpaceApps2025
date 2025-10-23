Vibe-coded application for NASA Space Apps Hackathon

This project is an interactive classification system for Kepler Objects of Interest (KOI) — potential exoplanets discovered by NASA’s Kepler mission.

Users can input stellar and planetary parameters such as stellar temperature, radius, orbital period, transit depth, or brightness, and the application — using a trained Random Forest model — predicts whether the object is classified as:

- Confirmed — verified exoplanet

- Candidate — possible exoplanet

- False Positive — signal caused by non-planetary effects

The model was trained on real data from the NASA Exoplanet Archive, focusing on transit signal analysis (brightness drops in star light curves).

The frontend, built with HTML + JavaScript, provides an intuitive interface for entering features and automatically fills in missing values with typical median data.
The backend, powered by FastAPI (Python), processes the input, performs classification, and returns both the predicted class and probabilities.

This allows users to explore how stellar and orbital parameters influence classification results and to understand how machine learning models interpret astronomical data in the context of exoplanet discovery.

