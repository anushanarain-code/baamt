import streamlit as st
import pandas as pd

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("BAAMT – Behavioural Advocacy and Messaging Tool")

st.write(
"BAAMT is a behavioural analysis tool designed to support advocacy organisations, "
"policy researchers, and campaign strategists in designing more effective communication. "
"The tool integrates insights from moral psychology, behavioural science, and advocacy "
"strategy to generate structured guidance on how different audiences may interpret "
"advocacy messaging."
)

# ---------------------------------------------------
# Audience Context
# ---------------------------------------------------

st.header("Audience Context")

st.markdown("""
Select the context in which your advocacy campaign operates.

These contextual factors shape how advocacy messages are interpreted
and are incorporated directly into the strategic analysis generated
by the tool.

**Audience Type** – the primary group the campaign aims to influence  
**Geography** – the political and institutional context  
**Stakeholder Type** – actors shaping discourse or decisions  
**Campaign Type** – the primary strategic objective
""")

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
# THEORY SECTION
# ---------------------------------------------------

st.header("Theoretical Framework: Moral Foundations Theory")

st.markdown("""
BAAMT draws on **Moral Foundations Theory**, a framework developed by
social psychologists such as Jonathan Haidt to explain how people
intuitively evaluate ethical and political issues.

The theory suggests that human moral reasoning is influenced by several
core psychological foundations. These foundations operate as intuitive
moral lenses through which people interpret arguments, policies, and
social behaviour.

The five foundations included in this assessment are:

**Care / Harm**  
Concerns about compassion, protection, and the reduction of suffering.

**Fairness / Justice**  
Concerns about equality, reciprocity, and whether systems distribute
benefits and responsibilities fairly.

**Authority / Respect**  
Concerns about institutional order, leadership, and the importance
of maintaining stable social systems.

**Loyalty / Solidarity**  
Concerns about community belonging, collective identity, and protecting
one's social group.

**Purity / Integrity**  
Concerns about ethical integrity, moral responsibility, and maintaining
societal standards.

Research suggests that advocacy messages that resonate with the moral
priorities of an audience are more likely to be persuasive. BAAMT uses
these foundations to estimate which moral narratives may be most
effective in a given advocacy context.
""")

# ---------------------------------------------------
# Behaviour Questionnaire
# ---------------------------------------------------

st.header("Behavioural Questionnaire")

st.markdown("""
Please rate each statement using the following scale:

1 – Strongly Disagree  
2 – Disagree  
3 – Neutral  
4 – Agree  
5 – Strongly Agree

These responses allow the tool to estimate which **moral foundations**
are most influential for the audience.
""")

questions = {

"Care1":"Public policies should prioritise reducing suffering whenever possible.",
"Care2":"Protecting vulnerable groups should be a central goal of social policy.",

"Fairness1":"Justice and fairness should guide policy decisions even when trade-offs exist.",
"Fairness2":"Systems should ensure that everyone is treated equally.",

"Authority1":"Respect for institutions is important for maintaining social stability.",
"Authority2":"Policies should reinforce trust in established institutions.",

"Loyalty1":"People should feel a strong responsibility toward their community.",
"Loyalty2":"Supporting one's social group is an important moral value.",

"Purity1":"Society should uphold strong ethical standards.",
"Purity2":"Maintaining moral integrity is essential for a healthy society."
}

scores = {}

for q in questions:
    scores[q] = st.slider(questions[q],1,5,3)

# ---------------------------------------------------
# Moral Foundation Scores
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
# Moral Foundations Chart
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
# Example Messaging (Expanded)
# ---------------------------------------------------

example_messages = {

"Care":
"""
Every policy decision has real consequences for vulnerable individuals
and communities. By prioritising reforms that reduce suffering and
protect those who are most at risk, we can create systems that reflect
our shared commitment to compassion and responsibility. Thoughtful
policy change today can help build a society where fewer individuals
are left exposed to preventable harm.
""",

"Fairness":
"""
A well-functioning society depends on systems that treat people fairly
and distribute responsibilities in a balanced way. When policies allow
costs or harms to be shifted onto others without accountability,
inequalities deepen and public trust erodes. By strengthening rules
that ensure transparency and fairness, we can create institutions
that reward responsible behaviour and protect the interests of all.
""",

"Authority":
"""
Strong and credible institutions are essential for maintaining
social stability and public trust. Effective governance requires
clear standards, responsible oversight, and policies that reinforce
confidence in the systems that regulate economic and social life.
Strengthening institutional accountability can therefore play a key
role in ensuring that regulations operate as intended and that
public interests are protected.
""",

"Loyalty":
"""
Communities thrive when people feel a shared responsibility for
protecting collective wellbeing. Policies that strengthen community
resilience and reinforce shared values can help ensure that social
systems continue to serve the long-term interests of society.
Working together to support responsible reforms can therefore help
build stronger and more resilient communities.
""",

"Purity":
"""
Societies are ultimately judged by the ethical standards they uphold.
When institutions and industries operate without clear moral
accountability, public confidence and social trust can deteriorate.
Ensuring that policies promote integrity, responsibility, and ethical
conduct helps maintain the moral foundations on which stable and
trustworthy institutions depend.
"""
}

# ---------------------------------------------------
# Generate Report
# ---------------------------------------------------

if st.button("Generate Report"):

    st.header("Example Advocacy Message")
    st.write(example_messages[dominant])

    report = f"""
BAAMT Advocacy Analysis

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign Type: {campaign}

Dominant Moral Foundation: {dominant}

Example Advocacy Message
{example_messages[dominant]}
"""

    st.download_button(
        "Download Full Report",
        report,
        file_name="baamt_report.txt",
        mime="text/plain"
    )
