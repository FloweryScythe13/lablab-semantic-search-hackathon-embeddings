import streamlit as st

from backend.get_similar_results import get_similar_results

def main():

    # Create a text input widget
    user_input = st.text_input("Enter your input:")

    # Create a button that the user can click to trigger the model
    if st.button("Submit"):
        # Trigger the model with the user's input
        result = get_similar_results(user_input)
  
        # Display the top entries returned by the model
        st.dataframe(data=result)

if __name__ == '__main__':
    main()