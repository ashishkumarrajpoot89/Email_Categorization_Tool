# import streamlit as st
# import pickle
# from db_connection import insert_feedback

# # Load model & vectorizer
# model = pickle.load(open("email_model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# st.title("📧 Email Categorization Tool")
# st.markdown("Classify emails into **Work, Personal, Promotions, or Spam** and give feedback to improve accuracy.")

# email_text = st.text_area("Enter Email Text:")
# if st.button("Classify"):
#     if email_text.strip():
#         X_vect = vectorizer.transform([email_text])
#         prediction = model.predict(X_vect)[0]
#         st.success(f"Predicted Category: **{prediction}**")

#         actual_category = st.selectbox("Is this correct? If not, select the actual category:",
#                                        ["", "work", "personal", "promotions", "spam"])
#         if st.button("Submit Feedback"):
#             if actual_category:
#                 insert_feedback(email_text, prediction, actual_category)
#                 st.info("✅ Feedback saved successfully!")



# import streamlit as st
# import pickle
# from db_connection import insert_feedback

# # Load model & vectorizer
# model = pickle.load(open("email_model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# st.title("📧 Email Categorization Tool")
# st.markdown("Classify emails into **Work, Personal, Promotions, or Spam** and give feedback to improve accuracy.")

# # --- Step 1: Text input ---
# email_text = st.text_area("Enter Email Text:")

# # --- Step 2: Classify ---
# if st.button("Classify"):
#     if email_text.strip():
#         X_vect = vectorizer.transform([email_text])
#         prediction = model.predict(X_vect)[0]
#         st.session_state["email_text"] = email_text
#         st.session_state["prediction"] = prediction
#         st.success(f"Predicted Category: **{prediction}**")

# # --- Step 3: Show feedback only if prediction exists ---
# if "prediction" in st.session_state:
#     st.success(f"Predicted Category: **{st.session_state['prediction']}**")
#     actual_category = st.selectbox(
#         "Is this correct? If not, select the actual category:",
#         ["", "work", "personal", "promotions", "spam"]
#     )
#     if st.button("Submit Feedback"):
#         if actual_category:
#             insert_feedback(
#                 st.session_state["email_text"],
#                 st.session_state["prediction"],
#                 actual_category
#             )
#             st.info("✅ Feedback saved successfully!")


import streamlit as st
import pickle
from db_connection import insert_feedback

# Load model & vectorizer
model = pickle.load(open("email_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📧 Email Categorization Tool")
st.markdown("Classify emails into **Work, Personal, Promotions, or Spam** and give feedback to improve accuracy.")

# Initialize session state
if "prediction" not in st.session_state:
    st.session_state.prediction = None
if "email_text" not in st.session_state:
    st.session_state.email_text = ""

# Input box
email_text = st.text_area("Enter Email Text:", value=st.session_state.email_text)

# Classify button
if st.button("Classify"):
    if email_text.strip():
        X_vect = vectorizer.transform([email_text])
        prediction = model.predict(X_vect)[0]
        st.session_state.prediction = prediction
        st.session_state.email_text = email_text
    else:
        st.warning("Please enter some text.")

# Show prediction and feedback form only if classification is done
if st.session_state.prediction:
    st.success(f"Predicted Category: **{st.session_state.prediction}**")

    actual_category = st.selectbox(
        "Is this correct? If not, select the actual category:",
        ["", "work", "personal", "promotions", "spam"]
    )

    if st.button("Submit Feedback"):
        if actual_category:
            insert_feedback(
                st.session_state.email_text,
                st.session_state.prediction,
                actual_category
            )
            st.info("✅ Feedback saved successfully!")
            # Reset state after submission
            st.session_state.prediction = None
            st.session_state.email_text = ""
        else:
            st.warning("Please select the actual category before submitting.")
