import streamlit as st
from scrap import return_data
from logic import edu_level, all_skills, pipeline
#from ai import ai_convo
from streamlit_extras.floating_button import *


st.title("Career Ideas!")

st.write("Fill out the info in the side bar, so we can get started!")
#sidebar buttons
st.sidebar.markdown("# Tell me about yourself!")

salary = st.sidebar.slider("Salary", 30160, 239200, 49500, 100, "$%d")
st.sidebar.space("xxsmall")

education_level = st.sidebar.radio("What education do you have?", edu_level)
st.sidebar.space("xxsmall")

three_skills = st.sidebar.multiselect("Pick 3 skills that you have", all_skills, max_selections=3)

# once have input, filter data accordingly 
if len(three_skills) == 3 and education_level:
    skill_one, skill_two, skill_three = three_skills
    
    filtered_data = pipeline(return_data(), education_level, salary, skill_one, skill_two, skill_three)

    # create columns to seperate data and navigation buttons
    col1, col2, col3 = st.columns([.5, 4, .5])
    job = filtered_data
    
    if "job_index" not in st.session_state:
        st.session_state.job_index = 0
        
    # make sure there is a job
    if not filtered_data:
        with col2:
            with st.container(border = True):
                st.warning("No job exists with these criteria. Please reinput criteria to try again")
                st.stop()

    current_job = job[st.session_state.job_index]

    with col2:
        with st.container(border = True):
            st.subheader(f"📌 Job: {current_job.get("job_name")}", text_alignment="center")
            st.text(f"💰 Salary: {current_job.get("salary")}", text_alignment="center")


    #Navigation buttons
    st.divider()
    with col1:
        if st.button("◀️ Prev"):
            if st.session_state.job_index > 0:
                st.session_state.job_index -=1

    with col3:
        if st.button("Next ▶️"):
            if st.session_state.job_index < len(job) - 1:
                st.session_state.job_index +=1

    st.write(f"Job {st.session_state.job_index + 1} of {len(job)}")





# if st.floating_button(":material/chat:"):
#     st.write("Chat button clicked!")

#     st.write("hello")
#     #ai_convo()