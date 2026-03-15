import streamlit as st

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("BAAMT – Behavioural Advocacy and Messaging Tool")

st.write(
"BAAMT is a behavioural analysis tool designed to help advocacy organizations, "
"policy researchers, and social campaigners understand how different audiences "
"may respond to advocacy messaging. The tool combines insights from behavioural "
"science and moral psychology to generate strategic guidance for advocacy campaigns."
)

# ---------------------------------------------------
# Audience Context
# ---------------------------------------------------

st.header("Audience Context")

st.markdown("""
Select the context in which your advocacy campaign operates.

These contextual variables shape how advocacy messages are interpreted and
help the tool generate more relevant strategic recommendations.

**Audience Type** – The primary group whose attitudes or behaviour the campaign aims to influence.  
**Geography** – The political and regulatory environment in which advocacy takes place.  
**Stakeholder Type** – Actors who influence public discourse or policy decisions.  
**Campaign Type** – The main advocacy strategy being pursued.
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
**3 – Neutral / Unsure**  
**4 – Agree**  
**5 – Strongly Agree**

Your responses help the tool estimate which **moral foundations** are most influential
for the selected audience profile. These moral priorities are then combined with the
audience type and campaign context to generate strategic recommendations for advocacy
communication.
""")

questions = {

"Care1":"Public policies should prioritise reducing suffering whenever possible.",
"Care2":"Protecting vulnerable groups should be a central goal of social policy.",

"Fairness1":"Justice and fairness should guide policy decisions even if they require economic trade-offs.",
"Fairness2":"Systems should ensure that everyone is treated equally under the rules.",

"Authority1":"Respect for institutions and leadership is important for maintaining social order.",
"Authority2":"Policies should reinforce trust in established institutions.",

"Loyalty1":"People should feel a strong sense of responsibility toward their community.",
"Loyalty2":"Supporting one's social group is an important moral value.",

"Purity1":"Society should uphold strong ethical standards in both public and private life.",
"Purity2":"Maintaining moral integrity is essential for a healthy society."
}

scores = {}

for q in questions:
    scores[q] = st.slider(questions[q],1,5,3)

# ---------------------------------------------------
# Calculate foundation scores
# ---------------------------------------------------

care_score = (scores["Care1"] + scores["Care2"]) / 2
fairness_score = (scores["Fairness1"] + scores["Fairness2"]) / 2
authority_score = (scores["Authority1"] + scores["Authority2"]) / 2
loyalty_score = (scores["Loyalty1"] + scores["Loyalty2"]) / 2
purity_score = (scores["Purity1"] + scores["Purity2"]) / 2

foundation_scores = {
"Care":care_score,
"Fairness":fairness_score,
"Authority":authority_score,
"Loyalty":loyalty_score,
"Purity":purity_score
}

dominant = max(foundation_scores, key=foundation_scores.get)

# ---------------------------------------------------
# Analysis Text
# ---------------------------------------------------

foundation_analysis = {

"Care":
"""The responses suggest that compassion and harm reduction are likely to
be particularly influential moral considerations for this audience.
When audiences prioritize the Care foundation, they tend to respond strongly
to narratives that highlight suffering, vulnerability, and the responsibility
to protect others from harm. Advocacy campaigns targeting such audiences
often benefit from storytelling, concrete examples, and evidence showing how
policy decisions affect real lives. By connecting reforms to the reduction of
suffering and the protection of vulnerable groups, campaigns can make ethical
arguments feel immediate and compelling.""",

"Fairness":
"""This audience appears especially responsive to concerns related to justice,
equity, and fair treatment. Individuals who prioritise the Fairness foundation
often evaluate issues by asking whether systems distribute costs and benefits
in a balanced way. Advocacy messages that expose hidden inequalities,
unfair advantages, or structural injustices tend to resonate strongly.
Campaigns may therefore benefit from highlighting how reforms create a
more transparent and equitable system.""",

"Authority":
"""The responses indicate that respect for institutions and social order
plays an important role in how this audience evaluates policy questions.
Audiences with a strong Authority orientation often respond positively
to messages that emphasise responsible governance, institutional integrity,
and the importance of well-functioning regulatory systems. Advocacy
campaigns targeting this moral orientation may therefore benefit from
framing reforms as strengthening institutions rather than challenging them.""",

"Loyalty":
"""This profile suggests that group identity and collective responsibility
are influential moral considerations for this audience. Loyalty-oriented
audiences often respond to narratives that highlight solidarity,
community wellbeing, and shared responsibility. Advocacy campaigns
may therefore benefit from emphasising how proposed reforms strengthen
communities and protect shared values.""",

"Purity":
"""The responses suggest sensitivity to moral integrity and ethical
boundaries. Audiences influenced by the Purity foundation often
interpret policy debates through the lens of ethical responsibility
and moral standards. Advocacy messages that frame issues as questions
of integrity, responsibility, and societal values may therefore
resonate strongly."""
}

# ---------------------------------------------------
# Strategy Section
# ---------------------------------------------------

campaign_strategy_text = f"""
The campaign strategy suggested by BAAMT is derived from three key inputs:
the **dominant moral foundation identified in the questionnaire**, the
**selected audience profile**, and the **campaign context** chosen at the
beginning of the tool.

Because the dominant moral foundation in this case appears to be **{dominant}**,
the campaign narrative should emphasise themes that align with this moral
priority. At the same time, the messaging should be tailored to the selected
audience group (**{audience}**) and the campaign approach (**{campaign}**).

In practical terms, this means that advocacy messages should combine
ethical framing that resonates with the {dominant} foundation together
with examples, policy proposals, or narratives that are appropriate
for the selected audience. By aligning moral framing with audience
context, campaigns can increase both the clarity and persuasive power
of their communication.
"""

# ---------------------------------------------------
# Example Messaging
# ---------------------------------------------------

example_messages = {

"Care":
"Example message: 'Policy reforms can significantly reduce suffering and create a more compassionate society. By supporting responsible reforms today, we can protect vulnerable populations and build systems that reflect our shared commitment to wellbeing.'",

"Fairness":
"Example message: 'A fair system ensures that responsibility is shared and that no group bears hidden costs. Transparent policies help create markets and institutions that reward ethical practices.'",

"Authority":
"Example message: 'Strong institutions depend on clear standards and responsible governance. Strengthening oversight helps ensure that systems operate with integrity and public trust.'",

"Loyalty":
"Example message: 'Communities thrive when we work together to protect shared values. Supporting responsible reforms strengthens the wellbeing of our society as a whole.'",

"Purity":
"Example message: 'Societies are judged by the standards they uphold. Ensuring ethical responsibility in policy and industry helps maintain the integrity of our institutions.'"
}

# ---------------------------------------------------
# Generate Report
# ---------------------------------------------------

if st.button("Generate Report"):

    st.header("Audience Profile Analysis")

    st.write(foundation_analysis[dominant])

    st.header("Campaign Strategy")

    st.write(campaign_strategy_text)

    st.header("Example Advocacy Messaging")

    st.write(example_messages[dominant])

    report = f"""
BAAMT Advocacy Analysis

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign Type: {campaign}

Dominant Moral Foundation: {dominant}

Audience Interpretation:
{foundation_analysis[dominant]}

Campaign Strategy:
{campaign_strategy_text}

Example Message:
{example_messages[dominant]}
"""

    st.download_button(
        "Download Full Report",
        report,
        file_name="baamt_report.txt",
        mime="text/plain"
    )
