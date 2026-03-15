import streamlit as st

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
The following statements explore how people evaluate ethical and social issues.

Please rate each statement using the scale below:

**1 – Strongly Disagree**  
**2 – Disagree**  
**3 – Neutral**  
**4 – Agree**  
**5 – Strongly Agree**

Your responses allow the tool to estimate which **moral foundations**
are most influential for the audience. These moral priorities are
combined with the campaign context to generate advocacy insights.
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
# Context Analysis
# ---------------------------------------------------

context_analysis = f"""
The campaign context selected for this assessment combines the
audience type **{audience}**, the geographical environment **{geography}**,
the stakeholder category **{stakeholder}**, and the strategic campaign
objective **{campaign}**.

These contextual dimensions significantly influence how advocacy
messages are interpreted. For example, audiences within the {geography}
policy environment often evaluate advocacy proposals within existing
institutional frameworks and political priorities. The selected
audience group, {audience}, also shapes communication strategy
because different audiences process information differently: some
respond strongly to moral narratives, while others prioritise
technical evidence or institutional credibility.

Stakeholder dynamics also influence advocacy outcomes. In this case,
the role of **{stakeholder}** indicates that advocacy messages may
spread through social networks, institutional channels, or community
leadership structures. Finally, the chosen campaign objective,
**{campaign}**, determines whether the communication strategy should
prioritise behavioural change, policy reform, or broader awareness
building.

Taken together, these contextual variables provide the strategic
environment within which moral narratives and advocacy messages
must operate.
"""

# ---------------------------------------------------
# Moral Analysis
# ---------------------------------------------------

foundation_analysis = f"""
The behavioural questionnaire indicates that the dominant moral
foundation for this audience appears to be **{dominant}**. Moral
foundations influence how people intuitively interpret social and
political issues, often shaping emotional responses before detailed
reasoning takes place.

When advocacy messaging aligns with the dominant moral priorities
of an audience, the message is more likely to be perceived as
credible and persuasive. Conversely, messages that ignore these
moral intuitions may struggle to gain traction even if they are
factually strong.
"""

# ---------------------------------------------------
# Reform Orientation
# ---------------------------------------------------

avg = sum(foundation_scores.values())/5

if avg >=4:
    reform_orientation = """
The overall response pattern suggests that the audience may be open
to relatively ambitious reforms, provided that those reforms are
presented as ethically justified and socially beneficial.
"""
else:
    reform_orientation = """
The response pattern suggests that the audience may prefer gradual
or incremental reforms. Campaigns may therefore benefit from
presenting change as practical improvement rather than systemic
disruption.
"""

# ---------------------------------------------------
# Risk Profile
# ---------------------------------------------------

risk_profile = f"""
The behavioural and contextual profile suggests several strategic
risks that campaigns should consider. Messaging that contradicts
the audience's dominant moral foundation (**{dominant}**) may
appear ideologically misaligned. In addition, campaigns operating
in the **{geography}** environment must remain sensitive to local
institutional norms and policy debates.

Finally, communication strategies that overlook the influence of
**{stakeholder}** groups may struggle to build legitimacy or
momentum within relevant networks.
"""

# ---------------------------------------------------
# Campaign Strategy
# ---------------------------------------------------

campaign_strategy = f"""
The recommended campaign strategy integrates three dimensions of
analysis generated by this tool: the **moral foundations profile**,
the **audience and stakeholder context**, and the **campaign
objective**.

Because the dominant moral foundation is **{dominant}**, advocacy
messages should emphasise themes associated with this value system.
However, these moral narratives must also be adapted to the specific
communication environment represented by the selected audience
(**{audience}**) and geographic context (**{geography}**).

Within this context, the role of **{stakeholder}** actors suggests
that building credibility and social endorsement may be important
for amplifying the campaign's influence. Campaign strategies may
therefore benefit from partnerships, coalition building, or
institutional engagement depending on the nature of the campaign.

The strategic objective of **{campaign}** further shapes the
approach. Behaviour change campaigns may emphasise social norms
and everyday decisions, whereas policy advocacy campaigns may
focus on regulatory frameworks, governance structures, and
institutional accountability.
"""

# ---------------------------------------------------
# Messaging Strategy
# ---------------------------------------------------

messaging_strategy = f"""
An effective messaging strategy should integrate moral framing,
audience expectations, and the institutional environment in which
the campaign operates.

Because the dominant moral foundation identified in the questionnaire
is **{dominant}**, campaign messages should foreground values and
narratives associated with this moral orientation. At the same time,
the communication style should reflect the characteristics of the
target audience (**{audience}**) and the broader policy context
(**{geography}**).

In addition, stakeholder dynamics involving **{stakeholder}** may
shape how messages spread and gain legitimacy. Messages that are
reinforced by credible voices or institutions may therefore be
particularly influential.

Finally, the strategic objective of the campaign (**{campaign}**)
should guide the tone and framing of communication. Behaviour
change campaigns may focus on everyday practices and social norms,
while policy advocacy campaigns may emphasise governance,
regulatory reform, and institutional accountability.

By aligning moral narratives with audience context and campaign
goals, advocacy organisations can design messages that are both
ethically resonant and strategically effective.
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
