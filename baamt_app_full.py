import streamlit as st
import pandas as pd

st.set_page_config(page_title="BAAMT", layout="wide")

# ---------------------------------------------------
# INTRODUCTION (RESTORED)
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
credible and emotionally compelling. Conversely, arguments that conflict
with these intuitive moral expectations may encounter resistance even
when supported by strong empirical evidence.

Understanding the moral profile of an audience therefore helps advocacy
organisations frame their arguments in ways that connect more directly
with audience values.
"""

reform_orientation = """
The distribution of responses suggests that the audience may prefer
policy proposals that are framed as pragmatic improvements rather
than radical systemic change. Campaigns may therefore benefit from
presenting reforms as practical steps that strengthen existing
institutions while addressing identifiable problems.

Positioning reforms as responsible adjustments rather than disruptive
transformations can help reduce perceived risk and increase political
acceptability.
"""

risk_profile = f"""
Several potential strategic risks emerge from this behavioural profile.

First, messaging that contradicts the dominant moral foundation
(**{dominant}**) may appear ideologically misaligned with audience
values. Second, advocacy campaigns operating in the **{geography}**
environment must remain sensitive to existing policy debates and
institutional norms.

Finally, campaigns that overlook the influence of **{stakeholder}**
actors may struggle to gain traction within the networks through
which political ideas and narratives typically spread.
"""

campaign_strategy = f"""
An effective campaign strategy should integrate moral framing with
the broader advocacy environment identified in the contextual analysis.

Because **{dominant}** appears to be the dominant moral foundation,
campaign narratives should emphasise themes aligned with this value
system. At the same time, these narratives must be adapted to the
communication style of the **{audience}** audience and the institutional
dynamics of the **{geography}** environment.

Stakeholder engagement with **{stakeholder}** actors may also be
important for amplifying the campaign's influence. Strategic alliances,
public endorsements, or institutional engagement can help translate
moral narratives into broader public legitimacy.
"""

messaging_strategy = f"""
The messaging strategy should combine moral resonance with contextual
credibility. Messages that appeal to **{dominant}** values are more
likely to feel intuitively compelling to the target audience.

However, these narratives should also acknowledge the policy
environment in **{geography}**, the expectations of **{audience}**
audiences, and the influence of **{stakeholder}** actors.

By integrating moral framing with contextual awareness, advocacy
organisations can produce messages that are both ethically persuasive
and strategically realistic.
"""

example_messages = {
"Care":"Policy decisions ultimately affect the wellbeing of real people...",
"Fairness":"A fair society depends on systems that distribute responsibilities equitably...",
"Authority":"Strong institutions require clear standards and responsible oversight...",
"Loyalty":"Communities thrive when people work together to protect shared values...",
"Purity":"Societies are judged by the ethical standards they uphold..."
}

final_summary = f"""
Overall, the analysis suggests that advocacy strategies for this
campaign should align moral narratives, audience expectations,
and institutional realities. By integrating the moral foundation
profile with the broader campaign context, organisations can design
advocacy messages that resonate with audience values while also
remaining credible within the relevant political environment.
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
