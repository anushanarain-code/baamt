import streamlit as st

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("BAAMT – Behavioural Advocacy and Messaging Tool")

st.write(
"BAAMT is a behavioural analysis tool designed to help advocacy organizations, "
"policy researchers, and social campaigners better understand how different audiences "
"may respond to advocacy messaging. The tool draws on behavioural science and moral "
"psychology to generate strategic insights about advocacy communication."
)

# ---------------------------------------------------
# Audience Context
# ---------------------------------------------------

st.markdown("""
### Audience Context

Select the campaign environment in which you are working.  
These variables help contextualize the behavioural analysis produced by BAAMT.

• **Audience Type** – the primary group you want to influence  
• **Geography** – the regulatory and cultural environment  
• **Stakeholder Type** – actors who influence the issue landscape  
• **Campaign Type** – the type of advocacy intervention
""")

# ---------------------------------------------------
# Inputs
# ---------------------------------------------------

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

# ---------------------------------------------------
# Descriptions
# ---------------------------------------------------

audience_explanations = {

"General Public":
"The general public represents a broad and diverse audience whose attitudes, consumption choices, and voting behaviour collectively influence market dynamics and political priorities. Advocacy campaigns targeting the general public often benefit from accessible messaging, emotional resonance, and clear explanations of the societal consequences of everyday behaviours.",

"Policy Makers":
"Policy makers represent institutional decision-makers who have the authority to shape regulatory frameworks and legislative outcomes. Advocacy efforts directed at this audience tend to be most effective when grounded in credible evidence, policy feasibility, and comparative examples from other jurisdictions.",

"Professionals":
"Professional audiences include scientists, industry actors, regulators, and subject-matter experts whose opinions can influence both public discourse and policy development. Messaging directed toward professional audiences often requires technical credibility, careful use of evidence, and alignment with professional norms.",

"Youth":
"Younger audiences often demonstrate strong engagement with ethical and future-oriented narratives. Advocacy messaging aimed at youth audiences frequently benefits from emphasizing long-term societal impacts, generational responsibility, and collective social change."
}

geography_explanations = {

"India":
"Advocacy efforts in India operate within a complex federal system characterized by diverse cultural contexts, rapidly evolving regulatory frameworks, and strong interactions between public opinion and political institutions.",

"Global":
"Global advocacy campaigns often involve transnational institutions, multinational corporations, and international civil society networks.",

"Europe":
"European policy environments often emphasize sustainability, regulatory accountability, and precautionary approaches to technological and environmental risk.",

"USA":
"The United States advocacy environment often combines strong market dynamics with polarized political debate."
}

stakeholder_explanations = {

"General Public":
"The broader population whose attitudes and behavioural choices influence both democratic legitimacy and economic demand.",

"Community Leaders":
"Community leaders, educators, activists, and public figures can act as influential intermediaries who shape public narratives and help translate complex issues for local audiences.",

"Organizations":
"Organizations such as NGOs, corporations, professional associations, and advocacy groups can influence institutional practices, regulatory debates, and industry standards."
}

campaign_explanations = {

"Behaviour Change":
"Behaviour change campaigns attempt to influence everyday decisions such as consumption choices, lifestyle habits, or social behaviours.",

"Policy Advocacy":
"Policy advocacy campaigns aim to influence legislation, regulatory frameworks, or institutional decisions.",

"Awareness Campaign":
"Awareness campaigns aim to increase visibility and public understanding of an issue."
}

# ---------------------------------------------------
# Theoretical Framework
# ---------------------------------------------------

st.header("Theoretical Framework")

st.write(
"BAAMT draws on insights from Moral Foundations Theory, behavioural economics, and advocacy strategy research. "
"Moral Foundations Theory suggests that individuals interpret political and ethical issues through intuitive "
"moral lenses such as care, fairness, loyalty, authority, and purity. Advocacy campaigns that align their "
"messaging with these underlying moral intuitions are often more persuasive than campaigns that rely solely "
"on factual or technical arguments."
)

# ---------------------------------------------------
# Questionnaire
# ---------------------------------------------------

st.markdown("""
### Behavioural Questionnaire

Rate the following statements from **1 (Strongly Disagree)** to **5 (Strongly Agree)**.
""")

questions = {
"Care":"Reducing suffering should be a major priority when making public decisions.",
"Fairness":"Justice and fairness should guide policy even when they involve economic trade-offs.",
"Authority":"Societies function best when institutions and leadership structures are respected.",
"Loyalty":"Protecting one's community and social group is an important moral obligation.",
"Purity":"Moral integrity and ethical purity are important principles for guiding social behaviour."
}

scores = {}

for key,q in questions.items():
    scores[key] = st.slider(q,1,5,3)

# ---------------------------------------------------
# Moral Analysis
# ---------------------------------------------------

dominant = max(scores, key=scores.get)

foundation_analysis = {

"Care":
"This audience appears strongly motivated by concerns related to harm reduction and compassion. Advocacy messages that highlight the protection of vulnerable populations, the prevention of suffering, and the ethical responsibility to reduce harm are likely to resonate particularly strongly.",

"Fairness":
"This audience appears highly responsive to questions of justice, fairness, and equitable treatment.",

"Authority":
"This audience appears to place substantial weight on institutional stability, social order, and legitimate authority.",

"Loyalty":
"This audience appears strongly motivated by values related to group identity and social solidarity.",

"Purity":
"This audience appears sensitive to symbolic concerns about ethical integrity and moral boundaries."
}

# ---------------------------------------------------
# Strategic Profiles
# ---------------------------------------------------

avg_score = sum(scores.values())/len(scores)

if avg_score >= 4:
    reform_orientation = "Reform-oriented audiences may be relatively open to ambitious policy change."
else:
    reform_orientation = "Incremental reform strategies may be more effective for this audience."

if scores["Authority"] >=4:
    risk_profile = "This audience appears relatively risk-averse and may prefer policy stability."
else:
    risk_profile = "This audience may be more open to experimentation and innovation."

campaign_strategy = (
"Advocacy campaigns targeting this audience should combine clear ethical framing "
"with credible evidence and narratives that connect the issue to everyday experiences."
)

advocacy_lever = (
"Potential advocacy levers may include coalition-building with credible institutions, "
"strategic media engagement, and framing the issue in ways that align with existing "
"moral intuitions."
)

# ---------------------------------------------------
# Generate Report
# ---------------------------------------------------

if st.button("Generate Report"):

    st.header("Audience Context")

    st.write(audience_explanations[audience])
    st.write(geography_explanations[geography])
    st.write(stakeholder_explanations[stakeholder])
    st.write(campaign_explanations[campaign])

    st.header("Moral Foundations Profile")

    for k,v in scores.items():
        st.write(f"{k}: {v}")

    st.write(foundation_analysis[dominant])

    st.header("Reform Orientation")
    st.write(reform_orientation)

    st.header("Risk Profile")
    st.write(risk_profile)

    st.header("Campaign Strategy")
    st.write(campaign_strategy)

    st.header("Advocacy Lever")
    st.write(advocacy_lever)

    st.header("Full Report Summary")

    summary = f"""
BAAMT Advocacy Analysis

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign Type: {campaign}

Dominant Moral Foundation: {dominant}

Strategic Implication:
{foundation_analysis[dominant]}

Reform Orientation:
{reform_orientation}

Risk Profile:
{risk_profile}

Campaign Strategy:
{campaign_strategy}

Advocacy Lever:
{advocacy_lever}
"""

    st.download_button(
        label="Download Report",
        data=summary,
        file_name="baamt_report.txt",
        mime="text/plain"
    )
