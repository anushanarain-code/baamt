import streamlit as st

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("BAAMT – Behavioural Advocacy and Messaging Tool")

st.write(
"BAAMT is a behavioural analysis tool designed to help advocacy organisations, "
"policy researchers, and campaigners understand how different audiences may "
"interpret advocacy messaging. The tool combines insights from behavioural "
"science and moral psychology to generate strategic guidance for designing "
"more effective advocacy campaigns."
)

# ---------------------------------------------------
# Audience Context
# ---------------------------------------------------

st.header("Audience Context")

st.markdown("""
Select the context in which your advocacy campaign operates.

These contextual variables shape how advocacy messages are interpreted
and help generate a more accurate strategic assessment.

**Audience Type** – The primary group whose attitudes or behaviour the campaign seeks to influence.  
**Geography** – The political and institutional environment in which advocacy occurs.  
**Stakeholder Type** – Actors who influence policy discourse or public opinion.  
**Campaign Type** – The strategic objective of the campaign.
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
# Behavioural Questionnaire
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

Your responses help estimate which **moral foundations** are most influential
for this audience. The tool then combines this moral profile with the selected
audience and campaign context to generate advocacy insights.
""")

questions = {

"Care1":"Public policies should prioritise reducing suffering whenever possible.",
"Care2":"Protecting vulnerable groups should be a central goal of social policy.",

"Fairness1":"Justice and fairness should guide policy decisions even when trade-offs exist.",
"Fairness2":"Systems should ensure that everyone is treated equally under the rules.",

"Authority1":"Respect for institutions is important for maintaining social stability.",
"Authority2":"Policies should reinforce trust in established institutions.",

"Loyalty1":"People should feel a strong responsibility toward their community.",
"Loyalty2":"Supporting one's social group is an important moral value.",

"Purity1":"Society should uphold strong ethical standards in public life.",
"Purity2":"Maintaining moral integrity is essential for a healthy society."
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
# Audience Profile Analysis
# ---------------------------------------------------

foundation_analysis = {

"Care":
"""The responses indicate that compassion and harm reduction are likely to be
central moral considerations for this audience. When audiences prioritise the
Care foundation, they tend to respond strongly to narratives that highlight
the real-world consequences of suffering and vulnerability. Advocacy messages
that illustrate how policy choices affect individuals, communities, or animals
in tangible ways are therefore more likely to resonate. When combined with the
selected audience profile and campaign context, this moral orientation suggests
that persuasive communication should emphasise empathy, responsibility, and
the possibility of reducing harm through practical reforms.""",

"Fairness":
"""The responses suggest that the audience evaluates issues strongly through
the lens of justice and equitable treatment. Audiences with a fairness-oriented
profile often assess policies by asking whether systems distribute costs and
benefits in a balanced way. Advocacy campaigns targeting such audiences tend
to be most effective when they highlight hidden inequities or structural
imbalances and present reforms as mechanisms that restore fairness and
transparency within institutions and markets.""",

"Authority":
"""This profile indicates that respect for institutions and social order
plays an important role in shaping the audience's moral reasoning.
Individuals with a strong authority orientation often respond positively
to arguments that emphasise responsible governance, effective regulation,
and institutional credibility. Advocacy strategies directed at this
audience are therefore likely to be most persuasive when reforms are framed
as strengthening systems and improving oversight rather than disrupting
existing structures.""",

"Loyalty":
"""The responses suggest that collective identity and community solidarity
are influential considerations for this audience. Individuals who prioritise
loyalty often interpret policy debates through the lens of shared values
and group wellbeing. Advocacy messaging that highlights the collective
benefits of reform and frames change as protecting the interests of the
community can therefore be particularly effective.""",

"Purity":
"""This profile indicates that ethical integrity and moral responsibility
play an important role in how the audience evaluates social issues.
Purity-oriented audiences often respond strongly to arguments that frame
issues in terms of ethical standards, moral accountability, and the need
to uphold societal values. Advocacy campaigns targeting such audiences
may therefore benefit from emphasising integrity, responsibility, and the
ethical implications of policy decisions."""
}

# ---------------------------------------------------
# Reform Orientation
# ---------------------------------------------------

avg_score = sum(foundation_scores.values())/5

if avg_score >=4:
    reform_orientation = """
The response pattern suggests that the audience may be relatively open to
substantial reform when those reforms are presented as morally justified
and socially beneficial. This indicates a potential receptiveness to
system-level changes provided that they are framed in ways that align with
the audience's moral priorities and institutional expectations.
"""
else:
    reform_orientation = """
The overall response pattern suggests that the audience may prefer gradual
or incremental reforms rather than disruptive policy shifts. Advocacy
strategies may therefore benefit from presenting reforms as practical
improvements that build upon existing systems rather than replacing them
entirely.
"""

# ---------------------------------------------------
# Risk Profile
# ---------------------------------------------------

risk_profile = f"""
The behavioural profile generated by this assessment suggests several
strategic risks that advocacy campaigns should consider. First, messaging
that conflicts with the audience's dominant moral foundation ({dominant})
may be perceived as unconvincing or ideologically biased. Second, campaigns
that rely solely on technical evidence without addressing underlying moral
concerns may fail to engage the audience's intuitive reasoning processes.
Finally, if the proposed reforms appear overly disruptive relative to the
audience's reform orientation, the campaign may encounter resistance even
among individuals who broadly agree with the underlying goals. Recognising
these risks allows advocacy strategies to anticipate potential objections
and design narratives that maintain credibility while gradually building
support for change.
"""

# ---------------------------------------------------
# Messaging Strategy
# ---------------------------------------------------

messaging_strategy = f"""
The messaging strategy suggested by BAAMT emerges from the interaction
between three analytical dimensions: the **dominant moral foundation
identified in the questionnaire ({dominant})**, the **audience profile
selected at the beginning of the assessment ({audience})**, and the
**campaign objective ({campaign})**.

Because the dominant moral foundation in this case is **{dominant}**,
advocacy narratives should foreground themes that resonate with this
moral priority. However, effective advocacy rarely depends on a single
dimension alone. Instead, persuasive campaigns align moral framing with
audience expectations and institutional realities.

For the selected audience group, this means that messages should not only
reflect the values associated with the {dominant} foundation but also
connect those values to concrete policy choices, behavioural practices,
or institutional reforms. The campaign context further shapes the tone
and emphasis of the messaging strategy. Behaviour change campaigns may
focus on individual choices and social norms, while policy advocacy
campaigns may highlight regulatory solutions, governance mechanisms,
and institutional accountability.

In practice, this integrated strategy encourages advocates to combine
ethical framing with credible evidence and relatable examples. By doing
so, campaigns can speak simultaneously to the audience's intuitive moral
concerns and their practical expectations about how social change occurs.
"""

# ---------------------------------------------------
# Example Messaging
# ---------------------------------------------------

example_messages = {

"Care":
"Policy reforms can significantly reduce suffering and create a more compassionate society. By supporting responsible changes today, we can protect vulnerable populations while building systems that reflect our shared commitment to wellbeing.",

"Fairness":
"A fair system ensures that responsibilities are shared and that hidden costs are not passed on to society. Transparent policies help create institutions that reward ethical practices rather than exploit vulnerabilities.",

"Authority":
"Strong institutions depend on clear standards and responsible governance. Strengthening oversight ensures that systems operate with integrity and maintain public trust.",

"Loyalty":
"Our communities thrive when we work together to protect shared values. Responsible reforms help ensure that social systems continue to serve the collective interests of society.",

"Purity":
"Societies are judged by the standards they uphold. Ensuring ethical responsibility in policy and industry helps maintain the moral integrity of our institutions."
}

# ---------------------------------------------------
# Generate Report
# ---------------------------------------------------

if st.button("Generate Report"):

    st.header("Audience Profile Analysis")
    st.write(foundation_analysis[dominant])

    st.header("Reform Orientation")
    st.write(reform_orientation)

    st.header("Risk Profile")
    st.write(risk_profile)

    st.header("Messaging Strategy")
    st.write(messaging_strategy)

    st.header("Example Advocacy Messaging")
    st.write(example_messages[dominant])

    report = f"""
BAAMT Advocacy Analysis

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign Type: {campaign}

Dominant Moral Foundation: {dominant}

Audience Profile Analysis:
{foundation_analysis[dominant]}

Reform Orientation:
{reform_orientation}

Risk Profile:
{risk_profile}

Messaging Strategy:
{messaging_strategy}

Example Message:
{example_messages[dominant]}
"""

    st.download_button(
        "Download Full Report",
        report,
        file_name="baamt_report.txt",
        mime="text/plain"
    )
