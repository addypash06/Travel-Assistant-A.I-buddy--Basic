import streamlit as st
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()
client = genai.Client()
model_type  = ["gemini-3.5-flash-lite", "gemini-3.8-flash"]
st.title("Travel Assistant 🌍")
st.caption("Tumhara personal travel planner")

location = st.text_input("Where do you wanna go?")
days = st.number_input("Enter days: ", min_value=1, max_value=365)
budget = st.radio("Choose budget", ["10,000-50,000", "50,000-1,00,000", "1,00,000 and more"])

prompt = f"""You are Travel Planner with 30+ years of experience. Your task 
is to plan the trip at {location} for {days} days. The budget is {budget} Provide answers in bullet points
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
