import streamlit as st
import pickle
import numpy as np
import sklearn


genders = ['Male', 'Female']

programs = [
    'Electronics And Communication Engineering', 
    'Computer Science',
    'Information Technology', 
    'Mechanical Engineering',
    'Electrical Engineering', 
    'Civil Engineering'
   ]

backlogs = ['Yes', 'No']

# loading model
with open('model.sav', 'rb') as file:
        data = pickle.load(file)

# loading scaler
with open('scaler.sav', 'rb') as file:
    scaler = pickle.load(file)

model = data['model']
le_gender = data['le_gender']
le_stream = data['le_stream']
le_backlog = data['le_backlog']


# function for prediction page
def show_prediction():
    st.title('Engineering Student Placement Prediction')
    st.write('#### Please complete the form for a successful prediction')

    # accept user input and make pediction
    st.subheader('Program')
    program = st.selectbox('Program offered by student', programs)
    st.subheader('Age')
    age = st.slider('Indicate student age', 18, 30)
    st.subheader('Gender')
    gender = st.selectbox('Indicate student gender', genders)
    st.subheader('Internships')
    internships = st.slider('Number of internships student took', 0, 10)
    st.subheader('Backlogs')
    backlog = st.radio('Indicate if student has backlog history', backlogs)
    st.subheader('CGPA')
    cgpa = st.slider('CGPA of student', 1, 10)

    # predict returns True when clicked
    predict = st.button('Predict', help='click to get prediction')

    # when clicked
    if predict:
        # creating an array of the data
        x = np.array([[age, gender, program, internships, cgpa, backlog]])

        # encoding the data with an encoder
        x[:, 2] = le_stream.transform(x[:, 2])
        x[:, 1] = le_gender.transform(x[:, 1])
        x[:, 5] = le_backlog.transform(x[:, 5])

        x = x.astype(int)
        # scaling the encoded data
        scaled = scaler.transform(x)

        # prediction with scaled data
        prediction = model.predict(scaled)

        if prediction == 1:
            st.subheader('Student will be placed 🎉')
        elif prediction == 0:
            st.subheader("Student is likely not to be placed")