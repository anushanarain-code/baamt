import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import textwrap

st.set_page_config(page_title="BAAMT", layout="wide")

# ---------- INSTRUCTIONS ----------
st.title("🧠 BAAMT: Behavioural Advocacy and Messaging Tool")
st.markdown("""
BAAMT helps advocacy organizations design messaging strategies based on the moral values of their target audience.  
Complete the assessment below to generate a comprehensive behavioural profile and recommended messaging strategy.  
Please answer honestly and consider the target audience carefully. Your responses will guide strategy framing.
""")

# ---------- AUDIENCE CONTEXT ----------
st.subheader("Audience Information")
audience = st.selectbox("Select Target Audience", ["General Public", "Policy Makers", "Activists"])
geography = st.selectbox("Select Geography", ["India", "Global", "Other"])
stakeholder = st.selectbox("Select Stakeholder Type", ["Citizen", "Community Leader", "Organization Representative"])
campaign = st.selectbox("Select Campaign Type", ["Behaviour Change", "Policy Advocacy", "Awareness"])

st.markdown("""
**Instructions for Behavioural Assessment:**  
Rate each statement below from 1 (Strongly Disagree) to 5 (Strongly Agree). Consider how your target audience would respond, not yourself.  
Your answers help generate a detailed moral profile and messaging strategy.
""")

# ---------- BEHAVIOURAL ASSESSMENT ----------
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

answers = []
for q in questions:
    val = st.slider(q, 1, 5, 3)
    answers.append(val)

# ---------- RESULTS CALCULATION ----------
# Dummy calculations for demonstration
care = np.mean(answers[0:2])
fairness = np.mean(answers[1:3])
authority = np.mean(answers[2:4])
loyalty = np.mean(answers[3:5])
purity = np.mean(answers[4:6])

segment = ("Mixed moral audiences whose responses are likely to depend on contextual framing "
           "and coalition-based messaging. For instance, some individuals may prioritize harm "
           "reduction while others focus on tradition or authority.")
reform = ("This audience may be receptive to transformative or constructive advocacy narratives "
          "that highlight social change, fairness, and protection of vulnerable groups. Messaging "
          "should include practical examples of improvements and societal benefits.")
risk = ("Moderate sensitivity to moral and social risk. Advocacy can focus on evidence-based "
        "messages, illustrative stories, and harm reduction without triggering resistance.")
trust = ("Trust levels toward institutions vary. Messaging may need to emphasize transparency, "
         "reliability, and track records of organizations or policies.")
lever = ("Primary advocacy approaches could include public campaigns, coalition building, "
         "and evidence-sharing with community leaders.")
geo = ("Messaging should consider local culture, traditions, and legal frameworks, highlighting "
       "context-specific benefits and examples.")
strategy = ("A comprehensive campaign plan should integrate messaging, coalition support, "
            "and iterative feedback mechanisms to ensure engagement across diverse moral audiences.")
brief = ("The advocacy strategy combines moral framing, evidence-based messages, and actionable steps "
         "for influencing the target audience. Include clear examples, recommended channels, "
         "and potential risks.")
framing = ("Examples of message framing: emphasizing compassion, harm reduction, fairness, and "
           "community well-being with context-specific stories and data.")
coalition = ("Coalition strategy: partner with community leaders, NGOs, and relevant institutions to "
             "strengthen message credibility.")
policy = ("Policy pathway: identify regulatory levers, incentives, and advocacy channels.")
risk_analysis = ("Opposition risk: anticipate resistance points, misinformation, and social barriers.")

# ---------- RADAR CHART ----------
categories = ['Care', 'Fairness', 'Authority', 'Loyalty', 'Purity']
values = [care, fairness, authority, loyalty, purity]
values += values[:1]  # close the loop

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
ax.plot(angles, values, 'o-', linewidth=2)
ax.fill(angles, values, alpha=0.25)
ax.set_thetagrids(np.degrees(angles[:-1]), categories)
ax.set_ylim(0,5)

radar_buf = io.BytesIO()
plt.savefig(radar_buf, format='png')
plt.close(fig)
radar_buf.seek(0)

st.subheader("Audience Moral Radar Chart")
st.image(radar_buf)

# ---------- GENERATE PDF ----------
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Audience: {audience}", ln=True)
    pdf.cell(0, 8, f"Geography: {geography}", ln=True)
    pdf.cell(0, 8, f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(0, 8, f"Campaign Objective: {campaign}", ln=True)
    pdf.ln(5)
    
    # Add radar chart
    pdf.image(radar_buf, x=60, w=90)

    # ---------- ADD SECTIONS ----------
    def add_section(title, text):
        pdf.ln(4)
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(pdf.w - 2*pdf.l_margin, 7, title)
        pdf.set_font("Arial", "", 11)
        safe_text = text.replace("–","-").replace("—","-")
        paragraphs = safe_text.split('\n')
        for para in paragraphs:
            pdf.multi_cell(pdf.w - 2*pdf.l_margin, 6, para)
            pdf.ln(1)

    sections = [
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
    ]

    for title, text in sections:
        add_section(title, text)

    pdf_bytes = pdf.output(dest="S").encode("latin-1")  # PDF bytes safe for Streamlit download
    return pdf_bytes

if st.button("Generate BAAMT Strategy Report"):
    pdf_bytes = generate_pdf()
    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )

# ---------- EMAIL OPTION ----------
st.markdown("### Share via Email")
email = st.text_input("Enter recipient email")
if st.button("Send Email"):
    if email:
        # Here you would integrate email sending via SMTP or API
        st.success(f"Report would be sent to {email}. (Email sending not implemented in demo)")
    else:
        st.warning("Please enter a valid email address.")
