import streamlit as st
from logic import edu_level, all_skills, query_pipeline, query_average_skill_with_education, query_average_education_by_salary
from ai import ai_convo
import pandas as pd
from api import quit_rate_api

#region Set up page
st.set_page_config(page_title = "Career Ideas", page_icon = "💼", layout = "wide")
st.title("Career Ideas!",)

st.write("Fill out the info in the side bar, so we can get started!")

#tabs
tab1, tab2, tab3 = st.tabs(["Find a job!", "Get data", "Ask AI"])

#sidebar buttons
st.sidebar.markdown("# Tell me about yourself!")

salary = st.sidebar.slider("Salary", 30160, 239200, 49500, 100, "$%d")
st.sidebar.space("xxsmall")

education_level = st.sidebar.radio("What education do you have?", edu_level)
st.sidebar.space("xxsmall")

three_skills = st.sidebar.multiselect("Pick 3 skills that you have", all_skills, max_selections=3)

# wait for input 
if len(three_skills) != 3: 
    st.stop()

if not education_level:
    st.stop()

skill_one, skill_two, skill_three = three_skills

filtered_data = query_pipeline(education_level, salary, skill_one, skill_two, skill_three)
#endregion

#region Get Job Info (Tab 1)
with tab1:
    # create columns to seperate data and navigation buttons
    colbtn1, colbtn2, colbtn3 = st.columns([1, 6, 1])
    job = filtered_data
        
    # make sure there is a job that fits criteria 
    if not filtered_data:
        with colbtn2:
            with st.container(border = True):
                st.warning("No job exists with these criteria. Please reinput criteria to try again")
                st.stop()


    #region Create navigation buttons
    if "job_index" not in st.session_state:
        st.session_state.job_index = 0
        st.session_state.job_index %=len(job)

    with colbtn1:
        st.space("xxlarge")
        prev = st.button("◀️ \n Prev")

    with colbtn3:
        st.space("xxlarge")
        next = st.button("▶️ \n Next")

    if prev:
            st.session_state.job_index = (st.session_state.job_index - 1) % len(job)

    if next:
        st.session_state.job_index = (st.session_state.job_index + 1) % len(job)
    #endregion


    current_job = job[st.session_state.job_index]

    #show "job card"
    with colbtn2:
        with st.container(border = True):
            st.subheader(f"📌 {current_job.get('job_name')}", text_alignment="center")
            st.subheader(f"💰 ${(current_job.get('salary')):,}", text_alignment="center")
            st.markdown(f"**Job Description:** {current_job.get('description')}")
            st.markdown(f"**Work Environment:** {current_job.get('work_environment')}")

            col21, col22, col23, col24, col25 = st.columns([1, 3, 2, 3, 1])
            with col22:
                st.text("✔️ Many jobs available" if float(current_job.get('openings').replace(",","")) > 10 else "❌ Not many jobs available", text_alignment= "center")
            with col24:
                st.text("✔️ Many self-employed" if float(current_job.get("self_employed")) > 5.8 else "❌ Not many self employed", text_alignment= "center")
            

    #job number
    col_pgnmbr1, col_pgnmbr2, col_pgnmbr3 = st.columns([3, 1, 3])
    with col_pgnmbr2:
        st.text(f"Job {st.session_state.job_index + 1} of {len(job)}", text_alignment = "center")
#endregion

#region Get Visuals (Tab 2)
with tab2:
    edu = 1 if education_level != "No formal educational credential" else None
    st.subheader("🛠️ Average skills needed in a job with" + (("a" + f"{education_level.lower()}") if edu else (f" {education_level.lower()}")), text_alignment="center")
    visual_skill_edu = query_average_skill_with_education(education_level)
    visual_skills = visual_skill_edu.keys()
    visual_education_needed = [edu for edu in visual_skill_edu.values()]

    df = pd.DataFrame(
        {
            "Skills": visual_skills,
            "Average amount needed": visual_education_needed
        })

    st.bar_chart(df, x = "Skills", y = "Average amount needed")

    st.space("medium")
    # visual_edu_salary = query_average_education_by_salary(salary)
    # st.subheader("🎓Average education needed by a job making $")

    st.space("medium")
    rows = []

    quit_rates = quit_rate_api()
    df = pd.DataFrame(quit_rates)
    st.line_chart(df["value"])
    # visual_skills = quit_rate_api.keys()
    # visual_education_needed = [edu for edu in visual_skill_edu.values()]


#endregion

#region AI Conva (Tab 3)
with tab3:
    st.header("Ask me more!")

    ai_convo()
#endregion