import streamlit as st

def main():

    # Create a text input widget
    user_input = st.text_input("Enter your input:")

    # Create a button that the user can click to trigger the model
    if st.button("Submit"):
        # Trigger the model with the user's input
        result = trigger_model(user_input)
  
    # Display the top entries returned by the model
    st.write("Top entries:")
    
    # Just for testing
    st.write(user_input)

# Here we would need to query the results, probably another function inside for the
# Cohere API calls
def trigger_model(user_input):
    return user_input

if __name__ == '__main__':
    main()