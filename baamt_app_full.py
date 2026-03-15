import streamlit as st
import textwrap
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
from io import BytesIO

st.set_page_config(page_title="BAAMT - Behavioural Advocacy Tool", layout="wide")

# ---------- INSTRUCTION ABOVE AUDIENCE CONTEXT ----------
st.markdown("""
# 🧠 BAAMT
**Behavioural Advocacy and Messaging Tool**

BAAMT helps advocacy organizations design messaging strategies based on the moral values of their target audience.

**Instructions:** Please select the target audience, geography, stakeholder type, and campaign objective. Then, complete the behavioral assessment. Your responses will generate a detailed behavioral profile and suggested advocacy messaging strategy. Each section includes reader-friendly explanations and examples to make the outputs actionable for your campaigns.
""")

# ---------- AUDIENCE CONTEXT ----------
audience = st.selectbox("Select Target Audience", ["General Public", "Policymakers", "Community Leaders"])
geography = st.selectbox("Select Geography", ["India", "Global", "Other"])
stakeholder = st.selectbox("Select Stakeholder Type", ["Individual", "Organization", "Government Body"])
campaign = st.selectbox("Select Campaign Objective", ["Behaviour Change", "Policy Change", "Awareness Raising"])

# ---------- BEHAVIORAL ASSESSMENT ----------
st.markdown("## Behavioural Assessment")
st.markdown("Rate the following statements from **1 (Strongly Disagree)** to **5 (Strongly Agree).**")

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
    answers.append(st.slider(q, 1, 5, 3))

# ---------- CALCULATE SCORES ----------
care, fairness, authority, loyalty, purity = answers[0], answers[1], answers[2], answers[3], answers[4]

# ---------- DERIVED RESULTS ----------
segment = ("Mixed moral audiences whose responses may depend on context. "
           "They may react differently to messaging depending on whether it emphasizes harm reduction, fairness, or loyalty, and often require coalition-based framing. Examples include campaigns around animal welfare, environmental regulations, or social justice issues where values might conflict.")
reform = ("This audience may be receptive to transformative advocacy narratives that highlight systemic change, social responsibility, "
          "and moral duty. Messaging can emphasize long-term societal benefits, ethical leadership, and positive community outcomes. "
          "Examples: advocating for stricter animal welfare laws, promoting renewable energy policies, or supporting inclusive education reforms.")
risk = ("Audience shows moderate sensitivity to moral and societal risks. Messaging can include clear evidence of potential harm, success stories, "
        "and data-supported projections to enhance credibility. For example, highlighting the health benefits of plant-based diets, or social improvements from clean water initiatives.")
trust = ("Audience trust in institutions is moderate. Messages should acknowledge institutional roles but also empower personal responsibility and community engagement. "
         "Examples include promoting compliance with new health policies while encouraging local initiatives.")
lever = ("Primary advocacy lever is moral framing. Messages should connect policy or behavioral recommendations to ethical principles, social responsibility, and empathy. "
         "For instance, highlighting how community action reduces suffering or improves fairness.")
geo = ("Geographic adjustments consider local norms, cultural practices, and region-specific examples. For India, emphasize community, family, and societal cohesion in messaging.")
strategy = ("Campaign strategy plan includes phased messaging: initial awareness, followed by engagement, and finally, actionable calls for change. "
            "Use multi-channel approaches: social media, community workshops, and educational campaigns.")
brief = ("Full advocacy strategy brief synthesizes moral profile, behavioral segment, reform orientation, risk sensitivity, and recommended messaging frames. "
         "It guides implementers on messaging tone, coalition partners, policy pathways, and risk mitigation.")
framing = ("Message framing examples include emphasizing compassion, highlighting harm reduction, showcasing fairness in economic decisions, "
           "and invoking loyalty to community for participation. Add 2–3 examples per campaign for clarity.")
coalition = ("Coalition strategy identifies partners that share aligned values, creating stronger advocacy networks. Include NGOs, government bodies, and community organizations.")
policy = ("Policy pathway outlines feasible steps for implementing change while minimizing resistance. Include regulatory steps, incentives, and stakeholder buy-in.")
risk_analysis = ("Opposition risk analysis identifies potential counterarguments, sources of resistance, and mitigation strategies. Prepare messaging for both supportive and skeptical audiences.")

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

# ---------- RADAR CHART ----------
labels = ['Care', 'Fairness', 'Authority', 'Loyalty', 'Purity']
values = [care, fairness, authority, loyalty, purity]
values += values[:1]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.plot(angles, values, color='blue', linewidth=2)
ax.fill(angles, values, color='blue', alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_ylim(0,5)
ax.set_yticks([1,2,3,4,5])
ax.set_title("Audience Moral Foundations Radar Chart", fontsize=12)
st.pyplot(fig)

# ---------- GENERATE PDF & DOWNLOAD ----------
if st.button("Generate BAAMT Strategy Report"):
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

    for title, text in sections:
        add_section(title, text)

    # ---------- EMBED RADAR CHART ----------
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='PNG', bbox_inches='tight')
    plt.close(fig)
    img_buffer.seek(0)
    pdf.image(img_buffer, x=30, w=150)

    # ---------- SAVE TO BytesIO ----------
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    # ---------- DOWNLOAD BUTTON ----------
    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_buffer,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )

    # ---------- EMAIL OPTION ----------
    email = st.text_input("Enter your email to receive a copy:")
    if st.button("Send Report to Email") and email:
        # Here you would integrate email sending (SMTP or API)
        st.success(f"Report sent to {email} (demo placeholder, implement email backend).")
