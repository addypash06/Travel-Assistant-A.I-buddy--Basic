import streamlit as st
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()
client = genai.Client()
model_type  = ["gemini-3.5-flash-lite", "gemini-3.8-flash"]
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)
st.title("Travel Assistant 🌍")
st.caption("Tumhara personal travel planner")

location = st.text_input("Select location you wanna go?", placeholder="Eg. Paris")
days = st.number_input("Enter days: ", min_value=1, max_value=365)
budget = st.text_input("Choose budget",placeholder="Eg. ₹15,000")
no_of_people = st.slider("How many people",1,100,3)
places_to_be_cover = st.text_input("Specific interest places you want to visit in the given provided location", placeholder="Type here")
extras = st.text_area("Enter here anything you wanna do or want changes in plan:", placeholder="Eg. I prefer visiting nature more")
accm_budget = st.radio("What type of accommodation do you prefer?",["Mid-range", "Luxury", "Hostel", "Resort"])
food_type = st.radio("Which food do you prefer?", ["Pure Vegeterian", "Pure Non-vegeterian", "Vegeterian/Non-vegeterian", "Jain", "Vegan"])

prompt = f"""You are Travel Planner with 30+ years of experience. Your task 
is to plan the trip at {location} for {days} days. The budget is {budget}. The accomodation preference is {accm_budget}, then suggest areas/neighborhoods to stay in and explain why.
Divide the budget properly as per example given below and show its calculation mentioned in below example
Eg.

🏨 Accommodation    ₹10,000\n
🍜 Food              ₹5,000\n
🚕 Transportation    ₹4,000\n
🎟️ Activities        ₹3,000\n
🛍️ Miscellaneous     ₹3,000\n
────────────────────────────\n
Total                ₹25,000\n

{no_of_people} people will travel. Also compulsory cover {places_to_be_cover} alongside your recommendation & choices. Detailed {days}-Day Itinerary in detail along with time limitations. 
According to {food_type} provide the famous restaurants & famous local foods. Provide in this order: Breakfast -> Local lunch -> Cafe -> Dinner. Along with that provide famous food of that {location}.
Give importance to {extras} as well.  Provide all these answers in bullet points and make sure to add emojis as well not too much. 
Based on {location}, {days}, {no_of_people}, {extras} generate packing list as per below example each item under a category is placed on its own seperate line. Between item of previous category and new category should be seperated by 2 line.
Indicated with '\n' as a new line
Eg.

🎒 PACKING LIST\n
\n\n
**Clothing**:\n
☐ 4 T-shirts\n
☐ 2 Pants\n
☐ 1 Jacket\n
\n\n
**Essentials**:\n
☐ ID\n
☐ Charger\n
☐ Power bank\n
\n\n
**Activities**:\n
☐ Trekking shoes\n
☐ Sunscreen\n
☐ Water bottle\n
\n 

And add many more as per requirement
"""



if st.button("Plan Trip: "):
    if location and days and budget:
        interaction = client.interactions.create(
            model=model_type[0],
            input=prompt,
            generation_config={
                "temperature": 0.7,
                "top-k": 20,
                },
        )
        with st.spinner("Please wait!"):
            time.sleep(5)
        st.success("Plan Generated!")
        st.write(f"Your destination is **{location}**")
        st.write(f"No. of days: **{days}**")
        st.snow()
        st.write(interaction.output_text)

    else:
        st.warning("Please fill up the all above details")
else:
    st.warning("Please fill up the all above details")
