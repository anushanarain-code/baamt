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
"General Public":"This audience consists of citizens and consumers whose attitudes and everyday behaviours influence social norms and market demand.",
"Policy Makers":"This audience includes legislators, regulators, and government officials responsible for designing and implementing policy frameworks.",
"Professionals":"This group includes industry experts, technical specialists, and professionals whose practices influence institutional behaviour.",
"Youth":"Young audiences often shape emerging cultural values and future policy directions."
}

geography_explanations = {
"India":"Messaging should account for India's diverse cultural contexts, federal governance structure, and evolving public policy environment.",
"Global":"Global audiences require messaging that emphasizes universal ethical principles and cross-cultural relevance.",
"Europe":"European contexts often emphasize regulatory frameworks, sustainability goals, and precautionary policy approaches.",
"USA":"Messaging in the United States often resonates when framed around individual responsibility, innovation, and economic incentives."
}

stakeholder_explanations = {
"General Public":"Members of the broader population whose attitudes and behaviours shape social acceptance of policies or innovations.",
"Community Leaders":"Influential local actors who shape opinion within communities, including educators, activists, and religious leaders.",
"Organizations":"Institutions such as companies, NGOs, and public agencies that implement or influence large-scale change."
}

campaign_explanations = {
"Behaviour Change":"Campaigns focused on shifting everyday practices, habits, or consumer choices.",
"Policy Advocacy":"Campaigns designed to influence legislation, regulations, or institutional decision-making.",
"Awareness Campaign":"Efforts aimed at increasing public understanding and visibility of an issue."
}

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
"should combine compassion-based appeals with fairness narratives and "
"clear examples that illustrate real-world consequences."
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

    # Report text
    report = f"""
# BAAMT Advocacy Report

## Audience
**{audience}**

{audience_explanations[audience]}

## Geography
**{geography}**

{geography_explanations[geography]}

## Stakeholder
**{stakeholder}**

{stakeholder_explanations[stakeholder]}

## Campaign Type
**{campaign}**

{campaign_explanations[campaign]}

---

## Theoretical Framework
{framework}

---

## Behavioural Segment
{segment}

---

## Risk Sensitivity
{risk}

---

## Institutional Trust
{trust}

---

## Advocacy Strategy
{strategy}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="baamt_report.md",
        mime="text/markdown"
    )
