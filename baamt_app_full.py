import streamlit as st
from fpdf import FPDF
import textwrap
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="BAAMT Tool", layout="wide")

# ---------- INSTRUCTIONS & THEORY ----------
st.title("🧠 BAAMT")
st.markdown("""
**Behavioural Advocacy and Messaging Tool (BAAMT)** helps advocacy organizations design messaging strategies 
based on the moral values of their target audience.  

**Instructions:** Before starting the assessment, please carefully read the audience information below. 
The more accurately you understand your target audience, the better the behavioural profile and recommended 
messaging strategy will be.  

**Theoretical Framework:** This tool is grounded in **Moral Foundations Theory**, which suggests that people evaluate moral issues based on multiple dimensions:  
- **Care/Harm:** Focus on suffering and well-being of others.  
- **Fairness/Cheating:** Focus on justice, equality, and rights.  
- **Authority/Subversion:** Respect for tradition, leadership, and rules.  
- **Loyalty/Betrayal:** Commitment to community, family, and groups.  
- **Purity/Degradation:** Valuing cleanliness, sanctity, and spiritual well-being.  

Understanding these foundations helps tailor messages that resonate with the audience's values.
""")

# ---------- AUDIENCE CONTEXT ----------
st.subheader("Audience Information")
st.markdown("Select the target audience, geography, stakeholder type, and campaign objective below. This ensures the report is customized to your context.")
audience = st.selectbox("Select Target Audience", ["General Public", "Policy Makers", "Activists"])
geography = st.selectbox("Select Geography", ["India", "USA", "UK", "Global"])
stakeholder = st.selectbox("Select Stakeholder Type", ["NGO", "Government", "Corporation", "Community Group"])
campaign = st.selectbox("Select Campaign Objective", ["Behaviour Change", "Policy Advocacy", "Awareness Raising"])

# ---------- BEHAVIOURAL ASSESSMENT ----------
st.subheader("Behavioural Assessment")
st.markdown("Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree). Try to answer based on the target audience's likely perspective.")
care = st.slider("Preventing suffering should be a top priority in public policy.", 1, 5, 3)
fairness = st.slider("Fair treatment matters even if it requires economic trade-offs.", 1, 5, 3)
authority = st.slider("Society functions best when people respect authority and institutions.", 1, 5, 3)
loyalty = st.slider("Loyalty to one's community should guide political decision-making.", 1, 5, 3)
purity = st.slider("Purity and moral cleanliness are important social values.", 1, 5, 3)

# ---------- RESULTS LOGIC ----------
segment = (
    "This audience demonstrates a combination of moral priorities. They value fairness and care, "
    "but their decisions can be influenced by context, storytelling, and social cues. For example, "
    "they might support policies to protect animals if shown clear harm reduction, or prioritize "
    "community wellbeing when messages highlight group cohesion and positive local outcomes."
)

reform = (
    "This audience may respond well to narratives advocating for progressive or transformative change. "
    "Messages should include clear examples of how new policies or initiatives have led to meaningful improvements, "
    "showing the audience tangible benefits while framing change as both responsible and achievable."
)

risk = (
    "The audience has moderate sensitivity to moral risk. Messaging can focus on concrete evidence, harm reduction, "
    "and practical outcomes. For instance, showing case studies where policies prevented suffering or improved social equity can be effective."
)

trust = (
    "Institutional trust varies among this audience. Some follow government or NGO guidance closely, "
    "while others rely on community leaders. Messages should balance respect for authority with relatable stories of local impact."
)

lever = (
    "Primary advocacy lever: Use compassion and actionable guidance to engage the audience. "
    "Provide clear steps that individuals can take to contribute positively, such as volunteering, policy support, or spreading awareness."
)

geo = (
    f"Geographic messaging adjustment: Tailor examples and case studies to the {geography} context. "
    "Local stories, cultural norms, and region-specific priorities make messages more relatable and impactful."
)

strategy = (
    "Campaign Strategy Plan: Segment outreach by moral foundation emphasis, use coalition messaging, and employ storytelling. "
    "Highlight positive change examples, showcase social proof, and adjust framing based on audience moral priorities."
)

brief = (
    "Full Advocacy Strategy Brief: Provide actionable recommendations tailored to the audience, "
    "ensuring alignment with moral foundations and local context. Include concrete examples, suggested channels, "
    "and tips for measuring impact to support ongoing improvements."
)

framing = (
    "Message Framing Examples: Emphasize personal stories, empirical evidence, and collective benefits. "
    "For example, illustrate how a policy prevented harm to vulnerable communities or animals, and the positive outcomes observed."
)

coalition = (
    "Coalition Strategy: Partner with trusted local NGOs, activists, and community leaders who embody the audience's moral values. "
    "Collaborative messaging increases credibility and engagement."
)

policy = (
    "Policy Pathway: Highlight achievable steps, existing policy successes, and practical implementation guidance. "
    "Show how proposed actions fit within broader legal and institutional frameworks."
)

risk_analysis = (
    "Opposition Risk Analysis: Identify potential counterarguments, risks, and areas of resistance. "
    "Prepare morally grounded, evidence-based responses to anticipate audience concerns."
)

# ---------- GENERATE REPORT ----------
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

    st.divider()

    # ---------- PDF ----------
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.ln(5)
    pdf.cell(0, 8, f"Audience: {audience}", ln=True)
    pdf.cell(0, 8, f"Geography: {geography}", ln=True)
    pdf.cell(0, 8, f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(0, 8, f"Campaign Objective: {campaign}", ln=True)
    pdf.ln(5)

    def add_section(title, text):
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, title, ln=True)
        pdf.set_font("Arial", "", 11)
        for line in textwrap.wrap(text, 90):
            pdf.cell(0, 7, line, ln=True)
        pdf.ln(2)

    sections = [
        ("Behavioural Segment", segment),
        ("Reform Orientation", reform),
        ("Risk Sensitivity Profile", risk),
        ("Institutional Trust Orientation", trust),
        ("Primary Advocacy Lever", lever),
        ("Geographic Messaging Adjustment", geo),
        ("Campaign Strategy Plan", strategy),
        ("Full Advocacy Strategy Brief", brief),
        ("Message Framing Examples", framing),
        ("Coalition Strategy", coalition),
        ("Policy Pathway", policy),
        ("Opposition Risk Analysis", risk_analysis),
    ]

    for title, text in sections:
        add_section(title, text)

    # ---------- RADAR CHART ----------
    labels = ['Care', 'Fairness', 'Authority', 'Loyalty', 'Purity']
    values = [care, fairness, authority, loyalty, purity]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_title("Audience Moral Foundations Radar Chart", fontsize=10)

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='PNG', bbox_inches='tight')
    plt.close(fig)
    img_buffer.seek(0)
    pdf.image(img_buffer, x=30, w=150)

    pdf_bytes = pdf.output(dest="S").encode("utf-8")  # <-- UTF-8 safe

    # ---------- DOWNLOAD BUTTON ----------
    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )

    # ---------- EMAIL OPTION ----------
    st.subheader("Email the Report")
    email_to = st.text_input("Enter recipient email address")
    if st.button("Send Report via Email") and email_to:
        try:
            msg = MIMEMultipart()
            msg['Subject'] = 'BAAMT Advocacy Strategy Report'
            msg['From'] = 'your_email@example.com'  # replace with sender
            msg['To'] = email_to
            msg.attach(MIMEText("Please find attached the BAAMT report.", "plain"))
            attachment = MIMEApplication(pdf_bytes, _subtype="pdf")
            attachment.add_header('Content-Disposition', 'attachment', filename="BAAMT_report.pdf")
            msg.attach(attachment)

            # Simple SMTP example (replace with real server and credentials)
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login('your_email@example.com', 'your_password')
                server.send_message(msg)

            st.success(f"Report sent to {email_to}")
        except Exception as e:
            st.error(f"Failed to send email: {e}")
