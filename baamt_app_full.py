import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import textwrap

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")

st.write("""
BAAMT helps advocacy organisations design more effective communication strategies by
analysing the moral values and behavioural orientations of their target audiences.
The tool translates insights from behavioural science into practical guidance for
advocacy campaigns, policy engagement, and public messaging.
""")

st.markdown("---")

# THEORY SECTION

st.header("Theoretical Background")

st.write("""
BAAMT draws on insights from Moral Foundations Theory, a framework in moral
psychology that suggests people make moral judgments using several intuitive
moral foundations rather than purely rational analysis.

The most widely studied moral foundations include:

• Care – concern for suffering and compassion  
• Fairness – concern for justice and equality  
• Authority – respect for rules and institutions  
• Loyalty – commitment to one's group or community  
• Purity – beliefs about moral or cultural integrity  

Different audiences prioritise these moral concerns in different ways. When
advocacy messages align with the values that matter most to an audience, they
are far more likely to be persuasive and memorable.

BAAMT therefore measures how strongly an audience responds to these moral
dimensions and then translates that information into practical messaging
guidance and campaign strategy recommendations.
""")

st.markdown("---")

# INSTRUCTIONS

st.write("""
### How to Use This Tool

First select the audience and campaign context for which you are developing an
advocacy strategy. Then answer the behavioural assessment questions below.

Once the responses are submitted, BAAMT will analyse the moral profile of the
audience and generate a structured advocacy report that includes behavioural
insights, messaging guidance, and a suggested campaign strategy.
""")

# AUDIENCE CONTEXT

st.header("Audience Context")

audience = st.selectbox(
"Target Audience",
[
"General Public",
"Students and Young People",
"Policy Makers",
"Industry Stakeholders",
"Civil Society Organisations"
]
)

geography = st.selectbox(
"Geographic Context",
[
"India",
"Global",
"Europe",
"North America",
"Southeast Asia"
]
)

stakeholder = st.selectbox(
"Primary Stakeholder Engagement",
[
"Government Institutions",
"Corporate Actors",
"Civil Society",
"Consumers"
]
)

campaign = st.selectbox(
"Campaign Objective",
[
"Behaviour Change",
"Policy Reform",
"Corporate Engagement",
"Public Awareness"
]
)

st.markdown("---")

# MORAL QUESTIONNAIRE

st.header("Behavioural Assessment")

st.write("Please rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree).")

care1 = st.slider("Preventing suffering should be a central priority in public policy decisions.",1,5,3)
care2 = st.slider("Society has a moral responsibility to reduce harm to vulnerable beings.",1,5,3)

fair1 = st.slider("Economic systems should prioritise fairness even when this involves financial trade-offs.",1,5,3)
fair2 = st.slider("Markets should operate in ways that protect fairness and justice.",1,5,3)

auth1 = st.slider("Societies function best when people respect laws and institutions.",1,5,3)
auth2 = st.slider("Government institutions should play an important role in regulating social problems.",1,5,3)

loyal1 = st.slider("Communities should protect their cultural traditions and shared values.",1,5,3)
loyal2 = st.slider("People should prioritise the well-being of their community when making decisions.",1,5,3)

pure1 = st.slider("Certain practices are morally wrong even if they bring economic benefits.",1,5,3)
pure2 = st.slider("Maintaining moral integrity in society is extremely important.",1,5,3)

st.markdown("---")

if st.button("Generate Advocacy Report"):

    care=(care1+care2)/2
    fairness=(fair1+fair2)/2
    authority=(auth1+auth2)/2
    loyalty=(loyal1+loyal2)/2
    purity=(pure1+pure2)/2

    scores={
    "Care":care,
    "Fairness":fairness,
    "Authority":authority,
    "Loyalty":loyalty,
    "Purity":purity
    }

    st.header("1️⃣ Audience Moral Profile")

    for k,v in scores.items():
        st.write(f"{k}: {round(v,2)}")

    st.header("2️⃣ Moral Foundations Radar Chart")

    labels=list(scores.keys())
    values=list(scores.values())
    values+=values[:1]

    angles=[n/float(len(labels))*2*3.14159 for n in range(len(labels))]
    angles+=angles[:1]

    fig=plt.figure()
    ax=fig.add_subplot(111,polar=True)

    ax.plot(angles,values)
    ax.fill(angles,values,alpha=0.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    st.pyplot(fig)

    # Behavioural Segment

    st.header("3️⃣ Behavioural Segment")

    if care>4:
        segment="""
This audience shows a strong compassion orientation. People in this group are
particularly responsive to messages that highlight suffering, harm, and the
ethical responsibility to protect vulnerable beings.
"""
    elif authority>4:
        segment="""
This audience places strong importance on institutions and governance.
Advocacy campaigns should emphasise credible research, regulatory reform,
and responsible institutional action.
"""
    elif loyalty>4:
        segment="""
This audience is strongly influenced by community identity and shared values.
Advocacy messaging should emphasise collective responsibility and community
leadership.
"""
    else:
        segment="""
This audience shows a balanced moral profile without a single dominant value.
Advocacy campaigns should combine compassion, fairness arguments,
and institutional responsibility.
"""

    st.write(segment)

    # Reform Orientation

    st.header("4️⃣ Reform Orientation")

    if authority>3.5:
        reform="""
This audience tends to trust institutions and may prefer reforms that occur
through structured policy processes.
"""
    else:
        reform="""
This audience may be more open to stronger critiques of existing systems
and ambitious reforms.
"""

    st.write(reform)

    # Risk

    st.header("5️⃣ Risk Sensitivity Profile")

    if purity>4:
        risk="This audience shows strong sensitivity to moral or cultural risk."
    else:
        risk="This audience shows relatively low sensitivity to moral risk."

    st.write(risk)

    # Trust

    st.header("6️⃣ Institutional Trust Orientation")

    if authority+loyalty>7:
        trust="This audience appears to have relatively high trust in institutions."
    else:
        trust="This audience shows a more cautious attitude toward institutions."

    st.write(trust)

    # Lever

    st.header("7️⃣ Primary Advocacy Lever")

    if care>4:
        lever="Compassion and harm-reduction messaging."
    elif fairness>4:
        lever="Justice and fairness framing."
    elif authority>4:
        lever="Institutional responsibility framing."
    else:
        lever="Social norm change messaging."

    st.write(lever)

    # Geography

    st.header("8️⃣ Geographic Messaging Adjustment")

    if geography=="India":
        geo="Messaging should acknowledge cultural diversity and community leadership."
    elif geography=="Europe":
        geo="Messaging can emphasise regulatory standards and welfare norms."
    else:
        geo="Messaging should focus on universal ethical principles."

    st.write(geo)

    # Strategy

    st.header("9️⃣ Campaign Strategy Plan")

    strategy="""
An effective advocacy campaign should combine public education, credible
research evidence, and engagement with institutional stakeholders.
"""

    st.write(strategy)

    # Brief

    st.header("🔟 Full Advocacy Strategy Brief")

    brief=f"""
Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign Objective: {campaign}

The behavioural analysis suggests this audience can be engaged through
{lever.lower()} combined with clear evidence and practical solutions.
"""

    st.write(brief)

    # SUCCESS MESSAGE (UX IMPROVEMENT)

    st.success("Your advocacy report has been generated successfully. You can now download the full report below.")

    # PDF GENERATION

    report=f"""
BAAMT Advocacy Strategy Report

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}

Care: {care}
Fairness: {fairness}
Authority: {authority}
Loyalty: {loyalty}
Purity: {purity}

Behavioural Segment
{segment}

Reform Orientation
{reform}

Risk Sensitivity
{risk}

Institutional Trust
{trust}

Primary Advocacy Lever
{lever}

Geographic Messaging
{geo}

Campaign Strategy
{strategy}

Advocacy Strategy Brief
{brief}
"""

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=11)

    for line in textwrap.wrap(report,90):
        pdf.cell(0,8,line,ln=True)

    pdf_bytes = bytes(pdf.output(dest="S"))

    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )
