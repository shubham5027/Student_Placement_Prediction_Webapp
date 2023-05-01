
import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder


#loading trained model

pickle_file_path = r"C:\Users\LENOVO\Downloads\model_file_2"
loaded_model = pickle.load(open(pickle_file_path, 'rb'))



def placement_prediction(x):
    

    prediction = loaded_model.predict(x)
    print(prediction)

    st.subheader("Placement Result")
    if (prediction == 0):
        st.write("Sorry, it seems unlikely that you will be placed.")	
    else:
        st.write("Congratulations! You are likely to be placed.")
       
  

def main():

    
    #getting title & input from user
    st.title("Engineering Student Placement Prediction")
    st.subheader("Please complete the form for a successful prediction")
    st.sidebar.header("")
    stream = st.selectbox("Select Stream", ["Computer Science","Electrical Engineerng","Information Technology","Electronics & Communication Engineering","Mechanical Engineering","Civil Engineering"])
    age = st.slider("Enter Age", min_value=0, max_value=30, step=1)
    gender = st.selectbox("Select Gender", ["Male", "Female"])
    internship = st.slider("Internship", min_value=0, max_value=10, step=1)
    # backlogs = st.radio("Backlogs", ["Yes", "No"])
    backlogs = 1 if st.radio("Backlogs", ["Yes", "No"]) == "Yes" else 0
    cgpa = st.slider("Enter CGPA", min_value=0, max_value=10, step=1)
    

    gender_encoder = LabelEncoder()
    stream_encoder = LabelEncoder()
    backlog_encoder = LabelEncoder()

    x = np.array([[age, gender, stream, internship, cgpa, backlogs]])
    x[:, 1] = gender_encoder.fit_transform(x[:, 1])
    x[:, 2] = stream_encoder.fit_transform(x[:, 2])
    x[:, 5] = backlog_encoder.fit_transform(x[:, 5])
    x = x.astype(int)

    #code for prediction
    predict = ''

    # Check if the button was clicked
    if st.button("Test Result"):
        predict = placement_prediction(x)

    st.success(predict)


if __name__=='__main__':
    main()
# In this corrected code, the gender, stream, and backlogs columns are encoded using LabelEncoder and the encoder objects are defined and used inside the main function. The predict variable and the if st.button line are indented to be inside the main function, and the corrected gender variable is used in the x array.










if __name__=='__main__':
    main()
