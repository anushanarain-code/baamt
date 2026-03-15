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
# Audience Instructions
# -------------------------

st.markdown("""
### Audience Context

Please select the audience context for which you are designing an advocacy or policy campaign.

• **Audience Type** identifies the group you want to influence  
• **Geography** reflects the policy and cultural environment  
• **Stakeholder Type** identifies actors central to the campaign  
• **Campaign Type** clarifies the advocacy objective  

These inputs help contextualize the messaging recommendations produced by BAAMT.
""")

# -------------------------
# Audience Inputs
# -------------------------

st.header("Audience Information")

audience = st.selectbox(
"Audience Type",
["General Public","Policy Makers","Professionals","Youth"]
)

geography = st.selectbox(
"Geography",
["India","Global","Europe","USA"]
)

stakeholder = st.selectbox(
"Stakeholder Type",
["General Public","Community Leaders","Organizations"]
)

campaign = st.selectbox(
"Campaign Type",
["Behaviour Change","Policy Advocacy","Awareness Campaign"]
)

# -------------------------
# Strategic Explanations
# -------------------------

audience_explanations = {

"General Public":
"When the general public is the primary audience, advocacy messages should prioritize clarity, emotional resonance, and relatable everyday examples. Campaigns are often most effective when they highlight tangible benefits, social norms, and visible impacts on daily life.",

"Policy Makers":
"When policy makers are the target audience, messaging should emphasize regulatory feasibility, institutional benefits, and credible evidence. Policy briefs, economic implications, and examples of successful regulatory models are particularly persuasive.",

"Professionals":
"Professional audiences respond strongly to evidence-based messaging and technical credibility. Campaigns should emphasize best practices, research findings, and professional standards.",

"Youth":
"Youth audiences often respond strongly to future-oriented messaging and values-driven narratives. Campaigns that emphasize long-term social impact and opportunities for participation can create stronger engagement."
}

geography_explanations = {

"India":
"In India, advocacy messaging often benefits from emphasizing public welfare, development outcomes, and community wellbeing.",

"Global":
"Global campaigns should emphasize universal ethical values and shared global challenges.",

"Europe":
"In Europe, advocacy messages often resonate when framed around sustainability and regulatory responsibility.",

"USA":
"In the United States, advocacy campaigns often gain traction when framed around innovation, market solutions, and consumer choice."
}

stakeholder_explanations = {

"General Public":
"When the broader public is a key stakeholder group, campaigns should prioritize awareness initiatives, storytelling, and social norm messaging.",

"Community Leaders":
"Community leaders can act as influential intermediaries between campaigns and local populations.",

"Organizations":
"When organizations are central stakeholders, advocacy should emphasize institutional incentives and practical implementation pathways."
}

campaign_explanations = {

"Behaviour Change":
"Behaviour change campaigns work best when they combine awareness with clear and actionable steps that audiences can easily adopt.",

"Policy Advocacy":
"Policy advocacy campaigns should focus on evidence, coalition building, and demonstrating the feasibility of policy reform.",

"Awareness Campaign":
"Awareness campaigns aim to increase visibility and understanding of an issue through compelling narratives and accessible information."
}

# -------------------------
# Theoretical Framework
# -------------------------

st.header("Theoretical Framework")

framework = (
"BAAMT draws on Moral Foundations Theory, which suggests that human moral reasoning "
"is influenced by several intuitive ethical dimensions including care, fairness, loyalty, "
"authority, and purity. Different audiences prioritize these values differently. "
"Understanding these patterns can help advocates design messages that resonate with "
"existing moral intuitions rather than relying solely on abstract arguments."
)

st.write(framework)

# -------------------------
# Questionnaire Instructions
# -------------------------

st.markdown("""
### Behavioural Questionnaire

Please rate the following statements.

Scores range from **1 (Strongly Disagree)** to **5 (Strongly Agree)**.

These responses help estimate which moral foundations are most influential for the selected audience.
""")

# -------------------------
# Questions
# -------------------------

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
# Dynamic Behavioural Segmentation
# -------------------------

care = scores["Care"]
fairness = scores["Fairness"]
authority = scores["Authority"]
loyalty = scores["Loyalty"]
purity = scores["Purity"]

if care + fairness >= 8:

    segment = (
    "This audience appears strongly motivated by compassion and fairness concerns. "
    "Advocacy messages that highlight the prevention of suffering, protection of "
    "vulnerable groups, and equitable outcomes are likely to resonate most strongly."
    )

elif authority + loyalty >= 8:

    segment = (
    "This audience appears more responsive to social stability and community cohesion. "
    "Advocacy messages should emphasize responsibility, tradition, and the protection "
    "of shared social values."
    )

else:

    segment = (
    "This audience demonstrates a balanced moral profile. Messaging strategies should "
    "integrate multiple frames combining ethical reasoning with practical real-world benefits."
    )

risk = (
"This audience demonstrates moderate sensitivity to social risk. Messages should emphasize "
"practical improvements rather than highly confrontational moral framing."
)

trust = (
"Institutional trust appears variable for this audience. Advocacy messages should emphasize "
"credibility, transparency, and evidence-based reasoning."
)

strategy = (
"Effective campaigns should combine storytelling, credible evidence, and culturally relevant "
"examples to create persuasive narratives."
)

# -------------------------
# Generate Report
# -------------------------

if st.button("Generate Report"):

    st.header("Audience Profile")

    st.write("Audience:", audience)
    st.write(audience_explanations[audience])

    st.write("Geography:", geography)
    st.write(geography_explanations[geography])

    st.write("Stakeholder:", stakeholder)
    st.write(stakeholder_explanations[stakeholder])

    st.write("Campaign Type:", campaign)
    st.write(campaign_explanations[campaign])

    st.subheader("Behavioural Segment")
    st.write(segment)

    st.subheader("Risk Sensitivity")
    st.write(risk)

    st.subheader("Institutional Trust")
    st.write(trust)

    st.subheader("Advocacy Strategy")
    st.write(strategy)

    st.header("Full Report Summary")

    st.write(
    "Based on the BAAMT assessment, advocacy strategies for this audience should combine "
    "moral framing with clear real-world benefits. Messages that highlight fairness, "
    "compassion, and practical societal improvements are likely to generate stronger engagement."
    )

    report = f"""
# BAAMT Advocacy Report

## Audience
{audience}

{audience_explanations[audience]}

## Geography
{geography}

{geography_explanations[geography]}

## Stakeholder
{stakeholder}

{stakeholder_explanations[stakeholder]}

## Campaign Type
{campaign}

{campaign_explanations[campaign]}

## Theoretical Framework
{framework}

## Behavioural Segment
{segment}

## Risk Sensitivity
{risk}

## Institutional Trust
{trust}

## Advocacy Strategy
{strategy}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="baamt_report.md",
        mime="text/markdown"
    )
