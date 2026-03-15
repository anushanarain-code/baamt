import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt
import textwrap
import io
import base64

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="BAAMT - Behavioural Advocacy and Messaging Tool",
    layout="wide"
)

# -----------------------
# INSTRUCTIONS & THEORETICAL FRAMEWORK
# -----------------------
st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")
st.markdown("""
BAAMT helps advocacy organizations design messaging strategies that align with the moral values of their target audience.

### Theoretical Framework
BAAMT is grounded in **Moral Foundations Theory**, which identifies key moral values that influence people's reactions to messages: 

- **Care / Harm**: sensitivity to suffering and well-being  
- **Fairness / Cheating**: concern for equality and justice  
- **Loyalty / Betrayal**: attachment to group, community, or nation  
- **Authority / Subversion**: respect for rules, traditions, and hierarchy  
- **Purity / Sanctity**: concern for cleanliness, morality, and sacredness  

Understanding these foundations allows advocates to frame messages in ways that resonate deeply with their audience.
""")

st.markdown("### Audience Context")
st.info("Please select the audience information below. These dimensions help tailor the messaging strategy:")

# -----------------------
# AUDIENCE CONTEXT
# -----------------------
audience = st.selectbox("Select Target Audience", ["General Public", "Policy Makers", "Activists", "Community Leaders"])
geography = st.selectbox("Select Geography", ["India", "Global", "Urban", "Rural"])
stakeholder = st.selectbox("Select Stakeholder Type", ["Individual", "Organization", "Media"])
campaign = st.selectbox("Select Campaign Type", ["Behaviour Change", "Policy Reform", "Awareness Raising"])

st.markdown("### Behavioural Assessment")
st.info("Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree). Try to answer based on the target audience’s likely perspective.")

# Example assessment questions
questions = [
    "Preventing suffering should be a top priority in public policy.",
    "Fair treatment matters even if it requires economic trade-offs.",
    "Society functions best when people respect authority and institutions.",
    "Loyalty to one's community should guide political decision-making.",
    "Purity and moral cleanliness are important social values."
]

responses = {}
for q in questions:
    responses[q] = st.slider(q, 1, 5, 3)

# -----------------------
# SIMULATED RESULTS (replace with your calculations)
# -----------------------
segment = "Mixed moral audiences whose responses depend on context and coalition-based messaging. They may support certain reforms but remain cautious about risk."
reform = "This audience is receptive to transformative or disruptive advocacy narratives that challenge existing systems and emphasise the need for deeper social change, though they may require clear examples."
risk = "Moderate sensitivity to moral risk. Advocacy messaging should highlight empirical evidence, harm reduction, and social progress narratives in a clear and understandable way."
trust = "Generally respects institutions but may question authority if it conflicts with ethical standards or community values."
lever = "Primary advocacy lever: Compassion and fairness, supported by credible evidence and storytelling."
geo = "Adjust messaging based on local cultural norms, language, and examples relevant to the geography chosen."
strategy = "Campaign Strategy Plan: Use a combination of emotional appeals (care/harm) and fairness appeals, with concrete examples and coalition partners to reinforce credibility."
brief = "Full Advocacy Strategy Brief: Targeted messaging that combines moral framing, stakeholder alignment, and evidence-based narratives to maximize engagement and desired behavioural outcomes."
framing = "Message Framing Examples: Highlight preventing suffering, fairness in resource distribution, respecting cultural traditions, and protecting vulnerable groups."
coalition = "Coalition Strategy: Partner with local NGOs, community leaders, and media to amplify messages and increase trust."
policy = "Policy Pathway: Recommend actionable, evidence-based steps that align with audience values and reduce resistance."
risk_analysis = "Opposition Risk Analysis: Identify stakeholders who may oppose reform and preemptively address their concerns with factual, moral, and emotional arguments."

# -----------------------
# RADAR CHART
# -----------------------
import numpy as np

st.subheader("Audience Moral Profile Radar Chart")
moral_scores = [responses[questions[i]] for i in range(len(questions))]
labels = ["Care", "Fairness", "Authority", "Loyalty", "Purity"]
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
moral_scores += moral_scores[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
ax.plot(angles, moral_scores, color='red', linewidth=2, linestyle='solid')
ax.fill(angles, moral_scores, color='red', alpha=0.25)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_ylim(0,5)
st.pyplot(fig)

# -----------------------
# GENERATE PDF
# -----------------------
if st.button("Generate BAAMT Strategy Report"):
    
    pdf = FPDF()
    pdf.add_page()
    
    # Unicode-safe font
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    
    pdf.set_font("DejaVu", "", 12)
    pdf.ln(5)
    pdf.cell(0, 8, f"Audience: {audience}", ln=True)
    pdf.cell(0, 8, f"Geography: {geography}", ln=True)
    pdf.cell(0, 8, f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(0, 8, f"Campaign Objective: {campaign}", ln=True)
    pdf.ln(5)
    
    def add_section(title, text):
        pdf.set_font("DejaVu", "B", 12)
        pdf.cell(0, 8, title, ln=True)
        pdf.set_font("DejaVu", "", 11)
        for line in textwrap.wrap(text, 90):
            pdf.cell(0, 7, line, ln=True)
        pdf.ln(2)
    
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
    
    # Insert radar chart into PDF
    chart_path = "radar_chart.png"
    fig.savefig(chart_path)
    pdf.image(chart_path, x=30, w=150)
    
    # Output PDF as bytes
    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    
    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )
    
    # -----------------------
    # EMAIL OPTION
    # -----------------------
    st.markdown("### Share Report via Email")
    email_address = st.text_input("Enter recipient email address")
    if st.button("Send Report"):
        if email_address:
            # Create mailto link
            b64 = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="mailto:{email_address}?subject=BAAMT Report&body=Please find the BAAMT report attached.&attachment=BAAMT_report.pdf">Click here to send the report</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.error("Please enter a valid email address")
