import streamlit as st

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("BAAMT – Behavioural Advocacy and Messaging Tool")

st.write(
"BAAMT is a behavioural analysis tool designed to help advocacy organizations, "
"policy researchers, and social campaigners better understand how different audiences "
"may respond to advocacy messaging. The tool draws on behavioural science, moral "
"psychology, and strategic communication research to generate insights that can "
"inform the design of more effective advocacy campaigns."
)

# ---------------------------------------------------
# Audience Context
# ---------------------------------------------------

st.markdown("""
### Audience Context

Select the campaign environment in which you are working.  
These contextual factors shape how advocacy messages are interpreted.

• **Audience Type** – the primary group whose attitudes or behaviour the campaign seeks to influence  
• **Geography** – the political and regulatory environment in which the campaign takes place  
• **Stakeholder Type** – actors who influence discourse or decision-making  
• **Campaign Type** – the overall strategy of the advocacy intervention
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
# Context Explanations
# ---------------------------------------------------

audience_explanations = {

"General Public":
"""The general public represents a broad and diverse audience whose everyday behaviour,
consumption choices, and voting preferences collectively shape both market demand and
political incentives. Advocacy campaigns targeting the general public often succeed
when complex issues are translated into clear narratives that connect directly with
daily life. Messages that combine moral clarity with relatable examples tend to
perform better than those that rely purely on technical explanations. Effective
campaigns therefore focus on helping people understand how individual choices
connect to larger societal outcomes.""",

"Policy Makers":
"""Policy makers are institutional actors who possess the authority to design,
interpret, or implement regulations and laws. Advocacy efforts directed toward
this audience tend to be most effective when grounded in credible evidence,
policy feasibility, and clear explanations of regulatory implications.
Policy makers often operate under constraints such as political feasibility,
budgetary limitations, and administrative capacity, so messages that combine
ethical arguments with practical solutions are particularly persuasive.""",

"Professionals":
"""Professional audiences include scientists, industry actors, regulators,
and subject-matter experts who influence technical debates and policy design.
Advocacy campaigns targeting professional audiences often need to emphasize
credibility, empirical evidence, and methodological transparency. Messages
should demonstrate a clear understanding of professional norms and industry
realities while also presenting compelling reasons for change.""",

"Youth":
"""Younger audiences frequently demonstrate strong engagement with
future-oriented ethical narratives and social justice issues.
Advocacy campaigns targeting youth audiences often benefit from
emphasizing intergenerational responsibility, long-term societal
impacts, and the role that collective action can play in shaping
the future. Youth campaigns are also more likely to spread through
peer networks and digital media environments."""
}

geography_explanations = {

"India":
"""Advocacy campaigns in India operate within a highly diverse social
and political landscape. Federal governance structures mean that
policy authority is distributed across national and state levels,
while cultural diversity shapes how messages are interpreted across
different communities. Successful advocacy in India often combines
national-level policy framing with locally resonant narratives that
connect reforms to everyday social realities.""",

"Global":
"""Global advocacy efforts typically operate across multiple political
and cultural contexts simultaneously. Campaigns often rely on
international institutions, multinational corporations, and
transnational civil society networks to drive change. Messages
must therefore balance universal ethical principles with sensitivity
to regional differences.""",

"Europe":
"""European advocacy environments often emphasize precaution,
sustainability, and regulatory accountability. Campaigns frequently
engage with strong institutional frameworks and well-developed
policy consultation processes.""",

"USA":
"""Advocacy campaigns in the United States operate within a highly
visible and often polarized public discourse environment.
Messages that resonate tend to combine moral narratives with
clear demonstrations of economic and social impact."""
}

stakeholder_explanations = {

"General Public":
"""The broader population plays a critical role in shaping both
political legitimacy and economic demand. Even when policy
decisions are made by institutions, public opinion can strongly
influence the range of politically viable options available to
decision-makers.""",

"Community Leaders":
"""Community leaders often serve as intermediaries who translate
complex issues into locally meaningful narratives. Their support
can significantly increase the credibility and reach of advocacy
campaigns within specific communities.""",

"Organizations":
"""Organizations such as NGOs, corporations, professional
associations, and advocacy networks can shape institutional
practices, industry standards, and policy debates."""
}

campaign_explanations = {

"Behaviour Change":
"""Behaviour change campaigns aim to influence everyday choices,
habits, or social norms. These campaigns typically rely on
clear messaging, practical alternatives, and social norm
reinforcement to encourage individuals to adopt new behaviours.""",

"Policy Advocacy":
"""Policy advocacy campaigns focus on influencing legislation,
regulatory frameworks, or institutional decisions. Effective
campaigns combine ethical arguments with credible evidence,
stakeholder coalitions, and feasible policy proposals.""",

"Awareness Campaign":
"""Awareness campaigns seek to increase visibility and public
understanding of an issue. These campaigns are often the first
stage of broader advocacy strategies."""
}

# ---------------------------------------------------
# Questionnaire
# ---------------------------------------------------

st.markdown("""
### Behavioural Questionnaire

Rate each statement from **1 (Strongly Disagree)** to **5 (Strongly Agree)**.
""")

questions = {
"Care":"Reducing suffering should be a major priority when making public decisions.",
"Fairness":"Justice and fairness should guide policy even when economic trade-offs are involved.",
"Authority":"Societies function best when institutions and leadership structures are respected.",
"Loyalty":"Protecting one's community and social group is an important moral obligation.",
"Purity":"Maintaining ethical integrity and moral boundaries is essential for a healthy society."
}

scores = {}

for k,q in questions.items():
    scores[k] = st.slider(q,1,5,3)

dominant = max(scores, key=scores.get)

# ---------------------------------------------------
# Moral Foundation Analysis
# ---------------------------------------------------

foundation_analysis = {

"Care":
"""This profile suggests that the audience places significant
importance on compassion, harm reduction, and the protection
of vulnerable populations. Messages that highlight the real-world
consequences of suffering, environmental harm, or social injustice
are likely to resonate strongly. Advocacy campaigns targeting this
moral orientation often benefit from storytelling, case studies,
and concrete examples that make the impact of policy decisions
visible and emotionally meaningful.""",

"Fairness":
"""Audiences with a strong fairness orientation tend to evaluate
issues through the lens of justice, equality, and ethical treatment.
They are often responsive to arguments that emphasize fairness in
markets, institutions, or social systems. Advocacy messaging that
highlights inequities, systemic bias, or unjust outcomes can be
particularly persuasive when framed as opportunities to create a
more balanced and accountable system.""",

"Authority":
"""A strong authority orientation suggests that audiences value
institutional stability, social order, and legitimate leadership.
Advocacy strategies targeting such audiences often perform best
when reforms are framed as strengthening institutions rather than
challenging them.""",

"Loyalty":
"""Audiences with a strong loyalty orientation are particularly
sensitive to narratives related to group identity, solidarity,
and shared responsibility. Advocacy campaigns may therefore
benefit from emphasizing collective benefits and community pride.""",

"Purity":
"""A strong purity orientation indicates sensitivity to moral
boundaries and ethical integrity. Advocacy messages that frame
issues in terms of ethical responsibility and moral consequences
can resonate particularly strongly."""
}

# ---------------------------------------------------
# Strategic Profiles
# ---------------------------------------------------

avg_score = sum(scores.values())/len(scores)

if avg_score >=4:
    reform_orientation = """The overall response pattern suggests
that this audience may be relatively open to ambitious reforms
when those reforms are presented as morally justified and socially
beneficial."""
else:
    reform_orientation = """The response pattern indicates that
incremental reforms and gradual policy transitions may be more
effective than disruptive proposals."""

risk_profile = """Based on the distribution of responses across the
moral foundations profile, this audience appears moderately cautious
but responsive to credible evidence and well-structured arguments.
Advocacy efforts may therefore benefit from presenting change as
both ethically desirable and practically achievable."""

campaign_strategy = """A promising campaign strategy would combine
clear ethical framing with credible evidence and relatable narratives.
Messages should connect the issue to everyday experiences while also
demonstrating how proposed reforms align with widely held values."""

advocacy_lever = """Potential advocacy levers include coalition-building
with credible institutions, collaboration with trusted community
voices, and strategic use of media narratives that reinforce the
moral significance of the issue."""

# ---------------------------------------------------
# Example Messaging
# ---------------------------------------------------

example_messages = {

"Care":
"""Example message:  
'Every day, policy decisions shape the lives of millions of
sentient beings. By supporting humane and sustainable reforms,
we can significantly reduce suffering while building a more
compassionate society for future generations.'""",

"Fairness":
"""Example message:  
'A fair system ensures that the costs of production are not hidden
from society. By creating transparent and responsible policies,
we can ensure that markets reward ethical practices rather than
exploiting vulnerable populations.'""",

"Authority":
"""Example message:  
'Strong institutions depend on responsible governance.
By strengthening regulatory oversight and ensuring that
standards are upheld, policy makers can protect both
citizens and markets.'""",

"Loyalty":
"""Example message:  
'Our communities thrive when we look out for one another.
Supporting responsible reforms helps ensure that our
collective values are reflected in the systems that
shape our future.'""",

"Purity":
"""Example message:  
'A society's integrity is reflected in how it treats the
most vulnerable. Upholding ethical standards in policy
and industry ensures that our progress does not come
at the cost of our moral principles.'"""
}

# ---------------------------------------------------
# Generate Report
# ---------------------------------------------------

if st.button("Generate Report"):

    st.header("Audience Context")
    st.write(audience_explanations[audience])
    st.write(geography_explanations[geography])
    st.write(stakeholder_explanations[stakeholder])
    st.write(campaign_explanations[campaign])

    st.header("Moral Foundations Analysis")
    st.write(foundation_analysis[dominant])

    st.header("Reform Orientation")
    st.write(reform_orientation)

    st.header("Risk Profile")
    st.write(risk_profile)

    st.header("Campaign Strategy")
    st.write(campaign_strategy)

    st.header("Advocacy Lever")
    st.write(advocacy_lever)

    st.header("Example Advocacy Messaging")
    st.write(example_messages[dominant])

    summary = f"""
BAAMT Behavioural Advocacy Analysis

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign Type: {campaign}

Dominant Moral Foundation: {dominant}

Strategic Interpretation:
{foundation_analysis[dominant]}

Reform Orientation:
{reform_orientation}

Risk Profile:
{risk_profile}

Campaign Strategy:
{campaign_strategy}

Advocacy Lever:
{advocacy_lever}

Example Advocacy Message:
{example_messages[dominant]}
"""

    st.download_button(
        "Download Full Report",
        data=summary,
        file_name="baamt_report.txt",
        mime="text/plain"
    )
