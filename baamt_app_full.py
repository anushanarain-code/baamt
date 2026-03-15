import streamlit as st
import pandas as pd

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("BAAMT – Behavioural Advocacy and Messaging Tool")

st.write(
"BAAMT is a behavioural analysis tool designed to support advocacy organisations, "
"policy researchers, and campaign strategists in designing more effective communication."
)

# ---------------------------------------------------
# Audience Context
# ---------------------------------------------------

st.header("Audience Context")

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
# Moral Foundations Theory
# ---------------------------------------------------

st.header("Theoretical Framework: Moral Foundations Theory")

st.markdown("""
BAAMT draws on **Moral Foundations Theory**, a framework developed in moral
psychology to explain how individuals intuitively evaluate ethical and
political issues.

The theory proposes that people rely on several core moral foundations
when judging policies and social behaviour.

The five foundations included in this assessment are:

**Care / Harm** – compassion and protection from suffering  
**Fairness / Justice** – equality and reciprocity  
**Authority / Respect** – institutional order and leadership  
**Loyalty / Solidarity** – community belonging and collective identity  
**Purity / Integrity** – ethical responsibility and moral standards

Advocacy messages that resonate with the dominant moral priorities of
an audience are often more persuasive than messages that rely only on
technical evidence.
""")

# ---------------------------------------------------
# Questionnaire
# ---------------------------------------------------

st.header("Behavioural Questionnaire")

questions = {

"Care1":"Public policies should prioritise reducing suffering whenever possible.",
"Care2":"Protecting vulnerable groups should be a central goal of social policy.",

"Fairness1":"Justice and fairness should guide policy decisions.",
"Fairness2":"Systems should ensure that everyone is treated equally.",

"Authority1":"Respect for institutions is important for social stability.",
"Authority2":"Policies should reinforce trust in institutions.",

"Loyalty1":"People should feel strong responsibility toward their community.",
"Loyalty2":"Supporting one's social group is an important value.",

"Purity1":"Society should uphold strong ethical standards.",
"Purity2":"Maintaining moral integrity is essential."
}

scores = {}

for q in questions:
    scores[q] = st.slider(questions[q],1,5,3)

# ---------------------------------------------------
# Score Calculation
# ---------------------------------------------------

care = (scores["Care1"] + scores["Care2"]) / 2
fairness = (scores["Fairness1"] + scores["Fairness2"]) / 2
authority = (scores["Authority1"] + scores["Authority2"]) / 2
loyalty = (scores["Loyalty1"] + scores["Loyalty2"]) / 2
purity = (scores["Purity1"] + scores["Purity2"]) / 2

foundation_scores = {
"Care":care,
"Fairness":fairness,
"Authority":authority,
"Loyalty":loyalty,
"Purity":purity
}

dominant = max(foundation_scores, key=foundation_scores.get)

# ---------------------------------------------------
# Chart
# ---------------------------------------------------

st.subheader("Moral Foundations Profile")

chart_data = pd.DataFrame(
{
"Foundation": list(foundation_scores.keys()),
"Score": list(foundation_scores.values())
}
)

chart_data = chart_data.set_index("Foundation")

st.bar_chart(chart_data)

# ---------------------------------------------------
# ANALYSIS COMPONENTS
# ---------------------------------------------------

context_analysis = f"""
The campaign context combines the audience type **{audience}**, the
geographical environment **{geography}**, the stakeholder group
**{stakeholder}**, and the strategic campaign objective **{campaign}**.

These contextual dimensions shape how advocacy messages are interpreted
and how ideas circulate within policy systems and social networks.
"""

foundation_analysis = f"""
The questionnaire results suggest that **{dominant}** is the dominant
moral foundation influencing audience responses. Moral foundations
shape intuitive judgments about social and political issues.
"""

reform_orientation = """
The pattern of responses suggests that the audience may prefer
gradual and practical reforms that build upon existing systems.
"""

risk_profile = f"""
Messaging that conflicts with the audience's dominant moral foundation
(**{dominant}**) may face resistance even if the underlying evidence is strong.
"""

campaign_strategy = f"""
The recommended campaign strategy integrates the moral foundations
profile with the audience context. Because **{dominant}** is dominant,
campaign narratives should emphasise themes aligned with this value.
"""

messaging_strategy = f"""
Effective messaging should combine moral resonance with contextual
credibility. Communication should reflect the characteristics of
the **{audience}** audience within the **{geography}** policy context.
"""

example_messages = {

"Care":
"""
Every policy decision has real consequences for vulnerable individuals
and communities. By prioritising reforms that reduce suffering and
protect those at risk, society can move toward more compassionate
systems that safeguard wellbeing.
""",

"Fairness":
"""
A fair society depends on systems that distribute responsibilities
and benefits equitably. Strengthening policies that promote fairness
helps ensure that institutions operate transparently and responsibly.
""",

"Authority":
"""
Strong institutions rely on clear standards and responsible oversight.
Ensuring that governance systems operate with integrity strengthens
public trust and institutional stability.
""",

"Loyalty":
"""
Communities thrive when individuals feel responsible for protecting
shared values and collective wellbeing. Supporting reforms that
strengthen communities helps build resilient societies.
""",

"Purity":
"""
Societies are judged by the ethical standards they uphold.
Ensuring integrity and accountability helps maintain trust
in institutions and social systems.
"""
}

# ---------------------------------------------------
# Generate Report
# ---------------------------------------------------

if st.button("Generate Report"):

    st.header("Audience Context Analysis")
    st.write(context_analysis)

    st.header("Moral Foundations Analysis")
    st.write(foundation_analysis)

    st.header("Reform Orientation")
    st.write(reform_orientation)

    st.header("Risk Profile")
    st.write(risk_profile)

    st.header("Campaign Strategy")
    st.write(campaign_strategy)

    st.header("Messaging Strategy")
    st.write(messaging_strategy)

    st.header("Example Advocacy Messages")
    st.write(example_messages[dominant])

    report = f"""
BAAMT Advocacy Analysis

Audience Context Analysis
{context_analysis}

Moral Foundations Analysis
{foundation_analysis}

Reform Orientation
{reform_orientation}

Risk Profile
{risk_profile}

Campaign Strategy
{campaign_strategy}

Messaging Strategy
{messaging_strategy}

Example Message
{example_messages[dominant]}
"""

    st.download_button(
        "Download Full Report",
        report,
        file_name="baamt_report.txt",
        mime="text/plain"
    )
