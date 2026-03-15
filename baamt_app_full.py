import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import textwrap

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("Behaviourally-Adaptive Advocacy Messaging Tool (BAAMT)")

st.write(
"""
BAAMT helps advocates design more effective communication strategies by
understanding how different audiences respond to moral and behavioural
arguments. The tool draws on insights from **Moral Foundations Theory** and
behavioural science research to identify which kinds of narratives are most
likely to resonate with different groups.

By answering a short set of questions about the audience you are engaging,
the tool generates a structured advocacy strategy that explains how messaging
can be framed to maximise impact while remaining credible and constructive.
"""
)

st.divider()

st.header("Audience Context")

st.info(
"""
Before answering the questions below, think about **a specific audience you
are trying to influence**. This might be policymakers, the general public,
industry stakeholders, students, or civil society organisations.

Your answers should reflect **how you believe this audience would respond**
to the statements below. The goal is not to measure personal beliefs but to
approximate the values and moral intuitions that shape how this audience
interprets advocacy messages.
"""
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    audience = st.selectbox(
        "Audience Type",
        ["General Public", "Policy Makers", "Industry", "NGOs", "Academics"]
    )

with col2:
    geography = st.selectbox(
        "Geographic Context",
        ["Global", "North America", "Europe", "India", "Asia-Pacific"]
    )

with col3:
    stakeholder = st.selectbox(
        "Primary Stakeholder",
        ["Government", "Corporate actors", "Civil society", "Researchers"]
    )

with col4:
    campaign = st.selectbox(
        "Campaign Objective",
        ["Policy reform", "Corporate change", "Public awareness", "Movement building"]
    )

st.divider()

st.header("Audience Value Assessment")

questions = {
"care": "This audience is likely to respond strongly to arguments about reducing suffering and protecting vulnerable beings.",
"fairness": "This audience tends to care about fairness, justice, and whether systems treat people or animals equitably.",
"loyalty": "This audience often evaluates issues based on how they affect communities, identities, or collective interests.",
"authority": "This audience tends to respect institutions and expects social problems to be addressed through responsible governance.",
"purity": "This audience is likely to respond to arguments about moral integrity, naturalness, or protecting social values."
}

scores = {}

for key, q in questions.items():
    scores[key] = st.slider(q,1,5,3)

st.divider()

if st.button("Generate BAAMT Strategy Report"):

    st.progress(100)

    care=scores["care"]
    fairness=scores["fairness"]
    loyalty=scores["loyalty"]
    authority=scores["authority"]
    purity=scores["purity"]

    st.header("1️⃣ Audience Moral Profile")

    profile=f"""
This audience profile suggests that moral intuitions related to compassion,
fairness, community identity, institutional responsibility, and moral values
all play some role in shaping how messages will be interpreted.

Understanding which of these moral foundations is most influential helps
advocates decide whether communication strategies should emphasise harm
reduction, justice and fairness, community well-being, institutional reform,
or the preservation of ethical and cultural values.
"""

    st.write(profile)

    st.header("2️⃣ Moral Foundations Radar Chart")

    labels=list(scores.keys())
    values=list(scores.values())

    angles=np.linspace(0,2*np.pi,len(labels),endpoint=False)
    values=np.concatenate((values,[values[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    fig=plt.figure()
    ax=fig.add_subplot(111,polar=True)

    ax.plot(angles,values)
    ax.fill(angles,values,alpha=0.1)

    ax.set_thetagrids(angles[:-1]*180/np.pi,labels)

    st.pyplot(fig)

    st.divider()

    st.header("3️⃣ Behavioural Segment")

    if care>4:
        segment="""
This audience shows a strong compassion-oriented moral profile. People in
this group are particularly responsive to arguments that highlight suffering,
harm, and the ethical responsibility to protect vulnerable beings.

Advocacy campaigns targeting this audience should therefore prioritise
clear explanations of the real-world consequences of harmful systems.
Narratives that highlight how reforms can directly reduce suffering or
prevent harm are likely to resonate strongly.

Using storytelling, case studies, and examples of real individuals or
animals affected by harmful practices can make the issue more concrete
and emotionally meaningful for this audience.
"""
    elif authority>4:
        segment="""
This audience places significant importance on institutions, governance,
and structured approaches to solving social problems.

People with this orientation tend to believe that lasting change occurs
through responsible policy reform, improved regulation, and credible
institutional leadership.

Advocacy strategies should therefore focus on demonstrating how proposed
changes would strengthen systems, improve oversight, and help institutions
perform their responsibilities more effectively.
"""
    elif loyalty>4:
        segment="""
This audience tends to interpret issues through the lens of community
identity and collective well-being.

Messaging strategies should therefore emphasise how reforms support
shared values, protect communities, and contribute to the long-term
stability and prosperity of society.

Campaigns should avoid framing issues in a way that appears to attack
community traditions. Instead, advocates can emphasise how improvements
strengthen communities and reinforce positive social norms.
"""
    else:
        segment="""
This audience appears to have a relatively balanced moral profile,
meaning that different individuals within the group may respond to
different types of arguments.

Advocacy campaigns targeting such audiences should therefore combine
multiple narrative approaches. Messages can highlight harm reduction,
fairness, responsible governance, and community benefits so that
different segments of the audience find aspects of the message
personally meaningful.
"""

    st.write(segment)

    st.header("4️⃣ Reform Orientation")

    if authority>3.5:
        reform="""
The responses suggest that this audience is relatively comfortable with
institutional approaches to change. Rather than seeking radical disruption,
people in this group generally believe that social systems can be improved
through responsible leadership, better regulation, and incremental reform.

Advocacy messaging should therefore emphasise practical policy solutions,
credible governance mechanisms, and realistic implementation pathways.
"""
    else:
        reform="""
This audience may be more open to questioning whether existing systems
are functioning effectively. People with this orientation are sometimes
receptive to stronger critiques of the status quo and may support more
transformative reforms if the case for change is clearly articulated.

Advocacy campaigns can therefore speak more directly about structural
problems while still explaining how reforms would work in practice.
"""

    st.write(reform)

    st.header("5️⃣ Risk Sensitivity Profile")

    if purity>4:
        risk="""
This audience shows relatively high sensitivity to moral or cultural risk.
People in this group may worry that social change could undermine
important traditions or long-standing ethical values.

Advocacy messaging should therefore emphasise stability and responsibility,
explaining clearly how reforms protect important values while improving
outcomes.
"""
    else:
        risk="""
This audience does not appear highly sensitive to moral risk associated
with social change. Messaging can therefore focus more directly on
evidence, impact, and practical solutions without needing extensive
reassurance about social stability.
"""

    st.write(risk)

    st.header("6️⃣ Institutional Trust Orientation")

    trust="""
The results suggest that institutional credibility will play an important
role in how advocacy messages are interpreted. Audiences often rely on
trusted organisations, researchers, and public institutions when deciding
whether to accept new information about complex social issues.

Campaigns should therefore highlight credible evidence, respected
institutions, and authoritative sources when presenting policy proposals
or recommendations.
"""

    st.write(trust)

    st.header("7️⃣ Primary Advocacy Lever")

    lever="""
The most effective advocacy lever for this audience is likely to involve
combining ethical arguments with practical policy solutions. Messages
should demonstrate both the moral importance of the issue and the
feasibility of addressing it through responsible action.

Advocates should focus on solutions that appear achievable, credible,
and aligned with widely shared social goals.
"""

    st.write(lever)

    st.header("8️⃣ Geographic Messaging Adjustment")

    geo=f"""
Advocacy messaging may need to be adapted to reflect the political,
economic, and cultural context of **{geography}**.

Different regions have distinct institutional structures, regulatory
frameworks, and public narratives about social change. Campaigns should
therefore consider how local institutions, cultural norms, and policy
priorities shape the way messages will be received.
"""

    st.write(geo)

    st.header("9️⃣ Campaign Strategy Plan")

    strategy="""
A successful campaign targeting this audience should combine credible
evidence with clear explanations of how reforms can improve outcomes.

Communication should emphasise both the ethical importance of the issue
and the practical feasibility of implementing solutions. This often
requires combining research evidence, policy analysis, and real-world
examples to demonstrate why change is necessary and achievable.
"""

    st.write(strategy)

    st.header("🔟 Full Advocacy Strategy Brief")

    brief="""
Taken together, these results suggest that effective advocacy for this
audience should combine moral clarity with credible institutional
solutions.

Campaigns should avoid abstract moral debates and instead focus on
practical improvements that clearly reduce harm, strengthen governance,
and contribute to broader social well-being.
"""

    st.write(brief)

    st.divider()
    # ---------- ADVANCED STRATEGY MODULE ----------

st.header("11️⃣ Message Framing Examples")

framing = f"""
Based on the moral profile identified earlier, several message framing
approaches are likely to resonate with this audience.

If compassion-oriented arguments are influential, messaging should focus
on clearly explaining the real-world harms caused by existing systems and
how practical reforms could reduce suffering.

If fairness concerns are present, advocates can emphasise how reforms
correct systemic imbalances and ensure that responsibilities and benefits
are distributed more equitably across society.

Where institutional values are important, it can be effective to frame
proposals as strengthening governance systems and helping public
institutions fulfil their responsibilities more effectively.

Advocates should test multiple framing approaches to identify which
combination of ethical, economic, and institutional narratives produces
the strongest engagement with the target audience.
"""

st.write(framing)


st.header("12️⃣ Coalition Strategy")

coalition = f"""
Advocacy campaigns are often more effective when they are supported by
diverse coalitions rather than single organisations acting alone.

For this campaign context involving **{stakeholder}**, potential coalition
partners may include research organisations, civil society groups,
policy experts, and institutions that already have credibility with
the target audience.

Coalitions can increase legitimacy, expand communication reach, and
demonstrate that the proposed reforms are supported by a broad range of
stakeholders rather than representing the agenda of a single advocacy
organisation.

Where possible, advocates should identify partners that bring different
strengths, such as technical expertise, policy credibility, public
visibility, or grassroots mobilisation capacity.
"""

st.write(coalition)


st.header("13️⃣ Policy Pathway")

policy = f"""
Successful advocacy campaigns often require a clear pathway from
problem identification to policy adoption.

For a campaign focused on **{campaign}**, the pathway may involve
several stages including agenda setting, policy development,
stakeholder consultation, and formal institutional adoption.

Advocates should identify key decision-makers, understand the
institutional processes through which policy change occurs,
and develop strategies to introduce evidence and recommendations
at the moments when they are most likely to influence outcomes.

This often involves engaging both technical experts and
political stakeholders to ensure that proposals are seen as
credible, practical, and politically feasible.
"""

st.write(policy)


st.header("14️⃣ Opposition Risk Analysis")

risk_analysis = """
Advocacy campaigns should anticipate potential sources of resistance
or opposition. These may come from stakeholders with economic
interests in maintaining the status quo, institutional actors who
are cautious about regulatory change, or audience segments that
perceive reforms as threatening cultural or social norms.

Understanding these concerns in advance allows advocates to design
messages that address fears, clarify misconceptions, and emphasise
the broader benefits of reform.

Effective campaigns do not simply present arguments for change;
they also proactively engage with the concerns of critics and
demonstrate that proposed solutions are responsible, balanced,
and beneficial for society as a whole.
"""

st.write(risk_analysis)

st.divider()

    # ---------- FORMATTED PDF REPORT ----------

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)

    def add_section(title,text):

        pdf.ln(4)
        pdf.set_font("Arial","B",12)
        pdf.cell(0,8,title,ln=True)

        pdf.set_font("Arial","",11)

        wrapped=textwrap.wrap(text,90)

        for line in wrapped:
            pdf.cell(0,7,line,ln=True)

    pdf.set_font("Arial","B",16)
       if st.button("Generate BAAMT Strategy Report"):

    # 1. Behavioural Segment
    st.subheader("Behavioural Segment")
    st.write(segment)

    # 2. Reform Orientation
    st.subheader("Reform Orientation")
    st.write(reform)

    # ... other sections ...

    st.divider()

    # ---------- FORMATTED PDF REPORT ----------
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    def add_section(title, text):
        pdf.ln(4)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, title, ln=True)
        pdf.set_font("Arial", "", 11)
        wrapped = textwrap.wrap(text, 90)
        for line in wrapped:
            pdf.cell(0, 7, line, ln=True)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Audience: {audience}", ln=True)
    pdf.cell(0, 8, f"Geography: {geography}", ln=True)
    pdf.cell(0, 8, f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(0, 8, f"Campaign Objective: {campaign}", ln=True)

    add_section("Behavioural Segment", segment)
    add_section("Reform Orientation", reform)
    add_section("Risk Sensitivity Profile", risk)
    add_section("Institutional Trust Orientation", trust)
    add_section("Primary Advocacy Lever", lever)
    add_section("Geographic Messaging Adjustment", geo)
    add_section("Campaign Strategy Plan", strategy)
    add_section("Advocacy Strategy Brief", brief)

    add_section("Message Framing Examples", framing)
    add_section("Coalition Strategy", coalition)
    add_section("Policy Pathway", policy)
    add_section("Opposition Risk Analysis", risk_analysis)

    pdf_bytes = bytes(pdf.output(dest="S"))

    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )
