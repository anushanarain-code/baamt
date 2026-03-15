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

• Audience Type identifies the group you want to influence  
• Geography reflects the policy and cultural environment  
• Stakeholder Type identifies actors central to the campaign  
• Campaign Type clarifies the advocacy objective  
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

"General Public":
"When the general public is the primary audience, advocacy messages should prioritize clarity and relatable examples.",

"Policy Makers":
"Policy makers respond best to evidence-based arguments, regulatory feasibility, and policy comparisons.",

"Professionals":
"Professional audiences respond strongly to credible research, technical evidence, and best practices.",

"Youth":
"Youth audiences often respond strongly to future-oriented messaging and values-driven narratives."
}

geography_explanations = {

"India":
"In India, advocacy messaging often resonates when framed around social welfare, development, and community wellbeing.",

"Global":
"Global campaigns often resonate when framed around universal ethical values and global cooperation.",

"Europe":
"In Europe, sustainability and environmental responsibility often strengthen advocacy messaging.",

"USA":
"In the United States, advocacy messaging often gains traction when framed around innovation and consumer choice."
}

stakeholder_explanations = {

"General Public":
"The broader population whose attitudes influence democratic legitimacy and market demand.",

"Community Leaders":
"Community leaders can serve as influential intermediaries in shaping social attitudes.",

"Organizations":
"Organizations can influence policy, institutional practice, and industry standards."
}

campaign_explanations = {

"Behaviour Change":
"Behaviour change campaigns aim to shift everyday choices and habits through persuasive messaging.",

"Policy Advocacy":
"Policy advocacy campaigns focus on influencing laws, regulations, and institutional decisions.",

"Awareness Campaign":
"Awareness campaigns seek to increase public understanding and issue visibility."
}

# -------------------------
# Theoretical Framework
# -------------------------

st.header("Theoretical Framework")

framework = (
"BAAMT draws on Moral Foundations Theory, which proposes that human moral reasoning "
"is shaped by several intuitive ethical dimensions including care, fairness, loyalty, "
"authority, and purity. Understanding which moral foundations dominate within an "
"audience can help advocates design messages that resonate with existing moral intuitions."
)

st.write(framework)

# -------------------------
# Questionnaire
# -------------------------

st.markdown("""
### Behavioural Questionnaire

Rate each statement from **1 (Strongly Disagree)** to **5 (Strongly Agree)**.
""")

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
# Moral Foundations Analysis
# -------------------------

dominant = max(scores, key=scores.get)

foundation_analysis = {
"Care":
"This audience places strong emphasis on harm reduction and compassion. Advocacy messages highlighting suffering reduction and protection of vulnerable groups are likely to resonate strongly.",

"Fairness":
"This audience appears strongly motivated by fairness and justice concerns. Messages emphasizing equality and ethical responsibility are likely to resonate.",

"Authority":
"This audience places importance on order, leadership, and institutional stability. Messages emphasizing responsibility and structured solutions may be effective.",

"Loyalty":
"This audience appears strongly motivated by group loyalty and social cohesion. Messaging that highlights community identity may resonate.",

"Purity":
"This audience demonstrates sensitivity to moral and symbolic purity concerns. Messaging that highlights ethical integrity may resonate."
}

# -------------------------
# Dynamic Behavioural Segment
# -------------------------

care = scores["Care"]
fairness = scores["Fairness"]
authority = scores["Authority"]
loyalty = scores["Loyalty"]

if care + fairness >= 8:

    segment = (
    "This audience appears strongly motivated by compassion and fairness concerns."
    )

elif authority + loyalty >= 8:

    segment = (
    "This audience appears more responsive to tradition and social stability."
    )

else:

    segment = (
    "This audience demonstrates a balanced moral profile."
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

    st.header("Moral Foundations Profile")

    for k,v in scores.items():
        st.write(f"{k}: {v}")

    st.write(foundation_analysis[dominant])

    st.header("Behavioural Segment")

    st.write(segment)

    st.header("Full Report Summary")

    st.write(
    "This BAAMT assessment suggests that advocacy strategies should align messaging "
    "with the dominant moral intuitions of the audience while highlighting practical benefits."
    )

    report = f"""
BAAMT Advocacy Report

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign: {campaign}

Dominant Moral Foundation: {dominant}

Interpretation:
{foundation_analysis[dominant]}

Behavioural Segment:
{segment}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="baamt_report.txt",
        mime="text/plain"
    )
