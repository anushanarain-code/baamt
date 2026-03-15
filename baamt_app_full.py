import streamlit as st
import pandas as pd
import numpy as np
from fpdf import FPDF
import matplotlib.pyplot as plt
import io
import textwrap
import smtplib
from email.message import EmailMessage

# ---------- APP CONFIG ----------
st.set_page_config(page_title="BAAMT", layout="wide")

st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")
st.write("BAAMT helps advocacy organizations design messaging strategies based on the moral values of their target audience.\n"
         "Complete the assessment below to generate a behavioural profile and recommended messaging strategy.")

# ---------- AUDIENCE CONTEXT ----------
st.markdown("**Audience Context:** Please select the relevant audience, geography, stakeholder, and campaign objective for your messaging.")

audience = st.selectbox("Select Target Audience", ["General Public", "Policy Makers", "Community Leaders"])
geography = st.selectbox("Select Geography", ["India", "Global", "Other"])
stakeholder = st.selectbox("Select Stakeholder Type", ["General Public", "Corporate", "NGO"])
campaign = st.selectbox("Select Campaign Objective", ["Behaviour Change", "Policy Reform", "Awareness Raising"])

# ---------- BEHAVIOURAL ASSESSMENT ----------
st.markdown("**Behavioural Assessment:** Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree).")
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

responses = {}
for q in questions:
    responses[q] = st.slider(q, 1, 5, 3)

# ---------- CALCULATE RESULTS ----------
# Example calculations for demonstration
segment = ("Mixed moral audiences whose responses are likely to depend on contextual framing and coalition-based messaging. "
           "For instance, some individuals may prioritize harm reduction while others focus on tradition or authority.")
reform = ("This audience may be receptive to transformative or constructive advocacy narratives that highlight social change, fairness, "
          "and protection of vulnerable groups. Messaging should include practical examples of improvements and societal benefits.")
risk = ("Moderate sensitivity to moral and social risk. Advocacy can focus on evidence-based messages, illustrative stories, "
        "and harm reduction without triggering resistance.")
trust = ("Trust levels toward institutions vary. Messaging may need to emphasize transparency, reliability, "
         "and track records of organizations or policies.")
lever = ("Primary advocacy approaches could include public campaigns, coalition building, and evidence-sharing with community leaders.")
geo = ("Messaging should consider local culture, traditions, and legal frameworks, highlighting context-specific benefits and examples.")
strategy = ("A comprehensive campaign plan should integrate messaging, coalition support, and iterative feedback mechanisms to ensure engagement across diverse moral audiences.")
brief = ("The advocacy strategy combines moral framing, evidence-based messages, and actionable steps for influencing the target audience. "
         "Include clear examples, recommended channels, and potential risks.")
framing = ("Use stories, case studies, and illustrative examples to show the impact of moral choices. "
           "Include examples from local contexts and communities.")
coalition = ("Engage local leaders, NGOs, and community groups to amplify your messaging and create shared ownership of advocacy goals.")
policy = ("Identify feasible policy pathways aligned with audience moral profiles, using evidence and examples to demonstrate benefits.")
risk_analysis = ("Highlight potential opposition arguments and societal risks, with clear mitigation strategies.")

# ---------- RADAR CHART ----------
labels = ["Care", "Fairness", "Authority", "Loyalty", "Purity"]
values = [responses[questions[0]], responses[questions[1]], responses[questions[2]],
          responses[questions[3]], responses[questions[4]]]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]
fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
ax.plot(angles, values, 'o-', linewidth=2)
ax.fill(angles, values, alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticklabels([])
radar_buf = io.BytesIO()
plt.savefig(radar_buf, format='png')
plt.close(fig)
radar_buf.seek(0)

# ---------- GENERATE PDF ----------
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title and context
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Audience: {audience}", ln=True)
    pdf.cell(0, 8, f"Geography: {geography}", ln=True)
    pdf.cell(0, 8, f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(0, 8, f"Campaign Objective: {campaign}", ln=True)
    pdf.ln(5)

    # Theoretical Framework
    framework_text = ("BAAMT is based on the Moral Foundations Theory, which identifies core moral dimensions that influence "
                      "how different audiences interpret ethical issues. These dimensions include Care/Harm, Fairness/Cheating, "
                      "Authority/Subversion, Loyalty/Betrayal, and Purity/Degradation. Understanding these foundations helps tailor "
                      "advocacy messages to resonate with the audience's values.")
    pdf.set_font("Arial", "B", 12)
    pdf.multi_cell(pdf.w - 2*pdf.l_margin, 7, "Theoretical Framework")
    pdf.set_font("Arial", "", 11)
    for line in textwrap.wrap(framework_text, 100):
        pdf.multi_cell(pdf.w - 2*pdf.l_margin, 6, line)
    pdf.ln(4)

    # Radar Chart
    pdf.image(radar_buf, x=60, w=90)
    pdf.ln(5)

    # Section helper
    def add_section(title, text):
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(pdf.w - 2*pdf.l_margin, 7, title)
        pdf.set_font("Arial", "", 11)
        safe_text = text.replace("–","-").replace("—","-")
        paragraphs = safe_text.split('\n')
        for para in paragraphs:
            for line in textwrap.wrap(para, 100):
                pdf.multi_cell(pdf.w - 2*pdf.l_margin, 6, line)
            pdf.ln(1)

    # Add all sections
    for title, text in [
        ("Behavioural Segment", segment),
        ("Reform Orientation", reform),
        ("Risk Sensitivity Profile", risk),
        ("Institutional Trust Orientation", trust),
        ("Primary Advocacy Lever", lever),
        ("Geographic Messaging Adjustment", geo),
        ("Campaign Strategy Plan", strategy),
        ("Advocacy Strategy Brief", brief),
        ("Message Framing Examples", framing),
        ("Coalition Strategy", coalition),
        ("Policy Pathway", policy),
        ("Opposition Risk Analysis", risk_analysis)
    ]:
        add_section(title, text)

    return pdf.output(dest="S").encode("utf-8")

# ---------- DISPLAY RESULTS ----------
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
    st.subheader("Advocacy Strategy Brief")
    st.write(brief)

    st.image(radar_buf)

    # PDF Download
    pdf_bytes = generate_pdf()
    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )

    # Optional Email
    email_option = st.checkbox("Email this report")
    if email_option:
        recipient = st.text_input("Recipient email address")
        if st.button("Send Email") and recipient:
            try:
                msg = EmailMessage()
                msg['Subject'] = "Your BAAMT Strategy Report"
                msg['From'] = "your_email@example.com"  # <-- replace with real email
                msg['To'] = recipient
                msg.set_content("Please find your BAAMT Strategy Report attached.")
                msg.add_attachment(pdf_bytes, maintype='application', subtype='pdf', filename='BAAMT_report.pdf')
                # Example using Gmail SMTP (requires app password)
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login("your_email@example.com", "your_app_password")
                    smtp.send_message(msg)
                st.success("Email sent successfully!")
            except Exception as e:
                st.error(f"Error sending email: {e}")
