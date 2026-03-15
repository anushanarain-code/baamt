import streamlit as st
import pandas as pd

st.set_page_config(page_title="BAAMT", layout="wide")

# ---------------------------------------------------
# INTRODUCTION
# ---------------------------------------------------

st.title("BAAMT – Behavioural Advocacy and Messaging Tool")

st.write(
"BAAMT is a behavioural analysis prototype designed to support advocacy organisations, "
"policy researchers, and campaign strategists in designing more effective messaging. "
"The tool combines insights from moral psychology, behavioural science, and advocacy "
"strategy to analyse how different audiences may interpret advocacy arguments."
)

st.write(
"The tool evaluates audience moral intuitions, contextual political factors, and "
"campaign objectives in order to generate structured recommendations for advocacy "
"communication strategies."
)

# ---------------------------------------------------
# Audience Context
# ---------------------------------------------------

st.header("Audience Context")

st.markdown("""
Select the campaign context below. These contextual inputs help interpret how
different audiences may respond to advocacy messages.

Audience characteristics, geographic political environments, stakeholder
dynamics, and campaign objectives all influence how ideas circulate and
gain legitimacy within public debate.
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
# MORAL FOUNDATIONS THEORY
# ---------------------------------------------------

st.header("Theoretical Framework: Moral Foundations Theory")

st.markdown("""
BAAMT draws on **Moral Foundations Theory**, a framework developed in moral
psychology to explain how individuals intuitively evaluate ethical and
political issues.

Research suggests that people often respond to moral narratives before
engaging in detailed policy reasoning. Advocacy messages that resonate
with an audience's moral intuitions can therefore be significantly more
persuasive than messages that rely purely on technical information.

This assessment evaluates five commonly studied moral foundations:

Care / Harm – concern for compassion and the reduction of suffering  
Fairness / Justice – concern for equality and reciprocal treatment  
Authority / Respect – concern for institutional order and leadership  
Loyalty / Solidarity – concern for collective identity and community  
Purity / Integrity – concern for ethical responsibility and standards
""")

# ---------------------------------------------------
# QUESTIONNAIRE
# ---------------------------------------------------

st.header("Behavioural Questionnaire")

st.markdown("""
Please rate each statement using the scale below.

1 – Strongly Disagree  
2 – Disagree  
3 – Neutral  
4 – Agree  
5 – Strongly Agree
""")

questions = {

"Care1":"Public policies should prioritise reducing suffering whenever possible.",
"Care2":"Protecting vulnerable groups should be a central goal of social policy.",

"Fairness1":"Justice and fairness should guide policy decisions even when trade-offs exist.",
"Fairness2":"Systems should ensure that everyone is treated equally.",

"Authority1":"Respect for institutions is important for maintaining social stability.",
"Authority2":"Policies should reinforce trust in established institutions.",

"Loyalty1":"People should feel strong responsibility toward their community.",
"Loyalty2":"Supporting one's social group is an important moral value.",

"Purity1":"Society should uphold strong ethical standards.",
"Purity2":"Maintaining moral integrity is essential for social trust."
}

scores = {}

for q in questions:
    scores[q] = st.slider(questions[q],1,5,3)

# ---------------------------------------------------
# SCORE CALCULATION
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
# MORAL PROFILE CHART
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
# ANALYSIS SECTIONS
# ---------------------------------------------------

context_analysis = f"""
The campaign context selected for this assessment combines the audience
type **{audience}**, the geographical environment **{geography}**, the
stakeholder group **{stakeholder}**, and the strategic campaign objective
**{campaign}**.

These contextual variables influence how advocacy arguments are interpreted
within public debate. For example, audiences in the **{geography}** context
often operate within specific institutional structures and political
traditions that shape the perceived legitimacy of policy proposals.

Similarly, the characteristics of the **{audience}** audience influence
how messages are processed. Some audiences respond more strongly to
moral narratives and social values, while others prioritise technical
evidence or institutional credibility. The role of **{stakeholder}**
actors further shapes how ideas circulate, as these actors often act
as intermediaries who amplify or legitimise particular arguments.

Taken together, these contextual dimensions define the environment
within which advocacy messaging must operate.
"""

foundation_analysis = f"""
The behavioural questionnaire indicates that the dominant moral
foundation for this audience appears to be **{dominant}**.

Moral foundations shape intuitive judgments about ethical and political
issues. When advocacy messages resonate with the dominant moral
priorities of an audience, those messages are often perceived as more
credible and emotionally compelling.
"""

reform_orientation = """
The response pattern suggests that the audience may be more receptive
to policy proposals framed as pragmatic improvements rather than
disruptive systemic change.
"""

risk_profile = f"""
Messaging that contradicts the dominant moral foundation (**{dominant}**)
may appear ideologically misaligned with audience values.
"""

campaign_strategy = f"""
Because **{dominant}** is the dominant moral foundation, campaign
narratives should emphasise themes aligned with this value system.
"""

messaging_strategy = f"""
Messaging should align moral resonance with the expectations of
**{audience}** audiences within the **{geography}** policy context.
"""

# ---------------------------------------------------
# EXPANDED EXAMPLE MESSAGES
# ---------------------------------------------------

example_messages = {

"Care":
"""
Every policy decision ultimately affects the wellbeing of real people and
communities. When systems fail to reduce preventable harm or suffering,
the consequences are often borne by those who are already vulnerable.
Advocacy efforts that prioritise compassion and protection can therefore
play a crucial role in building policies that reflect shared social
responsibility and care for others.
""",

"Fairness":
"""
A stable and legitimate society depends on systems that distribute
responsibilities and benefits fairly. When institutions allow harms
or costs to be shifted onto others without accountability, public
trust weakens and inequalities deepen. Strengthening policies that
promote fairness and transparency can help ensure that institutions
operate responsibly and serve the interests of society as a whole.
""",

"Authority":
"""
Strong and credible institutions are essential for maintaining public
trust and social stability. Clear standards, effective oversight,
and responsible governance help ensure that institutions function as
intended and protect the public interest. Strengthening institutional
accountability can therefore reinforce confidence in regulatory systems
and the policies that guide them.
""",

"Loyalty":
"""
Communities thrive when individuals recognise a shared responsibility
to protect collective wellbeing. Policies that strengthen cooperation
and reinforce shared values can help ensure that communities remain
resilient in the face of social and economic challenges. Working
together to support responsible reforms can therefore help build
stronger and more cohesive societies.
""",

"Purity":
"""
Societies are often judged by the ethical standards they uphold.
When institutions or industries operate without clear moral
accountability, public trust and social legitimacy can deteriorate.
Ensuring that policies promote integrity, responsibility, and ethical
conduct helps maintain the moral foundations on which stable and
trustworthy institutions depend.
"""
}

final_summary = f"""
Overall, the analysis suggests that advocacy strategies for this
campaign should align moral narratives, audience expectations,
and institutional realities.
"""

# ---------------------------------------------------
# REPORT GENERATION
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

    st.header("Integrated Strategic Summary")
    st.write(final_summary)

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

Example Advocacy Message
{example_messages[dominant]}

Integrated Strategic Summary
{final_summary}
"""

    st.download_button(
        "Download Full Report",
        report,
        file_name="BAAMT_advocacy_analysis.txt",
        mime="text/plain"
    )
