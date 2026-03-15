import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="BAAMT",
    page_icon="🧠",
    layout="centered"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")

st.markdown("""
BAAMT is a behavioural strategy tool designed to help advocacy organisations
design more effective campaigns by aligning messaging with the **moral values,
risk perceptions, and institutional expectations of their target audiences**.

The framework draws on research from **Moral Foundations Theory**, behavioural
public policy, and decision science. These approaches suggest that people do
not respond to advocacy messages purely through facts or rational arguments,
but through deeply held moral intuitions, social identities, and perceptions
of risk and institutional legitimacy.

By identifying the moral foundations most salient to a target audience, BAAMT
generates a **behavioural profile and advocacy strategy brief** that can help
campaigners design messages that resonate with the audiences they seek to
influence.
""")

st.markdown("---")

# ---------------------------------------------------
# AUDIENCE INPUT
# ---------------------------------------------------

st.header("Audience Information")

audience_type = st.selectbox(
    "Target Audience",
    [
        "General Public",
        "Policy Makers",
        "Corporate Stakeholders",
        "Students",
        "Civil Society"
    ]
)

geography = st.selectbox(
    "Geography",
    [
        "India",
        "Global",
        "Other"
    ]
)

campaign_type = st.selectbox(
    "Campaign Type",
    [
        "Behaviour Change",
        "Policy Advocacy",
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
q3 = st.slider("Society functions best when people respect authority and institutions.",1,5)
q4 = st.slider("Loyalty to one's community should guide important decisions.",1,5)
q5 = st.slider("Purity and moral cleanliness are important social values.",1,5)

q6 = st.slider("Avoiding harm to vulnerable beings is an ethical responsibility.",1,5)
q7 = st.slider("Rules and laws should be followed even when inconvenient.",1,5)
q8 = st.slider("Fairness should guide economic systems.",1,5)
q9 = st.slider("Communities should protect their traditions.",1,5)
q10 = st.slider("Certain practices are morally wrong regardless of consequences.",1,5)

# ---------------------------------------------------
# SCORE CALCULATION
# ---------------------------------------------------

care = (q1+q6)/2
fairness = (q2+q8)/2
authority = (q3+q7)/2
loyalty = (q4+q9)/2
purity = (q5+q10)/2

generate = st.button("Generate Advocacy Strategy")

# ---------------------------------------------------
# RESULTS
# ---------------------------------------------------

if generate:

    st.header("Audience Moral Profile")

    st.write("Care / Harm:",round(care,2))
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
# BEHAVIOURAL SEGMENT
# ---------------------------------------------------

    if care>4 and fairness>4:
        segment="Compassion-driven reform audience"

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

    if fairness+care > authority+loyalty:
        reform_orientation="""
This audience demonstrates a **reform-oriented moral profile**. Individuals
with this profile are more receptive to arguments about systemic change,
institutional reform, and correcting injustices within social systems.
Advocacy efforts can therefore emphasize the possibility of improving
existing institutions rather than simply preserving the status quo.
"""
    else:
        reform_orientation="""
This audience demonstrates a **stability-oriented moral profile**. Individuals
with this orientation tend to prioritise social order, institutional legitimacy,
and the preservation of traditions. Advocacy messages directed toward such
audiences should therefore avoid framing change as disruptive, and instead
emphasise continuity, responsible stewardship, and gradual improvement.
"""

    st.subheader("Reform Orientation")
    st.write(reform_orientation)

# ---------------------------------------------------
# RISK PROFILE
# ---------------------------------------------------

    if authority+purity > fairness+care:
        risk_profile="""
The behavioural profile suggests a **risk-sensitive audience**. Such audiences
often respond strongly to perceived threats to social order, public health,
or moral integrity. Advocacy messages that highlight the risks associated with
current practices—such as environmental degradation, public health threats,
or institutional failure—are likely to resonate.
"""
    else:
        risk_profile="""
The behavioural profile suggests an audience that is **less risk-averse and
more opportunity oriented**. Messaging strategies can therefore emphasise
innovation, positive change, and the potential benefits of reform rather than
focusing primarily on risks or threats.
"""

    st.subheader("Risk Profile")
    st.write(risk_profile)

# ---------------------------------------------------
# ADVOCACY LEVER
# ---------------------------------------------------

    if audience_type=="Policy Makers":
        advocacy_lever="Regulatory reform and institutional accountability"

    elif audience_type=="Corporate Stakeholders":
        advocacy_lever="Market incentives and corporate leadership"

    else:
        advocacy_lever="Public awareness and social norm change"

    st.subheader("Primary Advocacy Lever")
    st.write(advocacy_lever)

# ---------------------------------------------------
# CAMPAIGN STRATEGY PLAN
# ---------------------------------------------------

    strategy_plan=f"""
A campaign directed toward **{audience_type}** audiences in **{geography}**
should combine moral framing with institutional credibility.

The campaign should prioritise the advocacy lever of **{advocacy_lever}**
while ensuring that communication strategies reflect the dominant
moral concerns identified in the behavioural assessment.

Campaign messaging should therefore balance **evidence-based policy
arguments with narratives that resonate emotionally and morally**
with the audience being targeted.
"""

    st.subheader("Campaign Strategy Plan")
    st.write(strategy_plan)

# ---------------------------------------------------
# ADVOCACY STRATEGY
# ---------------------------------------------------

    strategy=f"""
Based on the behavioural assessment, the recommended advocacy strategy
is to design messaging that aligns with the audience's dominant moral
foundations while maintaining credibility within the institutional
context in which advocacy is taking place.

Campaign narratives should combine **moral framing, evidence-based
arguments, and credible institutional signals** in order to influence
decision making.

Advocacy communications should therefore move beyond purely informational
approaches and instead seek to shape how audiences **interpret the ethical
and social meaning of the issue being addressed**.
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
Geography: {geography}
Campaign Type: {campaign_type}

Moral Profile
Care: {care}
Fairness: {fairness}
Authority: {authority}
Loyalty: {loyalty}
Purity: {purity}

Behavioural Segment:
{segment}

Reform Orientation:
{reform_orientation}

Risk Profile:
{risk_profile}

Advocacy Lever:
{advocacy_lever}

Campaign Strategy Plan:
{strategy_plan}

Advocacy Strategy:
{strategy}
"""

        pdf.multi_cell(0,8,report)
        pdf.output("baamt_strategy_report.pdf")

        with open("baamt_strategy_report.pdf","rb") as f:
            st.download_button("Download PDF",f,"baamt_strategy_report.pdf")
