import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import tempfile

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")

st.write("""
BAAMT helps advocacy organisations design evidence-based messaging strategies
by analysing the moral values and behavioural orientations of different audiences.

The tool integrates insights from behavioural science, political psychology,
and public policy research to help advocates design more effective campaigns
for social change and institutional reform.
""")

st.markdown("---")

st.header("Theoretical Framework")

st.write(f"""
This tool draws on insights from **Moral Foundations Theory**, a framework in
moral psychology that proposes that human moral reasoning is structured around
several core intuitive foundations. These include concerns about harm and care,
fairness and justice, authority and institutional order, loyalty to social
groups, and ideas of purity or moral integrity.

Understanding how strongly an audience responds to each of these moral
dimensions can help advocacy organisations design messages that resonate more
deeply with the values and expectations of the people they are trying to
persuade.

BAAMT also incorporates ideas from behavioural economics and political
communication research, recognising that advocacy messages are more effective
when they align with existing moral intuitions, institutional trust patterns,
and perceptions of social risk.
""")

st.markdown("---")

# Audience Context
st.header("Audience Context")

audience = st.selectbox(
"Target Audience",
[
"General Public",
"Students and Young People",
"Policy Makers",
"Industry Stakeholders",
"Civil Society Organisations"
]
)

geography = st.selectbox(
"Geographic Context",
[
"India",
"Global",
"Europe",
"North America",
"Southeast Asia"
]
)

stakeholder = st.selectbox(
"Primary Stakeholder Engagement",
[
"Government Institutions",
"Corporate Actors",
"Civil Society",
"Consumers"
]
)

campaign = st.selectbox(
"Primary Campaign Objective",
[
"Behaviour Change",
"Policy Reform",
"Corporate Engagement",
"Public Awareness"
]
)

st.markdown("---")

# Assessment
st.header("Behavioural Assessment")

st.write("Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree).")

care1 = st.slider("Preventing suffering should be a central priority in public policy decisions.",1,5,3)
fair1 = st.slider("Economic systems should prioritise fairness even when doing so involves financial trade-offs.",1,5,3)
auth1 = st.slider("Societies function best when people respect institutions, laws, and established authority.",1,5,3)
loyal1 = st.slider("People should show loyalty to their community and social groups when making political decisions.",1,5,3)
pure1 = st.slider("Ideas of moral purity and social cleanliness are important to maintaining a healthy society.",1,5,3)

care2 = st.slider("Avoiding harm to vulnerable beings is an ethical responsibility for society.",1,5,3)
auth2 = st.slider("Rules and laws should generally be followed even when doing so may be inconvenient.",1,5,3)
fair2 = st.slider("Markets and economic institutions should be structured to ensure fairness.",1,5,3)
loyal2 = st.slider("Communities should actively protect their cultural traditions and shared values.",1,5,3)
pure2 = st.slider("Some practices are morally wrong regardless of their economic or practical consequences.",1,5,3)

st.markdown("---")

if st.button("Generate Advocacy Report"):

    care=(care1+care2)/2
    fairness=(fair1+fair2)/2
    authority=(auth1+auth2)/2
    loyalty=(loyal1+loyal2)/2
    purity=(pure1+pure2)/2

    st.header("1️⃣ Audience Moral Profile")

    scores={
    "Care":care,
    "Fairness":fairness,
    "Authority":authority,
    "Loyalty":loyalty,
    "Purity":purity
    }

    for k,v in scores.items():
        st.write(f"{k}: {round(v,2)}")

    st.header("2️⃣ Moral Foundations Radar Chart")

    labels=list(scores.keys())
    values=list(scores.values())
    values+=values[:1]

    angles=[n/float(len(labels))*2*3.14159 for n in range(len(labels))]
    angles+=angles[:1]

    fig=plt.figure()
    ax=fig.add_subplot(111,polar=True)
    ax.plot(angles,values)
    ax.fill(angles,values,alpha=0.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    st.pyplot(fig)

    st.header("3️⃣ Behavioural Segment")

    if care>4:
        segment="Compassion-oriented audiences who respond strongly to narratives emphasising suffering, empathy, and ethical responsibility."
    elif authority>4:
        segment="Institutionally aligned audiences who place strong value on stability, rules, and the legitimacy of established governance structures."
    elif loyalty>4:
        segment="Community-centred audiences who prioritise collective identity, social belonging, and cultural continuity."
    else:
        segment="Mixed moral audiences whose responses are likely to depend on contextual framing and coalition-based messaging."

    st.write(segment)

    st.header("4️⃣ Reform Orientation")

    if authority>3.5:
        reform="This audience is likely to favour gradual and institutional pathways to reform, meaning that advocacy efforts should emphasise responsible governance, regulatory improvement, and credible institutional leadership."
    else:
        reform="This audience may be receptive to more transformative or disruptive advocacy narratives that challenge existing systems and emphasise the need for deeper social change."

    st.write(reform)

    st.header("5️⃣ Risk Sensitivity Profile")

    if purity>4:
        risk="High sensitivity to moral or cultural risk. Messaging should acknowledge perceived threats to social norms and present reforms as morally responsible improvements rather than radical disruptions."
    else:
        risk="Moderate sensitivity to moral risk. Advocacy messaging can focus more directly on empirical evidence, harm reduction, and social progress narratives."

    st.write(risk)

    st.header("6️⃣ Institutional Trust Orientation")

    if authority+loyalty>7:
        trust="High institutional trust. Advocacy strategies should prioritise engagement with policy institutions, regulatory bodies, and formal governance channels."
    else:
        trust="Moderate or limited institutional trust. Advocacy may need to rely more heavily on public mobilisation, civil society partnerships, and social norm change."

    st.write(trust)

    st.header("7️⃣ Primary Advocacy Lever")

    if care>4:
        lever="Compassion and harm-reduction framing that emphasises the ethical responsibility to reduce suffering."
    elif fairness>4:
        lever="Justice and fairness framing highlighting inequality, systemic bias, and moral accountability."
    elif authority>4:
        lever="Institutional responsibility framing focusing on governance standards and policy leadership."
    else:
        lever="Social norm change framing that highlights emerging ethical expectations and shifts in public values."

    st.write(lever)

    st.header("8️⃣ Geographic Messaging Adjustment")

    if geography=="India":
        geo="Advocacy communication should be attentive to cultural pluralism, respect for institutional authority, and the influence of community leadership within public discourse."
    elif geography=="Europe":
        geo="Messaging may emphasise regulatory standards, animal welfare norms, and ethical consumption patterns that are already embedded within public policy frameworks."
    else:
        geo="Messaging should emphasise universal ethical principles, sustainability narratives, and global governance frameworks."

    st.write(geo)

    st.header("9️⃣ Campaign Strategy Plan")

    strategy=f"""
An effective advocacy campaign for this audience should combine narrative
framing with credible evidence and coalition-building. Organisations should
focus on emphasising {lever.lower()} while building partnerships with
research institutions, civil society organisations, and influential public
voices.

Communication strategies should highlight both the ethical implications of
the issue and the practical pathways through which meaningful reform can
occur. Where possible, campaigns should also demonstrate how proposed
changes align with existing social values, economic incentives, and
institutional responsibilities.
"""

    st.write(strategy)

    st.header("🔟 Full Advocacy Strategy Brief")

    brief=f"""
Audience Context: {audience}

Geography: {geography}

Primary Stakeholder: {stakeholder}

Campaign Objective: {campaign}

The behavioural analysis suggests that this audience is best engaged through
{lever.lower()}. Advocacy messaging should frame the issue in ways that
acknowledge the moral intuitions of the audience while presenting clear
evidence that reform is both ethically necessary and socially beneficial.

Campaigns should prioritise credible messengers, partnerships with relevant
institutions, and strategic communication that emphasises achievable policy
pathways. Over time, sustained advocacy efforts should aim to shift public
norms while building the institutional conditions necessary for lasting
reform.
"""

    st.write(brief)

    # PDF
    report=f"""
BAAMT Advocacy Strategy Report

Audience: {audience}
Geography: {geography}
Stakeholder: {stakeholder}
Campaign Objective: {campaign}

Care: {care}
Fairness: {fairness}
Authority: {authority}
Loyalty: {loyalty}
Purity: {purity}

Behavioural Segment
{segment}

Reform Orientation
{reform}

Risk Sensitivity
{risk}

Institutional Trust
{trust}

Primary Advocacy Lever
{lever}

Geographic Messaging
{geo}

Campaign Strategy
{strategy}

Advocacy Strategy Brief
{brief}
"""

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=11)

    for line in report.split("\n"):
        pdf.multi_cell(0,8,line)

    tmp_file=tempfile.NamedTemporaryFile(delete=False,suffix=".pdf")
    pdf.output(tmp_file.name)

    with open(tmp_file.name,"rb") as f:
        st.download_button(
        label="Download BAAMT Report (PDF)",
        data=f,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
        )
