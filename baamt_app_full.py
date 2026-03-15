import streamlit as st
from fpdf import FPDF
import textwrap
import matplotlib.pyplot as plt
import io

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="BAAMT - Behavioural Advocacy and Messaging Tool",
    layout="wide"
)

# ----------------- HEADER -----------------
st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")
st.markdown(
    """
BAAMT helps advocacy organizations design messaging strategies based on the moral values of their target audience.
Complete the assessment below to generate a behavioural profile and recommended messaging strategy.
"""
)

# ----------------- AUDIENCE CONTEXT -----------------
st.markdown(
    "**Audience Information:** Please provide context for your target audience. This helps generate more precise messaging recommendations."
)

audience = st.selectbox("Select Target Audience", ["General Public", "Policymakers", "Youth", "Industry Stakeholders"])
geography = st.selectbox("Select Geography", ["India", "Global", "Other"])
stakeholder = st.selectbox("Select Stakeholder Type", ["Non-profit", "Government", "Corporate", "Academic"])
campaign = st.selectbox("Select Campaign Type", ["Behaviour Change", "Policy Advocacy", "Awareness Raising"])

# ----------------- BEHAVIOURAL ASSESSMENT -----------------
st.markdown(
    """
### Behavioural Assessment
Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree).

*These statements are grounded in Moral Foundations Theory, which helps understand the ethical priorities that guide people's decisions and responses.*
"""
)

questions = [
    "Preventing suffering should be a top priority in public policy.",
    "Fair treatment matters even if it requires economic trade-offs.",
    "Society functions best when people respect authority and institutions.",
    "Loyalty to one's community should guide political decision-making.",
    "Purity and moral cleanliness are important social values.",
    "Avoiding harm to vulnerable beings is an ethical responsibility.",
    "Rules and laws should be followed even when inconvenient.",
    "People should prioritize fairness in markets and economic systems.",
    "Communities should protect their cultural traditions.",
    "Certain practices are morally wrong regardless of consequences."
]

responses = []
for q in questions:
    responses.append(st.slider(q, 1, 5, 3))

# ----------------- SIMPLE SCORING -----------------
care = responses[0] + responses[5]
fairness = responses[1] + responses[7]
authority = responses[2] + responses[6]
loyalty = responses[3] + responses[8]
purity = responses[4] + responses[9]

segment = "Mixed moral audiences whose responses are likely to depend on contextual framing and coalition-based messaging. This means different groups may interpret the same message differently, so combining empathy, fairness, and social responsibility themes can be effective."

reform = "This audience may respond well to narratives that highlight the need for thoughtful social change, emphasizing both incremental improvements and broader transformative ideas. Messaging should clarify why reforms benefit communities and individuals alike."

risk = "The audience shows moderate sensitivity to moral risk. Effective advocacy can focus on evidence-backed harm reduction, real-life examples of impact, and the tangible benefits of adopting certain practices."

trust = "This audience places moderate trust in institutions. Messaging should build credibility by referencing reliable sources, highlighting transparency, and showing consistent ethical behavior from organizations."

lever = "Primary advocacy lever: Highlighting compassion and fairness, using storytelling, case studies, and social proof to encourage desired behaviors."

geo = f"Geographic messaging adjustment: Since the audience is in {geography}, include culturally relevant examples, local success stories, and language that resonates with regional norms."

strategy = "Campaign strategy plan: Use multi-channel approaches including social media, community workshops, and policy briefs. Tailor messaging to moral priorities of care, fairness, and loyalty to maximize engagement."

brief = "Full advocacy strategy brief: Combine the insights above into a coherent plan that emphasizes ethical responsibility, fairness, and social progress. Include concrete actions, messaging examples, coalition-building tactics, and risk mitigation strategies."

framing = "Message framing examples: \n1. Highlight suffering prevention and empathy.\n2. Show fairness in action through case studies.\n3. Emphasize community benefits and social cohesion.\n4. Include local cultural references to increase relevance."

coalition = "Coalition strategy: Partner with NGOs, academic institutions, and credible influencers to amplify messaging and reach diverse moral audiences."

policy = "Policy pathway: Recommend incremental policy changes backed by evidence, align proposals with public values, and show anticipated benefits."

risk_analysis = "Opposition risk analysis: Identify stakeholders likely to resist change, understand their motivations, and prepare counter-frames emphasizing shared moral priorities."

# ----------------- RADAR CHART -----------------
fig, ax = plt.subplots(figsize=(5, 5))
labels = ["Care", "Fairness", "Authority", "Loyalty", "Purity"]
values = [care, fairness, authority, loyalty, purity]
angles = [n / float(len(labels)) * 2 * 3.14159 for n in range(len(labels))]
values += values[:1]
angles += angles[:1]

ax.set_theta_offset(3.14159 / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], labels)
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Moral Profile")
ax.fill(angles, values, 'b', alpha=0.1)
plt.legend()
st.pyplot(fig)

# Save chart for PDF
chart_buf = io.BytesIO()
fig.savefig(chart_buf, format="PNG")
chart_buf.seek(0)

# ----------------- PDF GENERATION -----------------
if st.button("Generate BAAMT Strategy Report"):

    st.subheader("Behavioural Segment")
    st.write(segment)

    st.subheader("Reform Orientation")
    st.write(reform)

    st.subheader("Risk Sensitivity Profile")
    st.write(risk)

    st.subheader("Institutional Trust Orientation")
    st.write(trust)

    st.subheader("Primary Advocacy Lever")
    st.write(lever)

    st.subheader("Geographic Messaging Adjustment")
    st.write(geo)

    st.subheader("Campaign Strategy Plan")
    st.write(strategy)

    st.subheader("Full Advocacy Strategy Brief")
    st.write(brief)

    st.subheader("Message Framing Examples")
    st.write(framing)

    st.subheader("Coalition Strategy")
    st.write(coalition)

    st.subheader("Policy Pathway")
    st.write(policy)

    st.subheader("Opposition Risk Analysis")
    st.write(risk_analysis)

    st.divider()

    # ---------- FORMATTED PDF REPORT ----------
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Audience: {audience}", ln=True)
    pdf.cell(0, 8, f"Geography: {geography}", ln=True)
    pdf.cell(0, 8, f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(0, 8, f"Campaign Objective: {campaign}", ln=True)

    def add_section(title, text):
        pdf.ln(4)
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 8, title)
        pdf.set_font("Arial", "", 11)
        wrapped = textwrap.wrap(text, 90)
        for line in wrapped:
            pdf.multi_cell(0, 7, line)

    add_section("Behavioural Segment", segment)
    add_section("Reform Orientation", reform)
    add_section("Risk Sensitivity Profile", risk)
    add_section("Institutional Trust Orientation", trust)
    add_section("Primary Advocacy Lever", lever)
    add_section("Geographic Messaging Adjustment", geo)
    add_section("Campaign Strategy Plan", strategy)
    add_section("Full Advocacy Strategy Brief", brief)
    add_section("Message Framing Examples", framing)
    add_section("Coalition Strategy", coalition)
    add_section("Policy Pathway", policy)
    add_section("Opposition Risk Analysis", risk_analysis)

    # Add chart to PDF
    pdf.image(chart_buf, x=60, w=90)

    pdf_bytes = pdf.output(dest="S").encode("latin-1")

    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )

    # Optional email sharing
    recipient = st.text_input("Enter email to send report (optional)")
    if recipient:
        st.info(f"Report ready to be sent to {recipient} (email integration pending).")
