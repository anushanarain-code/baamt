import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import textwrap
from fpdf import FPDF
import io

# ---------- APP CONFIG ----------
st.set_page_config(page_title="BAAMT - Behavioural Advocacy Tool", layout="wide")

# ---------- TITLE AND DESCRIPTION ----------
st.title("🧠 BAAMT")
st.markdown("""
**Behavioural Advocacy and Messaging Tool**  
BAAMT helps advocacy organizations design messaging strategies based on the moral values of their target audience.  

Complete the assessment below to generate a behavioural profile and a recommended advocacy messaging strategy.
""")

# ---------- AUDIENCE CONTEXT ----------
st.subheader("Audience Information")
st.markdown("Please provide details about the audience, geography, and stakeholder context. This helps tailor the messaging strategy appropriately.")

audience = st.selectbox("Select Target Audience", ["General Public", "Policy Makers", "Community Leaders"])
geography = st.selectbox("Select Geography", ["India", "USA", "Global"])
stakeholder = st.selectbox("Select Stakeholder Type", ["Civil Society", "NGO Staff", "Government Officials"])
campaign = st.selectbox("Select Campaign Objective", ["Behaviour Change", "Policy Advocacy", "Awareness Raising"])

# ---------- INSTRUCTIONS ----------
st.markdown("""
**Instructions for Behavioural Assessment:**  
Rate each statement on a scale from **1 (Strongly Disagree)** to **5 (Strongly Agree)**. Try to answer based on how your target audience is likely to respond.
""")

# ---------- BEHAVIOURAL ASSESSMENT ----------
st.subheader("Behavioural Assessment")
statements = [
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

responses = {}
for stmt in statements:
    responses[stmt] = st.slider(stmt, min_value=1, max_value=5, value=3)

# ---------- CALCULATE AUDIENCE MORAL PROFILE ----------
moral_foundations = {
    "Care/Harm": [0, 5, 0, 0, 0, 5, 0, 0, 0, 0],
    "Fairness": [0, 5, 0, 0, 0, 0, 0, 5, 0, 0],
    "Authority": [0, 0, 5, 0, 0, 0, 5, 0, 0, 0],
    "Loyalty": [0, 0, 0, 5, 0, 0, 0, 0, 5, 0],
    "Purity": [0, 0, 0, 0, 5, 0, 0, 0, 0, 5]
}

moral_scores = {}
for foundation, weights in moral_foundations.items():
    score = sum([responses[stmt]*w for stmt, w in zip(statements, weights)]) / max(1, sum(weights))
    moral_scores[foundation] = round(score, 2)

# ---------- RADAR CHART ----------
st.subheader("Audience Moral Profile")
categories = list(moral_scores.keys())
values = list(moral_scores.values())
values += values[:1]  # close the loop

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.plot(angles, values, 'o-', linewidth=2)
ax.fill(angles, values, alpha=0.25)
ax.set_thetagrids(np.degrees(angles[:-1]), categories)
ax.set_ylim(0,5)
st.pyplot(fig)

# ---------- BEHAVIOURAL SEGMENT ----------
segment = ("Mixed moral audiences whose responses are likely to depend on contextual framing "
           "and coalition-based messaging. For instance, some individuals may prioritize harm reduction, "
           "while others focus on tradition or authority. Practical examples could include advocacy on animal welfare, "
           "environmental policies, or community health programs.")

# ---------- REFORM ORIENTATION ----------
reform = ("This audience may be receptive to transformative or constructive advocacy narratives that "
          "highlight social change, fairness, and protection of vulnerable groups. Messaging should "
          "include practical examples of improvements, societal benefits, and step-by-step recommendations.")

# ---------- RISK SENSITIVITY ----------
risk = ("Moderate sensitivity to moral and social risk. Advocacy can focus on evidence-based messages, "
        "illustrative stories, and harm reduction without triggering resistance. For example, highlight "
        "how small policy changes improve lives without causing major disruption.")

# ---------- INSTITUTIONAL TRUST ----------
trust = ("Trust levels toward institutions vary. Messaging may need to emphasize transparency, "
         "reliability, and track records of organizations or policies. Examples: cite prior successful programs, "
         "show measurable impact, or use trusted community voices.")

# ---------- PRIMARY ADVOCACY LEVER ----------
lever = ("Primary advocacy approaches could include public campaigns, coalition building, and evidence-sharing "
         "with community leaders. Messaging should combine moral framing with clear actionable steps.")

# ---------- GEOGRAPHIC MESSAGING ----------
geo = ("Messaging should consider local culture, traditions, and legal frameworks, "
       "highlighting context-specific benefits and examples. For instance, in urban areas, emphasize policy impact; "
       "in rural areas, focus on community practices.")

# ---------- CAMPAIGN STRATEGY ----------
strategy = ("A comprehensive campaign plan should integrate messaging, coalition support, and iterative feedback mechanisms "
            "to ensure engagement across diverse moral audiences. Include steps, timeline, and monitoring metrics.")

# ---------- FULL ADVOCACY STRATEGY ----------
brief = ("The advocacy strategy combines moral framing, evidence-based messages, and actionable steps "
         "for influencing the target audience. Include clear examples, recommended channels, and potential risks.")

# ---------- MESSAGE FRAMING EXAMPLES ----------
framing = ("Examples of message framing: highlight stories of individuals affected, quantify benefits of policy change, "
           "illustrate fairness and harm reduction, use testimonials, or emphasize ethical obligations.")

# ---------- ADDITIONAL STRATEGIES ----------
coalition = ("Form coalitions with aligned organizations, community groups, and trusted leaders to broaden influence. "
             "Provide examples of successful collaborations.")
policy = ("Map policy pathways, identify key decision-makers, and provide recommendations. Include legislative or administrative steps.")
risk_analysis = ("Assess potential opposition risks and public backlash. Include mitigation strategies, ethical considerations, "
                 "and contingency planning.")

# ---------- GENERATE AND DOWNLOAD PDF ----------
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Audience: {audience}", ln=True)
    pdf.cell(0, 8, f"Geography: {geography}", ln=True)
    pdf.cell(0, 8, f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(0, 8, f"Campaign Objective: {campaign}", ln=True)
    
    def add_section(title, text):
        pdf.ln(4)
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 7, title)
        pdf.set_font("Arial", "", 11)
        wrapped = textwrap.wrap(text, 90)
        for line in wrapped:
            pdf.multi_cell(0, 6, line)
    
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
    
    # Return PDF as bytes
    return pdf.output(dest="S").encode("latin-1")

# ---------- GENERATE REPORT BUTTON ----------
if st.button("Generate BAAMT Strategy Report"):
    pdf_bytes = generate_pdf()
    st.success("Report generated successfully!")
    
    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )
    
    # Email sharing (simplest approach)
    email_address = st.text_input("Send report to email (optional)")
    if email_address and st.button("Send Report via Email"):
        st.info(f"Simulated email sent to {email_address} with the BAAMT report attached.")
