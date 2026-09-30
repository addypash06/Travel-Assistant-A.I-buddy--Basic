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
extras = st.text_area("Enter here anything you wanna do or want changes in plain:", placeholder="Eg. I prefer visiting nature more")

prompt = f"""You are Travel Planner with 30+ years of experience. Your task 
is to plan the trip at {location} for {days} days. The budget is {budget}. Divide the budget properly as per example given below and show its calculation mentioned in below example
Eg.
🏨 Accommodation    ₹10,000\n
🍜 Food              ₹5,000\n
🚕 Transportation    ₹4,000\n
🎟️ Activities        ₹3,000\n
🛍️ Miscellaneous     ₹3,000\n
────────────────────────────
Total                ₹25,000

{no_of_people} people will travel. Also compulsory cover {places_to_be_cover} alongside your recommendation & choices. 
Give importance to {extras} as well. Provide all these answers in bullet points and make sure to add emojis as well not too much.
"""



if st.button("Plan Trip: "):
    interaction = client.interactions.create(
        model=model_type[0],
        input=prompt,
        generation_config={
            "temperature": 0.7,
            "top-k": 20,
            # "max_output_tokens": 400
            },
    )
    with st.spinner("Please wait!"):
        time.sleep(5)
    st.write("Your destination is",location)
    st.write("No. of days:", days)
    st.success("Plan Generated!")
    st.snow()
    st.write(interaction.output_text)

else:
    st.warning("Please fill up the all above details")
