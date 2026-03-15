import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("BAAMT – Behavioural Advocacy and Messaging Tool")

st.write(
"BAAMT helps advocacy organizations design messaging strategies based on "
"the moral values, trust orientation, and risk sensitivities of their target audiences."
)

# -------------------------
# Audience Inputs
# -------------------------

st.header("Audience Information")

audience = st.selectbox("Audience Type", [
"General Public","Policy Makers","Professionals","Youth"
])

geography = st.selectbox("Geography", [
"India","Global","Europe","USA"
])

stakeholder = st.selectbox("Stakeholder Type", [
"General Public","Community Leaders","Organizations"
])

campaign = st.selectbox("Campaign Type", [
"Behaviour Change","Policy Advocacy","Awareness Campaign"
])

# -------------------------
# Theoretical Framework
# -------------------------

st.header("Theoretical Framework")

framework = (
"BAAMT is grounded in Moral Foundations Theory, a framework in moral psychology "
"which proposes that human moral reasoning is influenced by five key domains: "
"Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, and "
"Purity/Degradation. Different audiences emphasize these foundations differently. "
"By identifying which moral values are most salient for a target audience, "
"advocacy organizations can craft messages that resonate with existing moral "
"intuitions rather than relying solely on abstract arguments."
)

st.write(framework)

# -------------------------
# Behavioural Questions
# -------------------------

st.header("Behavioural Assessment")

questions = {
"Care":"Preventing suffering should be a top priority in public policy.",
"Fairness":"Fair treatment matters even if it requires economic trade-offs.",
"Authority":"Society functions best when people respect authority.",
"Loyalty":"Loyalty to one's community should guide decision-making.",
"Purity":"Purity and moral cleanliness are important social values."
}

scores = {}

for key,q in questions.items():
    scores[key] = st.slider(q,1,5,3)

# -------------------------
# Radar Chart
# -------------------------

labels=list(scores.keys())
values=list(scores.values())
values+=values[:1]

angles=np.linspace(0,2*np.pi,len(labels),endpoint=False)
angles=np.concatenate((angles,[angles[0]]))

fig,ax=plt.subplots(figsize=(5,5),subplot_kw=dict(polar=True))
ax.plot(angles,values)
ax.fill(angles,values,alpha=0.2)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

st.pyplot(fig)

# -------------------------
# Interpretation
# -------------------------

segment = (
"This audience demonstrates a mixed moral profile. Messaging strategies "
"should therefore combine compassion-based appeals with fairness narratives "
"and concrete examples that illustrate real-world consequences."
)

strategy = (
"Effective campaigns for this audience should integrate storytelling, "
"credible evidence, and culturally relevant examples. Messages that "
"highlight practical outcomes and shared benefits are more likely to "
"generate engagement."
)

risk = (
"This audience demonstrates moderate sensitivity to social and moral risk. "
"Advocacy messaging should focus on pragmatic improvements rather than "
"framing issues in highly confrontational moral terms."
)

trust = (
"Institutional trust among this audience is variable. Messages should "
"therefore emphasize transparency, credible data sources, and examples "
"of successful policy implementation."
)

# -------------------------
# Generate Report
# -------------------------

if st.button("Generate Report"):

    st.header("Audience Profile")

    st.write("Audience:", audience)
    st.write("Geography:", geography)
    st.write("Stakeholder:", stakeholder)
    st.write("Campaign Type:", campaign)

    st.subheader("Behavioural Segment")
    st.write(segment)

    st.subheader("Risk Sensitivity")
    st.write(risk)

    st.subheader("Institutional Trust")
    st.write(trust)

    st.subheader("Advocacy Strategy")
    st.write(strategy)

    # Create downloadable report
    report = f"""
BAAMT Advocacy Report

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign Type: {campaign}

THEORETICAL FRAMEWORK
{framework}

BEHAVIOURAL SEGMENT
{segment}

RISK SENSITIVITY
{risk}

INSTITUTIONAL TRUST
{trust}

ADVOCACY STRATEGY
{strategy}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="baamt_report.txt",
        mime="text/plain"
    )
