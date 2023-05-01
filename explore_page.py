import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter


programs = [
    'All',
    'Electronics And Communication Engineering', 
    'Computer Science',
    'Information Technology', 
    'Mechanical Engineering',
    'Electrical Engineering', 
    'Civil Engineering'
   ]


@st.cache
def load_data():
    # load and clean the data for graphing
    df = pd.read_csv('collegePlace.csv')

    # renaming the engineering programs
    eng = ['Mechanical', 'Electronics And Communication', 'Electrical', 'Civil']
    for x in eng:
        df['Stream'] = df['Stream'].replace(x, x +' Engineering')

    return df

# loading data
df = load_data()

def all():
    # programs offered by students in the dataset
    counter = Counter(df['Stream'])
    stream = counter.most_common()
    value1 = [x[0] for x in stream]
    count1 = [x[1] for x in stream]
    title = "Programs offered by students(count)"
    fig1 = px.bar(stream, x=value1, y=count1, title=title)

    # students placed/not placed
    counter = Counter(df['PlacedOrNot'])
    placed = counter.most_common()
    value2 = [x[0] for x in placed]
    count2 = [x[1] for x in placed]
    fig2 = px.pie(placed, names=['Placed', 'Not placed'], values=count2, color=value2, 
                hole=0.5, title='Percentage of students placed/not placed')

    # CGPA of students
    counter = Counter(df['CGPA'])
    cgpa = counter.most_common()
    value3 = [x[0] for x in cgpa]
    count3 = [x[1] for x in cgpa]
    fig3 = px.bar(cgpa, x=value3, y=count3, color=value3, labels={'x': 'CGPA', 'y': 'count'}, 
                title='CGPA of students')

    return fig1, fig2, count2, fig3

def graph_program(program):
    # {program} == program chosen for graph to be drawn
    df2 = df[df['Stream'] == program]
    # males compared to females who offered {program}
    counter = Counter(df2['Gender'])
    gender = counter.most_common()
    value1 = [x[0] for x in gender]
    count1 = [x[1] for x in gender]
    title = "Males and Females who offered {}".format(program)
    fig1 = px.pie(gender, names=value1, values=count1, color=value1, hole=0.5, title=title)

    # {program} students placed/not placed
    counter = Counter(df2['PlacedOrNot'])
    placed = counter.most_common()
    value2 = [x[0] for x in placed]
    count2 = [x[1] for x in placed]
    fig2 = px.pie(placed, names=['Placed', 'Not placed'], values=count2, color=value2, 
                hole=0.5, title='Percentage of {} students placed/not placed'.format(program))

    # CGPA of {program} students
    counter = Counter(df2['CGPA'])
    cgpa = counter.most_common()
    value3 = [x[0] for x in cgpa]
    count3 = [x[1] for x in cgpa]
    fig3 = px.bar(cgpa, x=value3, y=count3, color=value3, labels={'x': 'CGPA', 'y': 'count'}, 
                  title='CGPA of {} students'.format(program))

    return fig1, count1, fig2, count2, fig3


def explore_graphs():
    st.title("Explore data")
    selection = st.selectbox('Select data to display', programs)

    if selection == 'All':
        # plotting graphs
        fig1, fig2, count2, fig3, = all()
        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)
        col1, col2 = st.columns(2)
        col1.metric(label='Placed', value=count2[0])
        col2.metric(label='Not Placed', value=count2[1])
        st.plotly_chart(fig3, use_container_width=True)
        col3, col4 = st.columns(2)
        col3.metric(label='Lowest CGPA', value=5)
        col4.metric(label='Highest CGPA', value=9)
    else:
        fig1, count1, fig2, count2, fig3 = graph_program(selection)
        st.plotly_chart(fig1, use_container_width=True)
        col1, col2 = st.columns(2)
        col1.metric(label='Male', value=count1[0])
        col2.metric(label='Female', value=count1[1])
        st.plotly_chart(fig2, use_container_width=True)
        col3, col4 = st.columns(2)
        col3.metric(label='Placed', value=count2[0])
        col4.metric(label='Not Placed', value=count2[1])
        st.plotly_chart(fig3, use_container_width=True)
        df2 = df[df['Stream'] == selection]
        col5, col6 = st.columns(2)
        col5.metric(label='Lowest CGPA', value=int(df2['CGPA'].min()))
        col6.metric(label='Highest CGPA', value=int(df2['CGPA'].max()))