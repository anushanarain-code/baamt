# BAAMT Streamlit App – Full Final Version
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import textwrap
import io

# ------------------ APP CONFIG ------------------
st.set_page_config(page_title="BAAMT Tool", page_icon="🧠", layout="wide")
st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")
st.write("""
BAAMT helps advocacy organizations design messaging strategies based on the moral values, risk orientations, and institutional trust of their target audience. 
Complete the assessment below to generate a detailed behavioural profile and advocacy strategy.
""")

# ------------------ AUDIENCE CONTEXT ------------------
st.markdown("### Audience Information")
st.info("Select the target audience, geography, and stakeholder type to tailor the messaging strategy appropriately.")

audience = st.selectbox("Target Audience", ["General Public", "Policy Makers", "Community Leaders"])
geography = st.selectbox("Geography", ["India", "USA", "UK", "Other"])
stakeholder = st.selectbox("Stakeholder Type", ["Individual", "NGO", "Government Agency"])
campaign = st.selectbox("Campaign Objective", ["Behaviour Change", "Policy Reform", "Awareness Campaign"])

# ------------------ BEHAVIOURAL ASSESSMENT ------------------
st.markdown("### Behavioural Assessment")
st.info("Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree).")

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
    score = st.slider(q, 1, 5, 3, key=q)
    responses.append(score)

# ------------------ COMPUTE RESULTS ------------------
care = responses[0] + responses[5]
fairness = responses[1] + responses[6]
authority = responses[2] + responses[7]
loyalty = responses[3] + responses[8]
purity = responses[4] + responses[9]

# Radar chart setup
labels = ["Care/Harm", "Fairness", "Authority", "Loyalty", "Purity"]
values = [care, fairness, authority, loyalty, purity]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
values += values[:1]
angles = np.concatenate((angles, [angles[0]]))

# ------------------ DISPLAY RESULTS ------------------
st.markdown("### Audience Moral Profile")
for label, value in zip(labels, values[:-1]):
    st.write(f"{label}: {value}")

# Radar chart
fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.plot(angles, values, 'o-', linewidth=2)
ax.fill(angles, values, alpha=0.25)
ax.set_thetagrids(angles[:-1]*180/np.pi, labels)
ax.set_title("Moral Foundations Radar Chart")
st.pyplot(fig)

# ------------------ INTERPRET RESULTS ------------------
segment = (
    "Mixed moral audiences whose responses are likely to depend on contextual framing "
    "and coalition-based messaging. For instance, some individuals may prioritize harm "
    "reduction while others may focus on tradition or authority. Clear examples and narratives "
    "help communicate across these differences."
)

reform = (
    "This audience may be receptive to transformative or constructive advocacy narratives "
    "that highlight social change, fairness, and protection of vulnerable groups. "
    "Messaging should include practical examples of improvements, societal benefits, "
    "and illustrative case studies."
)

risk = (
    "Moderate sensitivity to moral and social risk. Advocacy messaging can focus on "
    "evidence-based examples, stories of harm reduction, and positive outcomes without "
    "triggering resistance or defensiveness."
)

trust = (
    "Trust levels toward institutions vary. Messaging may need to emphasize transparency, "
    "reliability, and proven track records of organizations or policies, using real-life "
    "examples to illustrate credibility."
)

lever = (
    "Primary advocacy approaches could include public campaigns, coalition building, "
    "and sharing evidence with community leaders and influencers who can amplify messages."
)

geo = (
    f"Messaging should consider the local culture, traditions, and legal frameworks in {geography}. "
    "Highlight context-specific benefits, examples, and culturally relevant narratives."
)

strategy = (
    "A comprehensive campaign plan should integrate messaging, coalition support, "
    "and iterative feedback mechanisms to ensure engagement across diverse moral audiences."
)

brief = (
    "The advocacy strategy combines moral framing, evidence-based messages, and actionable steps "
    "for influencing the target audience. Include clear examples, recommended channels, "
    "and potential risks, ensuring alignment with the target audience’s values and sensitivities."
)

theory = (
    "Theoretical Framework: BAAMT is based on Moral Foundations Theory, which identifies five key dimensions "
    "of moral reasoning — Care/Harm, Fairness, Loyalty, Authority, and Purity. This framework helps tailor "
    "messages to resonate with the audience’s moral intuitions, increasing engagement and effectiveness."
)

# ------------------ PDF GENERATION ------------------
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "B", 16)
    pdf.multi_cell(0, 8, "BAAMT Advocacy Strategy Report", align="C")
    pdf.ln(5)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, f"Audience: {audience}")
    pdf.multi_cell(0, 6, f"Geography: {geography}")
    pdf.multi_cell(0, 6, f"Stakeholder: {stakeholder}")
    pdf.multi_cell(0, 6, f"Campaign Objective: {campaign}")
    pdf.ln(4)
    
    def add_section(title, text):
        pdf.set_font("Arial", "B", 13)
        pdf.multi_cell(0, 6, title)
        pdf.set_font("Arial", "", 12)
        wrapped = textwrap.wrap(text, 100)
        for line in wrapped:
            pdf.multi_cell(0, 6, line)
        pdf.ln(2)
    
    add_section("Theoretical Framework", theory)
    add_section("Behavioural Segment", segment)
    add_section("Reform Orientation", reform)
    add_section("Risk Sensitivity Profile", risk)
    add_section("Institutional Trust Orientation", trust)
    add_section("Primary Advocacy Lever", lever)
    add_section("Geographic Messaging Adjustment", geo)
    add_section("Campaign Strategy Plan", strategy)
    add_section("Advocacy Strategy Brief", brief)

    pdf_bytes = io.BytesIO()
    pdf.output(pdf_bytes)
    pdf_bytes.seek(0)
    return pdf_bytes

# ------------------ GENERATE & DOWNLOAD BUTTON ------------------
if st.button("Generate BAAMT Strategy Report"):
    st.success("Report generated successfully! You can download or share it via email below.")
    pdf_bytes = generate_pdf()

    # Download PDF
    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )

    # Email share
    recipient_email = st.text_input("Email Report To (optional)")
    if recipient_email:
        st.info(f"Email functionality placeholder – in production, the PDF would be sent to {recipient_email}.")

# ------------------ END OF APP ------------------
