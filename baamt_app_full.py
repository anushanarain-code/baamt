import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

st.set_page_config(page_title="BAAMT", layout="wide")

st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")

st.write(
"""
BAAMT helps advocacy organisations design evidence-based messaging strategies 
based on the moral values and behavioural orientation of their target audiences.

The tool draws on behavioural science frameworks including Moral Foundations 
Theory, Social Norm Theory, and Prospect Theory to generate messaging guidance 
for advocacy campaigns.
"""
)

# -----------------------------
# Audience Context
# -----------------------------

st.header("Audience Context")

audience = st.selectbox(
"Select Target Audience",
["General Public","Policy Makers","Students","Industry Stakeholders"]
)

geography = st.selectbox(
"Select Geography",
["India","Global","Europe","North America"]
)

stakeholder = st.selectbox(
"Primary Stakeholder",
["Government","Civil Society","Private Sector","Consumers"]
)

campaign_type = st.selectbox(
"Campaign Objective",
["Behaviour Change","Policy Reform","Corporate Engagement","Public Awareness"]
)

# -----------------------------
# Moral Foundations Assessment
# -----------------------------

st.header("Behavioural Assessment")

st.write("Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree).")

care1 = st.slider("Preventing suffering should be a top priority in public policy.",1,5,3)
fair1 = st.slider("Fair treatment matters even if it requires economic trade-offs.",1,5,3)
auth1 = st.slider("Society functions best when people respect authority and institutions.",1,5,3)
loyal1 = st.slider("Loyalty to one's community should guide political decision-making.",1,5,3)
pure1 = st.slider("Purity and moral cleanliness are important social values.",1,5,3)
care2 = st.slider("Avoiding harm to vulnerable beings is an ethical responsibility.",1,5,3)
auth2 = st.slider("Rules and laws should be followed even when inconvenient.",1,5,3)
fair2 = st.slider("People should prioritise fairness in markets and economic systems.",1,5,3)
loyal2 = st.slider("Communities should protect their cultural traditions.",1,5,3)
pure2 = st.slider("Certain practices are morally wrong regardless of consequences.",1,5,3)

care = (care1 + care2) / 2
fair = (fair1 + fair2) / 2
auth = (auth1 + auth2) / 2
loyal = (loyal1 + loyal2) / 2
pure = (pure1 + pure2) / 2

# -----------------------------
# Behavioural Profiling
# -----------------------------

st.header("Audience Moral Profile")

scores = {
"Care":care,
"Fairness":fair,
"Authority":auth,
"Loyalty":loyal,
"Purity":pure
}

df = pd.DataFrame(dict(r=scores.values()),index=scores.keys())

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

labels = list(scores.keys())
values = list(scores.values())
values += values[:1]

angles = [n / float(len(labels)) * 2 * 3.14159 for n in range(len(labels))]
angles += angles[:1]

ax.plot(angles, values)
ax.fill(angles, values, alpha=0.1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

st.pyplot(fig)

for k,v in scores.items():
    st.write(f"{k}: {round(v,2)}")

# -----------------------------
# Behavioural Interpretation
# -----------------------------

st.header("Behavioural Analysis")

if care > 4:
    segment = "High empathy audience"
elif auth > 4:
    segment = "Institutionally oriented audience"
elif loyal > 4:
    segment = "Community identity audience"
else:
    segment = "Mixed moral audience"

st.write("Behavioural Segment:",segment)

# Reform orientation
if auth > 3.5:
    reform = "Incremental institutional reform is likely to be persuasive."
else:
    reform = "Disruptive or transformative advocacy may resonate more strongly."

st.write("Reform Orientation:",reform)

# Risk sensitivity
if pure > 4:
    risk = "High sensitivity to perceived moral or cultural risks."
else:
    risk = "Moderate sensitivity to moral risk framing."

st.write("Risk Profile:",risk)

# Institutional trust
if auth + loyal > 7:
    trust = "High institutional trust orientation."
else:
    trust = "Moderate or low institutional trust orientation."

st.write("Institutional Trust:",trust)

# -----------------------------
# Strategy Engine
# -----------------------------

st.header("Recommended Advocacy Strategy")

if care > 4:
    lever = "Compassion and harm reduction framing."
elif fair > 4:
    lever = "Justice and fairness framing."
elif auth > 4:
    lever = "Institutional responsibility framing."
else:
    lever = "Social norm change framing."

st.write("Primary Advocacy Lever:",lever)

# Geography adaptation

if geography == "India":
    geo_message = "Messaging should consider cultural values, community leadership, and institutional legitimacy."
elif geography == "Europe":
    geo_message = "Messaging can emphasise regulatory standards and ethical consumption norms."
else:
    geo_message = "Messaging should focus on universal ethical principles and global sustainability narratives."

st.write("Geographic Messaging Adjustment:",geo_message)

# Campaign strategy

strategy = f"""
Campaign strategy should combine narrative change with targeted institutional engagement.
Advocacy organisations should emphasise {lever.lower()} while building coalitions with
civil society organisations, research institutions, and policy stakeholders.

Communication should present credible evidence, highlight ethical implications,
and encourage stakeholders to adopt reforms that reduce harm while remaining
consistent with the moral expectations of the audience.
"""

st.subheader("Campaign Strategy Plan")
st.write(strategy)

# Advocacy strategy brief

brief = f"""
Audience: {audience}

Primary Stakeholder: {stakeholder}

Campaign Type: {campaign_type}

The behavioural analysis suggests that this audience responds most strongly to
{lever.lower()}. Advocacy communications should emphasise moral responsibility,
evidence-based policy solutions, and the broader societal benefits of reform.

Campaigns should prioritise coalition-building, expert credibility, and
institutional engagement while gradually shifting social norms toward
greater concern for nonhuman welfare.
"""

st.subheader("Advocacy Strategy Brief")
st.write(brief)

# -----------------------------
# PDF Export
# -----------------------------

def generate_pdf():

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    report = f"""
BAAMT Advocacy Strategy Report

Audience: {audience}
Stakeholder: {stakeholder}
Geography: {geography}

Moral Profile
Care: {care}
Fairness: {fair}
Authority: {auth}
Loyalty: {loyal}
Purity: {pure}

Behavioural Segment
{segment}

Reform Orientation
{reform}

Risk Profile
{risk}

Institutional Trust
{trust}

Primary Advocacy Lever
{lever}

Geographic Messaging
{geo_message}

Campaign Strategy
{strategy}

Advocacy Strategy Brief
{brief}
"""

    pdf.multi_cell(0,8,report)

    pdf.output("baamt_report.pdf")

generate_pdf()

with open("baamt_report.pdf","rb") as file:
    st.download_button(
        label="Download BAAMT Strategy Report",
        data=file,
        file_name="baamt_report.pdf",
        mime="application/pdf"
    )
