import streamlit as st
from fpdf import FPDF
import textwrap
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="BAAMT Tool", layout="wide")

# ---------- INSTRUCTION ----------
st.title("🧠 BAAMT")
st.markdown("""
**Behavioural Advocacy and Messaging Tool (BAAMT)** helps advocacy organizations design messaging strategies based on the moral values of their target audience.  
Complete the assessment below to generate a behavioural profile, radar chart, and recommended messaging strategy. Please answer honestly based on your knowledge of the target audience.
""")

# ---------- AUDIENCE CONTEXT ----------
st.subheader("Audience Information")
audience = st.selectbox("Select Target Audience", ["General Public", "Policy Makers", "Activists"])
geography = st.selectbox("Select Geography", ["India", "USA", "UK", "Global"])
stakeholder = st.selectbox("Select Stakeholder Type", ["NGO", "Government", "Corporation", "Community Group"])
campaign = st.selectbox("Select Campaign Objective", ["Behaviour Change", "Policy Advocacy", "Awareness Raising"])

# ---------- BEHAVIOURAL ASSESSMENT ----------
st.subheader("Behavioural Assessment")
care = st.slider("Preventing suffering should be a top priority in public policy.", 1, 5, 3)
fairness = st.slider("Fair treatment matters even if it requires economic trade-offs.", 1, 5, 3)
authority = st.slider("Society functions best when people respect authority and institutions.", 1, 5, 3)
loyalty = st.slider("Loyalty to one's community should guide political decision-making.", 1, 5, 3)
purity = st.slider("Purity and moral cleanliness are important social values.", 1, 5, 3)

# ---------- RESULTS CALCULATION (example logic) ----------
segment = "Mixed moral audiences whose responses are likely to depend on contextual framing and coalition-based messaging. They may value fairness and care, but their reactions can change depending on cultural or situational cues."
reform = "This audience may be receptive to more transformative or disruptive advocacy narratives that challenge existing systems and emphasise the need for deeper social change. Messaging should include concrete examples of positive societal transformation."
risk = "Moderate sensitivity to moral risk. Advocacy messaging can focus on empirical evidence, harm reduction, and clear, relatable narratives to demonstrate impact without overwhelming the audience."
trust = "Trust in institutions varies; some audiences will respect government and NGO guidance, while others will prioritize community leaders. Messages should balance authority appeal with relatable social proof."
lever = "Primary advocacy lever: Emphasize compassion and concrete benefits for vulnerable populations. Combine moral appeals with actionable steps to engage the audience."
geo = f"Adjust messaging based on local cultural norms, legal frameworks, and regional priorities for {geography}. Use local examples to make content more relatable."
strategy = "Campaign Strategy Plan: Use coalition-based outreach, social proof, and storytelling to communicate policy or behaviour changes effectively. Segment messages by moral foundation emphasis."
brief = "Full Advocacy Strategy Brief: Provide actionable recommendations tailored to the target audience, ensuring messaging aligns with their moral foundations and contextual factors. Include concrete examples, narratives, and suggested channels."
framing = "Example: Highlight stories of individuals positively affected by the proposed policy changes, combined with factual harm reduction evidence to appeal to care and fairness foundations."
coalition = "Form coalitions with local influencers, NGOs, and community leaders who embody the moral values of the target audience."
policy = "Identify realistic policy pathways and highlight previous successful examples to provide credibility and feasibility."
risk_analysis = "Assess opposition arguments and potential backlash. Prepare counter-messaging grounded in moral and empirical reasoning."

# ---------- GENERATE AND DOWNLOAD PDF ----------
if st.button("Generate BAAMT Strategy Report"):

    # Display results in app
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

    # ---------- PDF SETUP ----------
    pdf = FPDF()
    pdf.add_page()

    # Add Unicode font
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    def add_section(title, text):
        pdf.ln(4)
        pdf.set_font("DejaVu", "B", 12)
        pdf.cell(0, 8, title, ln=True)
        pdf.set_font("DejaVu", "", 11)
        wrapped = textwrap.wrap(text, 90)
        for line in wrapped:
            pdf.cell(0, 7, line, ln=True)

    # ---------- PDF HEADER ----------
    pdf.set_font("DejaVu", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    pdf.ln(5)
    pdf.set_font("DejaVu", "", 11)
    pdf.cell(0, 8, f"Audience: {audience}", ln=True)
    pdf.cell(0, 8, f"Geography: {geography}", ln=True)
    pdf.cell(0, 8, f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(0, 8, f"Campaign Objective: {campaign}", ln=True)

    # ---------- ADD SECTIONS ----------
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

    # ---------- RADAR CHART ----------
    labels = ['Care', 'Fairness', 'Authority', 'Loyalty', 'Purity']
    values = [care, fairness, authority, loyalty, purity]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values += values[:1]  # close the loop
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    ax.plot(angles, values, color='red', linewidth=2)
    ax.fill(angles, values, color='red', alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_title("Audience Moral Foundations Radar Chart", fontsize=10)

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='PNG', bbox_inches='tight')
    plt.close(fig)
    img_buffer.seek(0)
    pdf.ln(5)
    pdf.image(img_buffer, x=30, w=150)

    # ---------- DOWNLOAD PDF ----------
    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )
