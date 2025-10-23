<p align="center">
<h1>Vibe-coded exoplanet classifier for NASA Space Apps Hackathon</h1>

This project is an interactive classification system for Kepler Objects of Interest (KOI) — potential exoplanets discovered by NASA’s Kepler mission.

Users can input stellar and planetary parameters such as stellar temperature, radius, orbital period, transit depth, or brightness, and the application — using a trained Random Forest model — predicts whether the object is classified as:

- Confirmed — verified exoplanet

- Candidate — possible exoplanet

- False Positive — signal caused by non-planetary effects

The model was trained on real data from the NASA Exoplanet Archive, focusing on transit signal analysis (brightness drops in star light curves).

The frontend, built with HTML + JavaScript, provides an intuitive interface for entering features and automatically fills in missing values with typical median data.
The backend, powered by FastAPI (Python), processes the input, performs classification, and returns both the predicted class and probabilities.

This allows users to explore how stellar and orbital parameters influence classification results and to understand how machine learning models interpret astronomical data in the context of exoplanet discovery.
<img width="1422" height="730" alt="image" src="https://github.com/user-attachments/assets/99c5159a-128b-4009-9efd-e4ce2ee25b41" />
<img width="1422" height="649" alt="image" src="https://github.com/user-attachments/assets/39aa4f33-29bd-4fa4-abf7-d8ba7071b75d" />
<img width="1422" height="735" alt="image" src="https://github.com/user-attachments/assets/6c083dd4-ae76-418b-8656-042869b9d940" />


<img width="979" height="546" alt="image" src="https://github.com/user-attachments/assets/ca55bd34-9da6-4830-a780-6815b1c34058" />

<img width="976" height="544" alt="image" src="https://github.com/user-attachments/assets/7aab4280-750b-43fd-b7f9-4bd518c976ae" />
<img width="978" height="546" alt="image" src="https://github.com/user-attachments/assets/41ddf02b-1a82-487b-be16-b9a81f2e8110" />
</p>


