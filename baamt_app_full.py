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
Advocacy campaigns often fail because they assume all audiences respond to the same moral arguments.

BAAMT helps advocacy organisations identify the **moral values most salient to a target audience**, and suggests **strategic messaging frames** based on behavioural science research.
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

st.markdown("Rate from **1 (Strongly Disagree)** to **5 (Strongly Agree)**.")

q1 = st.slider("Preventing suffering should be a top priority in public policy.",1,5)
q2 = st.slider("Fair treatment matters even if it requires economic trade-offs.",1,5)
q3 = st.slider("Society functions best when people respect authority.",1,5)
q4 = st.slider("Loyalty to one's community should guide decisions.",1,5)
q5 = st.slider("Purity and moral cleanliness are important values.",1,5)

q6 = st.slider("Avoiding harm to vulnerable beings is an ethical responsibility.",1,5)
q7 = st.slider("Rules and laws should be followed even when inconvenient.",1,5)
q8 = st.slider("Fairness should guide economic systems.",1,5)
q9 = st.slider("Communities should protect their traditions.",1,5)
q10 = st.slider("Certain practices are morally wrong regardless of consequences.",1,5)

# ---------------------------------------------------
# SCORES
# ---------------------------------------------------

care = (q1+q6)/2
fairness = (q2+q8)/2
authority = (q3+q7)/2
loyalty = (q4+q9)/2
purity = (q5+q10)/2

# ---------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------

generate = st.button("Generate Behavioural Strategy")

if generate:

    st.header("Audience Moral Profile")

    st.write("Care/Harm:",round(care,2))
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

    st.markdown("---")

# ---------------------------------------------------
# STRATEGY GENERATION
# ---------------------------------------------------

    st.header("Messaging Strategy")

    dominant=max(care,fairness,authority,loyalty,purity)

    strategy=""

    if dominant==care:

        strategy="""
Focus messaging on **compassion and harm reduction**.

Narratives that highlight the suffering of animals or vulnerable beings are likely to resonate strongly with this audience. Campaigns should use emotional storytelling, visual narratives, and moral appeals centered on empathy and protection.

Example message:
Millions of animals suffer in modern food systems every year. By supporting humane alternatives we can reduce immense suffering and create a kinder world.
"""

    elif dominant==fairness:

        strategy="""
Frame the issue as **justice and systemic fairness**.

Campaign messaging should highlight inequalities, unfair subsidies, or structural injustices within food systems.

Example message:
Public resources should support ethical and sustainable food systems. Redirecting subsidies toward plant-based innovation can create a fairer future for people, animals, and the planet.
"""

    elif dominant==authority:

        strategy="""
Frame the issue around **institutional responsibility and governance**.

Audiences with strong authority orientation respond to messages emphasizing regulation, oversight, and responsible leadership.

Example message:
Strong regulatory standards are essential to ensure responsible treatment of animals and protect public health.
"""

    elif dominant==loyalty:

        strategy="""
Appeal to **community identity and shared values**.

Campaigns should emphasize protecting national traditions, communities, and future generations.

Example message:
Building sustainable food systems is part of protecting our communities and ensuring a healthy future for the next generation.
"""

    else:

        strategy="""
Frame the issue around **moral integrity and purity**.

Messaging should emphasize ethical consumption, natural living, and avoiding harmful practices.

Example message:
Choosing plant-based foods is a cleaner and more ethical way to live in harmony with nature.
"""

    st.write(strategy)

# ---------------------------------------------------
# GEOGRAPHY ADJUSTMENT
# ---------------------------------------------------

    if geography=="India":

        st.subheader("India-specific framing")

        st.write("""
Messaging in India can also highlight:

• food system sustainability  
• farmer transition opportunities  
• public health and antibiotic resistance  
• cultural traditions of plant-based diets
""")

# ---------------------------------------------------
# AUDIENCE ADJUSTMENT
# ---------------------------------------------------

    if audience_type=="Policy Makers":

        st.subheader("Policy Audience Strategy")

        st.write("""
Policy audiences respond best to:

• regulatory framing  
• economic impact analysis  
• public health arguments  
• institutional accountability
""")

    if audience_type=="Corporate Stakeholders":

        st.subheader("Corporate Engagement Strategy")

        st.write("""
Corporate messaging should emphasize:

• market opportunities  
• innovation leadership  
• ESG and sustainability commitments  
• reputational benefits
""")

# ---------------------------------------------------
# PDF REPORT
# ---------------------------------------------------

    if st.button("Download Strategy Report"):

        pdf=FPDF()
        pdf.add_page()

        pdf.set_font("Arial",size=12)

        report=f"""
BAAMT Behavioural Strategy Report

Audience: {audience_type}
Geography: {geography}
Campaign Type: {campaign_type}

Moral Scores
Care: {care}
Fairness: {fairness}
Authority: {authority}
Loyalty: {loyalty}
Purity: {purity}

Behavioural Segment:
{segment}

Recommended Strategy:
{strategy}
"""

        pdf.multi_cell(0,8,report)

        pdf.output("baamt_report.pdf")

        with open("baamt_report.pdf","rb") as f:
            st.download_button(
                "Download PDF",
                f,
                "baamt_report.pdf"
            )
