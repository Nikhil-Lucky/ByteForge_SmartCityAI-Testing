# SmartCity AI - Demo Script (Suhas's Part)

## Setup for Demo
*Before the presentation, make sure the app is running locally via `streamlit run app.py`.*

## Section 1: The Emergency Sequence (Maps & Ambulance)

**(Context: It's your turn to speak. Nikhil has just introduced the project and the main interface.)**

**Suhas:**  
"Thanks Nikhil! Now, I’ll show you our system in action for one of the most critical civic issues: **Emergency Medical Response.**

Imagine a citizen is in a panic and just types natural language into the chat. Let’s simulate that."

> *Action: In the Streamlit app chat box, type:*  
> **"I need an ambulance in Jayanagar"**  
> *Action: Click 'Send'*

**Suhas:**  
"Immediately, the AI Router Agent detects this is a medical emergency. 

Behind the scenes, our system calculates the exact geographic distance to all available ambulances and hospitals in the city. Instead of just picking a random unit, it mathematically selects the absolute closest available ambulance—in this case, AMB001.

It also checks our live mock database for hospital bed availability, and routes the patient to the nearest facility that *actually has open beds*—Sagar Hospitals.

If you look at the dynamic map we generated here, you can see the exact routing in blue. But notice something interesting in the route? There’s a red detour."

> *Action: Point to the map, specifically the red polygon and the bend in the blue route line.*

**Suhas:**  
"Bengaluru often suffers from severe waterlogging during rains. Our system integrates with traffic and weather data. It detected a flooded zone on the main route, generated this red warning polygon, and automatically diverted the ambulance's route around the flood to save critical time. 

Finally, to build trust with the citizens, we added an **Explainability Engine**. Right below the map, the AI clearly explains *why* it made these choices in simple English."

> *Action: Point to the 'Why this recommendation?' box.*

## Section 2: The Live City Dashboard

**Suhas:**  
"Let’s zoom out from the individual emergency to the city-wide view."

> *Action: Click on the "🗺️ Live Map" tab in the sidebar.*

**Suhas:**  
"This is our SmartCity Control Room view. We’ve built an interactive dashboard for civic authorities. 
On this map, authorities can see the real-time status of all medical units. The markers are color-coded: blue ambulances are available, gray ones are busy. Green hospitals have plenty of capacity, while red ones are full.

Scroll down slightly, and you can see our real-time analytics. This bar chart dynamically tracks hospital bed availability across the city, allowing authorities to easily spot resource shortages before they become crises.

That's the power of intelligent routing and visualization. I'll pass it over to Sunay to show the Civic Complaints module!"
