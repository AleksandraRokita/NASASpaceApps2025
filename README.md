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
<img width="985" height="551" alt="image" src="https://github.com/user-attachments/assets/43ba605f-865e-4e97-835a-30474b61f943" />
<img width="976" height="544" alt="image" src="https://github.com/user-attachments/assets/7aab4280-750b-43fd-b7f9-4bd518c976ae" />
<img width="978" height="546" alt="image" src="https://github.com/user-attachments/assets/41ddf02b-1a82-487b-be16-b9a81f2e8110" />




