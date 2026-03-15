import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

st.set_page_config(page_title="BAAMT", page_icon="🧠", layout="centered")

st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")

st.markdown("""
BAAMT is a behavioural strategy tool that helps advocacy organisations design
effective campaigns by aligning messaging with the **moral values,
risk perceptions, institutional roles, and geographic contexts of
their target audiences**.

The framework integrates insights from **Moral Foundations Theory,
behavioural public policy, and decision science**. These fields suggest
that advocacy succeeds not only through evidence, but through alignment
with the moral intuitions, social identities, and institutional
expectations of different audiences.
""")

st.markdown("---")

# ---------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------

st.header("Audience Context")

audience_type = st.selectbox(
"Audience Type",
[
"General Public",
"Policy Makers",
"Corporate Stakeholders",
"Students",
"Civil Society Organisations"
]
)

stakeholder_level = st.selectbox(
"Stakeholder Influence Level",
[
"Low influence stakeholders",
"Moderate influence stakeholders",
"High influence institutional actors"
]
)

geography = st.selectbox(
"Geographic Context",
[
"India",
"Global North",
"Global South",
"International"
]
)

campaign_type = st.selectbox(
"Campaign Objective",
[
"Behaviour Change",
"Policy Reform",
"Corporate Engagement",
"Public Awareness"
]
)

st.markdown("---")

# ---------------------------------------------------
# QUESTIONNAIRE
# ---------------------------------------------------

st.header("Behavioural Assessment")

st.markdown("Rate each statement from **1 (Strongly Disagree)** to **5 (Strongly Agree)**.")

q1 = st.slider("Preventing suffering should be a top priority in public policy.",1,5)
q2 = st.slider("Fair treatment matters even if it requires economic trade-offs.",1,5)
q3 = st.slider("Society functions best when people respect authority.",1,5)
q4 = st.slider("Loyalty to one's community should guide major decisions.",1,5)
q5 = st.slider("Purity and moral integrity are important social values.",1,5)

q6 = st.slider("Avoiding harm to vulnerable beings is an ethical responsibility.",1,5)
q7 = st.slider("Rules and laws should be followed even when inconvenient.",1,5)
q8 = st.slider("Fairness should guide economic systems.",1,5)
q9 = st.slider("Communities should protect traditions.",1,5)
q10 = st.slider("Some actions are morally wrong regardless of consequences.",1,5)

care=(q1+q6)/2
fairness=(q2+q8)/2
authority=(q3+q7)/2
loyalty=(q4+q9)/2
purity=(q5+q10)/2

generate=st.button("Generate Advocacy Strategy")

if generate:

    st.header("Audience Moral Profile")

    st.write("Care:",round(care,2))
    st.progress(care/5)

    st.write("Fairness:",round(fairness,2))
    st.progress(fairness/5)

    st.write("Authority:",round(authority,2))
    st.progress(authority/5)

    st.write("Loyalty:",round(loyalty,2))
    st.progress(loyalty/5)

    st.write("Purity:",round(purity,2))
    st.progress(purity/5)

    st.markdown("---")

# ---------------------------------------------------
# RADAR CHART
# ---------------------------------------------------

    labels=['Care','Fairness','Authority','Loyalty','Purity']
    values=[care,fairness,authority,loyalty,purity]

    angles=np.linspace(0,2*np.pi,len(labels),endpoint=False)
    values=np.concatenate((values,[values[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    fig=plt.figure()
    ax=fig.add_subplot(111,polar=True)

    ax.plot(angles,values)
    ax.fill(angles,values,alpha=0.25)
    ax.set_thetagrids(angles[:-1]*180/np.pi,labels)

    st.pyplot(fig)

# ---------------------------------------------------
# SEGMENTATION
# ---------------------------------------------------

    if care>4 and fairness>4:
        segment="Compassion-oriented reform audience"
    elif authority>4:
        segment="Institutionally oriented audience"
    elif loyalty>4:
        segment="Community identity audience"
    elif purity>4:
        segment="Moral purity audience"
    else:
        segment="Mixed moral orientation audience"

    st.subheader("Behavioural Segment")
    st.write(segment)

# ---------------------------------------------------
# REFORM ORIENTATION
# ---------------------------------------------------

    if fairness+care>authority+loyalty:
        reform="This audience demonstrates a reform-oriented outlook and may be receptive to arguments about improving institutions, correcting injustices, and modernising systems."
    else:
        reform="This audience demonstrates a stability-oriented outlook and may prioritise social order, institutional continuity, and gradual reform rather than disruptive change."

    st.subheader("Reform Orientation")
    st.write(reform)

# ---------------------------------------------------
# RISK PROFILE
# ---------------------------------------------------

    if authority+purity>fairness+care:
        risk="The audience appears risk sensitive and may respond strongly to messages emphasising threats, institutional failure, or public health risks."
    else:
        risk="The audience appears opportunity oriented and may respond more positively to messaging about innovation, progress, and constructive change."

    st.subheader("Risk Profile")
    st.write(risk)

# ---------------------------------------------------
# ADVOCACY LEVER
# ---------------------------------------------------

    if campaign_type=="Policy Reform":
        lever="Regulatory reform and legislative engagement"

    elif campaign_type=="Corporate Engagement":
        lever="Corporate accountability and market incentives"

    else:
        lever="Public awareness and social norm change"

    st.subheader("Primary Advocacy Lever")
    st.write(lever)

# ---------------------------------------------------
# GEOGRAPHY ADJUSTMENT
# ---------------------------------------------------

    if geography=="India":
        geo_note="Messaging in India may benefit from references to food security, farmer livelihoods, and cultural traditions around plant-forward diets."

    elif geography=="Global North":
        geo_note="Messaging in Global North contexts often resonates when linked to sustainability, animal welfare standards, and climate change."

    elif geography=="Global South":
        geo_note="Messaging may need to emphasise development goals, livelihoods, and equitable food systems."

    else:
        geo_note="International audiences may respond best to framing around global sustainability and planetary health."

    st.subheader("Geographic Context")
    st.write(geo_note)

# ---------------------------------------------------
# STAKEHOLDER POWER
# ---------------------------------------------------

    if stakeholder_level=="High influence institutional actors":
        stakeholder_note="Advocacy targeting high influence actors should prioritise credible evidence, institutional legitimacy, and policy feasibility."

    elif stakeholder_level=="Moderate influence stakeholders":
        stakeholder_note="Moderately influential stakeholders can often act as coalition partners and intermediaries."

    else:
        stakeholder_note="Lower influence stakeholders are often more responsive to grassroots mobilisation and public narrative change."

    st.subheader("Stakeholder Strategy")
    st.write(stakeholder_note)

# ---------------------------------------------------
# CAMPAIGN STRATEGY PLAN
# ---------------------------------------------------

    strategy_plan=f"""
An advocacy campaign targeting **{audience_type}** within the
**{geography}** context should combine the advocacy lever of
**{lever}** with messaging that reflects the audience's dominant
moral concerns.

Campaign communications should balance **moral framing,
credible evidence, and strategic narrative building** in order
to influence both public perception and institutional decision
making.
"""

    st.subheader("Campaign Strategy Plan")
    st.write(strategy_plan)

# ---------------------------------------------------
# ADVOCACY STRATEGY
# ---------------------------------------------------

    strategy=f"""
Effective advocacy in this context will require designing messages
that align with the moral intuitions and institutional expectations
of the audience.

Campaign narratives should combine **ethical framing,
policy credibility, and emotionally resonant storytelling**
to influence how audiences interpret the issue.

The strategy should therefore integrate **public narrative,
policy engagement, and coalition building** to maximise impact.
"""

    st.subheader("Advocacy Strategy")
    st.write(strategy)

# ---------------------------------------------------
# PDF REPORT
# ---------------------------------------------------

    if st.button("Download Strategy Brief"):

        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size=12)

        report=f"""
BAAMT Behavioural Advocacy Strategy Report

Audience: {audience_type}
Stakeholder Level: {stakeholder_level}
Geography: {geography}
Campaign Type: {campaign_type}

Care: {care}
Fairness: {fairness}
Authority: {authority}
Loyalty: {loyalty}
Purity: {purity}

Behavioural Segment: {segment}

Reform Orientation:
{reform}

Risk Profile:
{risk}

Advocacy Lever:
{lever}

Campaign Strategy Plan:
{strategy_plan}

Advocacy Strategy:
{strategy}
"""

        pdf.multi_cell(0,8,report)
        pdf.output("baamt_report.pdf")

        with open("baamt_report.pdf","rb") as f:
            st.download_button("Download PDF",f,"baamt_report.pdf")
