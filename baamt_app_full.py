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
These selections help contextualize the messaging strategy produced by the tool.

• **Audience Type** identifies the primary group you are trying to influence.  
• **Geography** reflects the policy and cultural environment within which advocacy will occur.  
• **Stakeholder Type** indicates the social actors who are most relevant to the campaign.  
• **Campaign Type** clarifies whether the objective is behavioural change, policy reform, or awareness.

These inputs help ensure that the final advocacy strategy is grounded in the realities of the target context.
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
# Explanations
# -------------------------

audience_explanations = {
"General Public":"The general public includes citizens and consumers whose everyday choices, purchasing behaviour, and social attitudes collectively shape market demand and political priorities.",
"Policy Makers":"Policy makers include legislators, regulators, and government officials who design and implement laws, regulations, and public policy frameworks.",
"Professionals":"Professionals include experts, industry practitioners, researchers, and specialists whose institutional decisions influence organizational practices.",
"Youth":"Youth audiences are often early adopters of new social values and cultural norms, making them influential in shaping long-term behavioural trends."
}

geography_explanations = {
"India":"Advocacy in India often operates within a complex federal governance structure, diverse cultural contexts, and rapidly evolving regulatory frameworks.",
"Global":"Global campaigns must resonate across different cultures and legal systems, often emphasizing universal ethical principles.",
"Europe":"European advocacy environments often emphasize precautionary regulation, environmental protection, and institutional governance frameworks.",
"USA":"Messaging in the United States often resonates when framed around innovation, economic incentives, and individual choice."
}

stakeholder_explanations = {
"General Public":"The broader population whose attitudes influence democratic legitimacy and market demand.",
"Community Leaders":"Influential actors such as educators, local organizers, religious leaders, and public intellectuals.",
"Organizations":"Formal institutions such as companies, NGOs, advocacy groups, and government bodies."
}

campaign_explanations = {
"Behaviour Change":"Campaigns aimed at shifting everyday behaviours, habits, or consumer choices.",
"Policy Advocacy":"Campaigns designed to influence legislation, regulation, or institutional decision-making.",
"Awareness Campaign":"Initiatives focused on raising public understanding and visibility of an issue."
}

# -------------------------
# Theoretical Framework
# -------------------------

st.header("Theoretical Framework")

framework = (
"BAAMT draws on Moral Foundations Theory, a framework in moral psychology which "
"suggests that human ethical reasoning is shaped by several intuitive moral dimensions. "
"These include care and harm, fairness and justice, loyalty and group belonging, "
"respect for authority, and concerns related to purity and moral integrity. "
"Different audiences emphasize these foundations to varying degrees. "
"By identifying which moral intuitions are most salient for a particular audience, "
"advocates can design messages that resonate more strongly with existing values."
)

st.write(framework)

# -------------------------
# Questionnaire Instructions
# -------------------------

st.markdown("""
### Behavioural Questionnaire

Please rate the following statements using the sliders below.  
Your responses help estimate which moral foundations are most influential for the selected audience.

Scores range from **1 (Strongly Disagree)** to **5 (Strongly Agree)**.
""")

# -------------------------
# Behavioural Questions
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
# Interpretation
# -------------------------

segment = (
"This audience demonstrates a mixed moral profile. Messaging strategies should therefore "
"integrate multiple ethical frames and emphasize both compassion and fairness."
)

risk = (
"This audience demonstrates moderate sensitivity to social risk. Messages should emphasize "
"practical improvements rather than highly confrontational moral framing."
)

trust = (
"Institutional trust is variable for this audience. Advocacy messages should therefore "
"emphasize transparency, evidence, and successful precedents."
)

strategy = (
"Effective campaigns should combine storytelling, credible evidence, and culturally "
"relevant examples to create persuasive narratives."
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

    # -------------------------
    # Full Report Summary
    # -------------------------

    st.header("Full Report Summary")

    st.write(
    "The BAAMT assessment suggests that advocacy strategies for this audience should "
    "integrate moral appeals related to compassion, fairness, and practical outcomes. "
    "Messages that highlight real-world benefits and credible evidence are likely to "
    "generate stronger engagement."
    )

    # -------------------------
    # Downloadable Report
    # -------------------------

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
