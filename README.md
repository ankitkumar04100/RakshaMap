# 🛡️ RakshaMap – AI-Powered Women-Centric Safety Mapper

<img width="1536" height="1024" alt="Designer (21)" src="https://github.com/user-attachments/assets/12781c59-5da1-4250-ad58-bd5613bd5ccf" />

RakshaMap is an AI-driven public safety intelligence platform designed to proactively enhance women’s safety in public spaces. Built as part of an AI for Good initiative, RakshaMap transforms safety from a reactive response into a predictive, data-driven system that helps individuals and communities make safer mobility decisions.

---

## 📌 Table of Contents

- Overview
- Elevator Pitch
- Problem Analysis
- Solution Overview: RakshaMap
- How RakshaMap Solves the Problem (Step-by-Step)
- User Flow (Exact Solution Flow)
- Why This Solution Is Effective
- Impact-Oriented Design Philosophy
- Key Takeaway for Judges
- Key Features
- How AI Is Used
- System Architecture
- Technology Stack
- Dataset Strategy
- Model Design & Logic
- Ethical AI & Bias Mitigation
- User Experience Design
- Use Cases
- Social Impact
- Challenges Faced
- Accomplishments
- What We Learned
- Future Roadmap
- Scalability & Deployment Vision
- Alignment with AI for Good
- Conclusion

---

## 🌍 Overview

Public safety is a universal concern, but women face disproportionately higher risks in public spaces due to social, infrastructural, and systemic factors. Despite the availability of emergency response tools, there remains a significant gap in **preventive safety intelligence**.

RakshaMap addresses this gap by using machine learning and geospatial analysis to **predict safety risk zones before incidents occur**, empowering women with actionable insights rather than reactive alerts.

---

## 🚀 Elevator Pitch

RakshaMap is a women-centric, AI-powered safety intelligence platform that predicts public risk zones using machine learning and location-based analysis. It enables safer route planning, real-time alerts, and preventive decision-making to reduce exposure to unsafe environments.

---

## ❗ Problem Analysis

### 1. The Reality of Public Safety for Women

Public safety is a shared concern, but women experience **disproportionately higher risk** in public spaces due to a combination of social, environmental, and systemic factors. Daily activities such as commuting for work, education, or personal needs often involve navigating environments where safety conditions are uncertain and constantly changing.

Key risk conditions commonly faced include:
- Poorly lit streets and transit areas
- Isolated routes with low human presence
- Time-based vulnerability, especially during late evening or early morning hours
- Limited real-time safety awareness
- Delayed response from emergency systems

These risks are not random; they follow **patterns influenced by time, location, and infrastructure**. However, most existing systems fail to capture or communicate these patterns proactively.

---

### 2. Why Existing Safety Solutions Are Inadequate

Current safety mechanisms largely focus on **reactive intervention**, meaning action is taken only after an incident has occurred or when a user manually triggers an alert.

Common limitations include:
- Emergency apps require the user to already be in danger
- CCTV systems focus on surveillance rather than prevention
- Helpline systems respond after distress is reported
- Static crime maps do not adapt to time-based risk variations
- Lack of personalized, location-specific safety intelligence

As a result, women often move through public spaces **without knowing the level of risk in advance**, reducing their ability to make informed decisions.

---

### 3. The Core Problem Statement

There is currently **no widely accessible, AI-driven system** that:
- Predicts safety risks before incidents occur
- Adapts risk assessment dynamically based on time and location
- Communicates safety intelligence in a simple, visual, and actionable form
- Focuses specifically on women’s safety while remaining inclusive

This gap leaves prevention largely unaddressed and places the burden of safety entirely on the individual at the moment of crisis.

---

## 💡 Solution Overview: RakshaMap

RakshaMap addresses this gap by redefining safety as a **predictive intelligence problem** rather than a reactive response problem.

It is designed as an **AI-powered, women-centric safety mapping platform** that uses machine learning and geospatial analysis to forecast risk levels across public locations and time windows.

Instead of asking *“What should I do when I’m in danger?”*, RakshaMap answers:
> *“How can I avoid danger before it happens?”*

---

## 🧠 How RakshaMap Solves the Problem (Step-by-Step)

### 1. Predictive Risk Assessment

RakshaMap uses supervised machine learning to analyze safety-related patterns based on:
- Time of day
- Geographic location
- Incident density patterns
- Area vulnerability indicators

The AI model generates a **risk score (0–100)** for each location-time combination, representing the probability of elevated safety risk.

---

### 2. Risk Categorization for Human Understanding

To ensure clarity and fast decision-making, risk scores are translated into intuitive categories:
- 🟢 **Safe Zone**
- 🟡 **Moderate Risk Zone**
- 🔴 **High Risk Zone**

This abstraction allows users to instantly understand safety conditions without technical complexity.

---

### 3. Visual Safety Intelligence Through Maps

RakshaMap presents AI predictions through an **interactive, color-coded map**, enabling users to:
- View safety conditions of surrounding areas
- Identify high-risk zones before entering them
- Compare alternative routes based on safety, not just distance

Visualization transforms raw AI output into **actionable safety awareness**.

---

### 4. Safer Route Recommendation

Unlike conventional navigation tools that prioritize speed or distance, RakshaMap emphasizes **risk avoidance**.

When multiple routes are available:
- High-risk zones are deprioritized
- Safer alternatives are suggested
- Users are empowered to choose routes aligned with personal safety

---

### 5. Real-Time Alerts and Awareness

RakshaMap enhances situational awareness by:
- Alerting users when approaching high-risk zones
- Highlighting time-sensitive changes in risk levels
- Encouraging proactive decision-making

This reduces reliance on emergency responses by promoting **early avoidance**.

---

## 👤 User Flow

RakshaMap is designed to provide safety insights with minimal user effort, ensuring quick access to critical information in real-world situations. The user flow prioritizes clarity, speed, and proactive risk awareness.

### Step-by-Step User Journey

1. **Application Launch**  
   The user opens the RakshaMap web or mobile application to access real-time safety information.

2. **Location & Time Detection**  
   The application requests location permission and automatically detects the current time, which are essential inputs for accurate risk prediction.

3. **Safety Map Visualization**  
   The user is presented with an interactive city map displaying color-coded safety zones:
   - **Green:** Low-risk areas  
   - **Yellow:** Moderate-risk areas  
   - **Red:** High-risk areas  

   The user’s current position is highlighted on the map.

4. **Destination Input**  
   The user enters or selects a destination. The system prepares multiple possible routes for evaluation.

5. **AI Risk Evaluation**  
   RakshaMap’s AI engine analyzes:
   - User location and destination
   - Time of day
   - Historical incident patterns  

   Based on this analysis, a risk score is generated for each route and zone.

6. **Safer Route Recommendation**  
   The application recommends the safest available route by avoiding high-risk zones while maintaining reasonable travel time.

7. **Real-Time Alerts & Monitoring**  
   As the user navigates:
   - The system continuously monitors movement
   - Alerts are triggered when approaching high-risk areas
   - Routes are dynamically adjusted if needed

8. **Safe Arrival & Completion**  
   The flow concludes when the user safely reaches the destination, completing the navigation session.

### Continuous Improvement Loop (Optional)

Users may optionally report unsafe locations or incidents, allowing the system to improve future risk predictions and community safety insights.

This user flow ensures that RakshaMap delivers actionable safety intelligence while remaining simple, intuitive, and effective for everyday use.

### User Flow Daigram

<img width="1536" height="1024" alt="Designer (23)" src="https://github.com/user-attachments/assets/64365da9-a3c7-4f8a-b9e7-a841d6a5a215" />

---

## 🎯 Why This Solution Is Effective

RakshaMap succeeds because it:
- Shifts safety from **reaction to prevention**
- Uses AI where pattern recognition is genuinely required
- Communicates complex predictions in a human-friendly way
- Addresses women’s safety directly while supporting broader public safety
- Aligns technology with real behavioral decision-making

---

## 🌱 Impact-Oriented Design Philosophy

RakshaMap is built on three guiding principles:
- **Predict** risks before they escalate
- **Prevent** exposure through informed choices
- **Protect** communities using responsible AI

By embedding these principles into its design, RakshaMap transforms AI from a technical tool into a **social safety enabler**.

---

## 🔐 Key Takeaway for Judges

RakshaMap does not attempt to replace emergency systems or law enforcement.  
Instead, it fills a critical gap by offering **preventive safety intelligence**, empowering women with foresight, confidence, and control over their mobility decisions.

This makes RakshaMap not just an application, but a **new way of thinking about public safety**.
 
---

## ✨ Key Features

- **AI-Generated Risk Scores (0–100)**  
  Each geographic zone is assigned a dynamic risk score based on time, location, and historical incident patterns, enabling data-driven safety awareness.

- **Risk Zone Classification**  
  Areas are categorized into **Safe**, **Moderate Risk**, and **High Risk** zones using AI predictions, allowing users to instantly understand safety levels.

- **Interactive, Color-Coded Safety Maps**  
  Real-time visual heatmaps help users quickly identify unsafe areas through intuitive red, yellow, and green overlays.

- **AI-Based Safer Route Recommendations**  
  The system evaluates multiple routes and recommends paths that minimize exposure to high-risk zones without significantly increasing travel time.

- **Location-Based Safety Alerts**  
  Users receive proactive alerts when approaching or entering high-risk areas, enabling preventive action rather than reactive response.

- **Community & NGO Insight Support**  
  Aggregated insights help NGOs and community organizations identify recurring risk hotspots and plan targeted safety interventions.

- **Time-Sensitive Risk Analysis**  
  Safety predictions adapt automatically based on the time of day, recognizing that risk patterns change between daytime and nighttime.

- **Privacy-First Design**  
  No personal identity data is stored; all predictions are zone-based to ensure ethical and responsible AI use.

---

## 🧠 How AI Is Used

RakshaMap places artificial intelligence at the core of its safety prediction system. The platform uses supervised machine learning to analyze historical and contextual safety data and generate location-specific risk insights in real time.

### Why Supervised Learning?
Supervised learning is chosen because historical safety incidents provide labeled data that allows the model to learn clear patterns between environmental factors and risk levels. This approach ensures explainability, reliability, and consistent performance—critical for safety-focused applications.

### Data Inputs
The AI model processes multiple parameters that influence public safety risk:

- **Time of Day:** Risk patterns vary significantly across different hours
- **Location Coordinates:** Latitude and longitude define spatial context
- **Incident Density:** Frequency of reported incidents in nearby zones
- **Area Vulnerability Indicators:** Lighting conditions, isolation level, and crowd density (derived features)

### Feature Engineering
Raw data is transformed into meaningful features such as:
- Time-based risk windows
- Zone-level incident intensity
- Proximity to previously reported unsafe areas

This improves prediction accuracy and spatial sensitivity.

### Model Inference
The trained machine learning model evaluates these features and generates:
- A **numerical risk score (0–100)** representing safety probability
- A **risk category** classified as:
  - Safe
  - Moderate Risk
  - High Risk

### Real-Time Adaptability
Predictions are dynamically recalculated when:
- User location changes
- Time context shifts
- New safety data becomes available

This ensures that risk insights remain relevant and actionable.

### Role of AI in Decision-Making
AI predictions directly power:
- Heatmap visualization
- Safer route recommendations
- Real-time safety alerts

Rather than reacting to incidents, RakshaMap’s AI enables **proactive risk awareness and prevention**.

### Responsible AI Considerations
- No personal identity data is collected or stored
- Predictions are zone-based, not individual-based
- The system is designed to support decision-making, not replace human judgment

---

## 🏗️ System Architecture

RakshaMap is designed using a modular and scalable architecture that enables real-time safety risk prediction, intelligent routing, and clear visualization for users. The system integrates frontend interfaces, backend services, AI models, and geospatial tools into a unified workflow.

### Architecture Overview

The architecture consists of six primary layers:

### 1. User Layer
End users interact with RakshaMap through a web or mobile interface. The user provides location access and destination input, and receives real-time safety insights, alerts, and route recommendations.

### 2. Frontend Layer
The frontend is built using modern web technologies to ensure responsiveness and usability.
- Displays interactive maps and safety heatmaps
- Visualizes risk zones using color-coded overlays
- Shows safer route recommendations
- Receives real-time alerts and warnings

**Technologies:** React, HTML, CSS, JavaScript, Leaflet.js

### 3. Backend API Layer
The backend acts as the central orchestration layer, handling communication between the frontend, AI engine, database, and external services.
- Processes incoming requests from users
- Aggregates spatial and temporal data
- Invokes AI models for risk prediction
- Manages data flow and response formatting

**Technologies:** FastAPI, REST APIs

### 4. AI Risk Prediction Engine
The AI engine analyzes multiple parameters to estimate safety risks for different geographic zones.
- Considers location coordinates, time of day, and historical incident patterns
- Generates a numerical risk score for each zone
- Classifies areas into Safe, Moderate, or High-risk categories
- Continuously updates predictions based on new inputs

**Technologies:** Python, Scikit-learn

### 5. Data & Storage Layer
This layer stores and manages all historical and contextual data required for risk prediction.
- Historical incident records
- Geospatial metadata
- Time-based risk patterns

**Technology:** SQLite

### 6. Maps & Visualization Services
External mapping services are used to render base maps, routes, and spatial overlays.
- Provides accurate map rendering
- Supports route calculation and navigation
- Enables overlay of AI-generated risk zones

**Technologies:** Google Maps API, Geospatial Services

### Data Flow Summary
1. The user’s location and destination are sent from the frontend to the backend.
2. The backend fetches historical and contextual data from the database.
3. The AI engine processes inputs and generates risk scores.
4. Risk data is sent back to the backend.
5. The frontend updates heatmaps, routes, and alerts in real time.

This architecture ensures scalability, reliability, and effective integration of AI-driven safety intelligence into real-world navigation scenarios.

### Arhitecture Daigram

<img width="1536" height="1024" alt="Designer (22)" src="https://github.com/user-attachments/assets/58f243f3-cc1d-4718-b654-53e5bd400886" />

---

## ⚙️ Technology Stack

**Built with:**  
Python, FastAPI, Scikit-learn, React, JavaScript, HTML, CSS, Leaflet.js, Google Maps API, SQLite, REST APIs, Machine Learning, Geospatial Analysis

---

## 📊 Dataset Strategy

Due to limited open public safety datasets:
- Publicly available data was analyzed
- Realistic simulated datasets were created
- Patterns were validated logically and ethically

This approach is acceptable for hackathon prototyping.

---

## 🤖 Model Design & Logic

- Supervised learning approach
- Feature engineering focused on explainability
- Output normalized for user understanding
- Designed to avoid overfitting and bias amplification

---

## ⚖️ Ethical AI & Bias Mitigation

- No personally identifiable data used
- Risk scores are probabilistic, not deterministic
- Transparency prioritized over black-box predictions
- Women-centric focus without exclusionary design

---

## 🎨 User Experience Design

- Minimalist interface
- Color-coded clarity
- Low cognitive load
- Designed for fast decision-making in real-world scenarios

---

## 👥 Use Cases

- Women commuting at night
- College students
- Working professionals
- NGOs identifying risk hotspots
- Urban safety planners

---

## 🌱 Social Impact

RakshaMap aims to:
- Reduce exposure to unsafe areas
- Increase confidence in public mobility
- Enable preventive safety planning
- Support inclusive, safer cities

---

## 🚧 Challenges Faced

- Limited structured datasets
- Ethical sensitivity of safety prediction
- Balancing simplicity with technical depth
- Ensuring inclusivity while remaining women-centric

---

## 🏆 Accomplishments

- Built a predictive safety intelligence system
- Integrated AI with real-time mapping
- Delivered a socially relevant prototype
- Aligned strongly with AI for Good principles

---

## 📘 What We Learned

- Responsible AI matters more than raw accuracy
- Prevention creates greater impact than reaction
- Clear storytelling amplifies technical work
- Empathy is critical in social-tech solutions

---

## 🔮 Future Roadmap

- Real-time NGO and civic data integration
- SOS and emergency response features
- NLP-based crowd-sourced reports
- Safety dashboards for authorities
- Mobile application deployment

---

## 📈 Scalability & Deployment Vision

RakshaMap is designed to:
- Scale across cities
- Integrate with smart city initiatives
- Support policy and planning decisions
- Serve as a public safety intelligence layer

---

## 🌐 Alignment with AI for Good

RakshaMap supports:
- Gender Equality (UN SDG 5)
- Sustainable Cities (UN SDG 11)
- Responsible AI development
- Community-driven impact

---

## 🧾 Conclusion

RakshaMap demonstrates how artificial intelligence, when guided by responsibility and empathy, can drive meaningful social impact. By shifting safety from reaction to prediction, RakshaMap empowers women and communities with knowledge, confidence, and prevention-focused intelligence.

---

### 🔐 Predict • Prevent • Protect


