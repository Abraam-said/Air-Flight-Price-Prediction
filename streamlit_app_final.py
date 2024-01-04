
import joblib
import streamlit as st
import pandas as pd

# Load the trained model and input features
Model = joblib.load("Model_Final.pkl")
Inputs = joblib.load("Inputs_Final.pkl")

# Prediction function
def prediction(Airline, Source, Destination, Total_Stops, Has_Additional_Info, 
               journey_day, journey_month, dep_time_hour, dep_time_min,
               Arrival_Time_hour, Arrival_Time_minute, Duration_hours, Duration_minutes):
    
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0, 'Airline'] = Airline
    test_df.at[0, 'Source'] = Source
    test_df.at[0, 'Destination'] = Destination
    test_df.at[0, 'Total_Stops'] = Total_Stops
    test_df.at[0, 'Has_Additional_Info'] = Has_Additional_Info
    test_df.at[0, 'journey_day'] = journey_day
    test_df.at[0, 'journey_month'] = journey_month
    test_df.at[0, 'dep_time_hour'] = dep_time_hour
    test_df.at[0, 'dep_time_min'] = dep_time_min
    test_df.at[0, 'Arrival_Time_hour'] = Arrival_Time_hour
    test_df.at[0, 'Arrival_Time_minute'] = Arrival_Time_minute
    test_df.at[0, 'Duration_hours'] = Duration_hours
    test_df.at[0, 'Duration_minutes'] = Duration_minutes

    result = Model.predict(test_df)
    return result[0]

# Main function for Streamlit app
def main():
    # Setting up the page title and icon
    st.set_page_config(page_icon='✈️', page_title='Flight Price Prediction')

    # Add a title in the middle of the page using Markdown and CSS
    st.markdown("<h1 style='text-align: center;text-decoration: underline;color:SteelBlue'>Flight Price Prediction ✈️</h1>", unsafe_allow_html=True)

    # Sidebar styling
    st.sidebar.header("User Inputs")
    st.sidebar.subheader("Select Features:")
    Airline = st.sidebar.selectbox('Airline', ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia', 'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet']) 
    
    Source = st.sidebar.selectbox('Source', ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']) 
    
    Destination = st.sidebar.selectbox('Destination', ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])  
    
    Total_Stops = st.sidebar.selectbox('Total Stops', ['non-stop', '2 stops', '1 stop', '3 stops', '4 stops'])
    
    Has_Additional_Info = st.sidebar.selectbox('Has Additional Info', ['No', 'Yes'])  
    
    # Main content styling
    st.subheader("Enter Journey Details:")
    journey_day = st.slider('Journey Day', min_value=1, max_value=31, value=15, step=1)
    
    journey_month = st.slider('Journey Month', min_value=1, max_value=12, value=6, step=1)
        
    dep_time_hour = st.slider('Departure Time Hour', min_value=0, max_value=23, value=12, step=1)
    
    dep_time_min = st.slider('Departure Time Minute', min_value=0, max_value=59, value=30, step=1)
    
    Arrival_Time_hour = st.slider('Arrival Time Hour', min_value=0, max_value=23, value=18, step=1)
    
    Arrival_Time_minute = st.slider('Arrival Time Minute', min_value=0, max_value=59, value=45, step=1)
    
    Duration_hours = st.slider('Duration Hours', min_value=0, max_value=24, value=2, step=1)
    
    Duration_minutes = st.slider('Duration Minutes', min_value=0, max_value=59, value=30, step=1)
    
    # Prediction button and result
    if st.button('Predict Price'):
        results = prediction(Airline, Source, Destination, Total_Stops, Has_Additional_Info,
                             journey_day, journey_month, dep_time_hour, dep_time_min,
                             Arrival_Time_hour, Arrival_Time_minute, Duration_hours, Duration_minutes)
        st.success(f"The Predicted Price is ₹{int(results)}")

if __name__ == '__main__':
    main()
