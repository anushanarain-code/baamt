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
# Moral Foundations Chart (SAFE ADDITION)
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
# Context Analysis
# ---------------------------------------------------

context_analysis = f"""
The campaign context selected for this assessment combines the
audience type **{audience}**, the geographical environment **{geography}**,
the stakeholder category **{stakeholder}**, and the strategic campaign
objective **{campaign}**.

These contextual variables influence how advocacy messages are
interpreted and how ideas circulate within policy and social
systems. For example, advocacy operating in the **{geography}**
environment may interact with specific institutional structures
and regulatory traditions. Likewise, the selected audience group,
**{audience}**, may evaluate advocacy arguments through different
lenses depending on whether they prioritise personal values,
professional expertise, or institutional credibility.

The role of **{stakeholder}** actors also shapes advocacy outcomes.
Messages that resonate with these actors may spread more widely
through networks, public discourse, or institutional processes.

Finally, the strategic objective of the campaign — **{campaign}** —
determines whether the focus should be on changing everyday
behaviour, influencing policy decisions, or building broader
public awareness around the issue.
"""

# ---------------------------------------------------
# Moral Analysis
# ---------------------------------------------------

foundation_analysis = f"""
The questionnaire responses suggest that the dominant moral
foundation shaping audience responses is **{dominant}**.

Moral foundations influence how people intuitively interpret
ethical and political questions. When advocacy messages align
with these intuitive moral priorities, they are more likely to
be perceived as credible and persuasive.
"""

# ---------------------------------------------------
# Reform Orientation
# ---------------------------------------------------

avg = sum(foundation_scores.values())/5

if avg >=4:
    reform_orientation = """
The response pattern suggests that the audience may be receptive
to more ambitious reforms when these reforms are framed as morally
justified and socially beneficial.
"""
else:
    reform_orientation = """
The response pattern suggests that the audience may prefer gradual
or incremental reforms that build upon existing systems.
"""

# ---------------------------------------------------
# Risk Profile
# ---------------------------------------------------

risk_profile = f"""
Several strategic risks emerge from this behavioural profile.
Messaging that contradicts the audience's dominant moral
foundation (**{dominant}**) may appear unconvincing. In addition,
campaigns operating in **{geography}** must remain sensitive to
local institutional dynamics and policy debates.
"""

# ---------------------------------------------------
# Campaign Strategy
# ---------------------------------------------------

campaign_strategy = f"""
The recommended campaign strategy integrates the moral foundations
profile with the broader campaign context.

Because **{dominant}** is the dominant moral foundation, advocacy
messages should emphasise themes associated with this value system.
However, these narratives must also be adapted to the communication
environment defined by the selected audience (**{audience}**) and
geographical setting (**{geography}**).

Stakeholder dynamics involving **{stakeholder}** may also influence
how messages spread and gain legitimacy. Strategic partnerships,
institutional engagement, or community endorsement may therefore
strengthen the campaign's impact.

Finally, the strategic objective of the campaign (**{campaign}**)
determines whether messaging should emphasise behavioural norms,
policy reforms, or broader public awareness.
"""

# ---------------------------------------------------
# Messaging Strategy
# ---------------------------------------------------

messaging_strategy = f"""
Effective messaging should combine moral resonance with contextual
credibility. Because **{dominant}** is the dominant moral foundation,
messages should foreground narratives aligned with this value.

At the same time, communication should be tailored to the selected
audience (**{audience}**) and policy environment (**{geography}**).
Messages may gain greater legitimacy when reinforced by relevant
stakeholders such as **{stakeholder}** actors.

By integrating moral framing with audience context and campaign
objectives, advocacy organisations can design communication that
is both persuasive and strategically coherent.
"""

# ---------------------------------------------------
# Example Messaging
# ---------------------------------------------------

example_messages = {
"Care":"Policies that reduce suffering can strengthen society as a whole.",
"Fairness":"Fair systems ensure that responsibility and benefits are shared equitably.",
"Authority":"Strong institutions require clear standards and responsible governance.",
"Loyalty":"Communities thrive when we work together to protect shared values.",
"Purity":"Ethical integrity is essential for a healthy and responsible society."
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

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign Type: {campaign}

Dominant Moral Foundation: {dominant}

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
