import streamlit as st
from fpdf import FPDF
import textwrap

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="BAAMT: Behavioural Advocacy & Messaging Tool",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------- HEADER -------------------
st.title("🧠 BAAMT")
st.markdown("""
**Behavioural Advocacy and Messaging Tool (BAAMT)**  
BAAMT helps advocacy organizations design messaging strategies that align with the moral values and priorities of their target audience.  

Please complete the assessment below to generate a detailed behavioural profile and recommended messaging strategy. The tool is designed to provide insights in a way that is understandable and actionable for advocacy planning.
""")

# ------------------- AUDIENCE CONTEXT -------------------
st.subheader("Audience Information")
st.markdown("Provide information about the target audience to tailor the behavioural insights and messaging recommendations. This context helps BAAMT generate more relevant and actionable strategies.")

audience = st.selectbox("Select Target Audience", ["General Public", "Policy Makers", "Corporate Stakeholders"])
geography = st.selectbox("Select Geography", ["India", "USA", "UK", "Global"])
stakeholder = st.selectbox("Select Stakeholder Segment", ["Urban", "Rural", "Youth", "Women", "Other"])
campaign = st.selectbox("Select Campaign Type", ["Behaviour Change", "Policy Advocacy", "Corporate Engagement"])

# ------------------- BEHAVIOURAL ASSESSMENT -------------------
st.subheader("Behavioural Assessment")
st.markdown("""
Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree).  
These statements are designed based on **Moral Foundations Theory**, which posits that human moral reasoning is guided by several foundational values such as care, fairness, loyalty, authority, and purity.  
Your answers will help us identify which moral values are most salient for your audience.
""")

questions = {
    "Preventing suffering should be a top priority in public policy.": 0,
    "Fair treatment matters even if it requires economic trade-offs.": 0,
    "Society functions best when people respect authority and institutions.": 0,
    "Loyalty to one's community should guide political decision-making.": 0,
    "Purity and moral cleanliness are important social values.": 0,
    "Avoiding harm to vulnerable beings is an ethical responsibility.": 0,
    "Rules and laws should be followed even when inconvenient.": 0,
    "People should prioritize fairness in markets and economic systems.": 0,
    "Communities should protect their cultural traditions.": 0,
    "Certain practices are morally wrong regardless of consequences.": 0,
}

responses = {}
for q in questions:
    responses[q] = st.slider(q, 1, 5, 3)

# ------------------- PROCESS RESULTS -------------------
# For demonstration, we generate some placeholder outputs
segment = "Mixed moral audiences whose responses are likely to depend on the context and the framing of messages. They may be more responsive when advocacy messages are framed with relatable examples and stories."
reform = "This audience may be open to transformative or progressive narratives, emphasizing social change, fairness, and responsible stewardship of resources."
risk = "Moderate sensitivity to moral and social risk. Messaging can highlight evidence-based harm reduction and community benefits without being confrontational."
trust = "Institutional trust varies; audiences may respond positively to transparent, credible, and consistent messaging from trusted sources."
lever = "Primary advocacy lever should emphasize compassion, fairness, and collective responsibility while showing practical benefits of action."
geo = f"Adjust messaging to local cultural, social, and economic context within {geography} to enhance relevance and engagement."
strategy = "Campaign strategy should combine storytelling, social proof, and actionable steps that clearly illustrate how taking action reduces harm and increases fairness."
brief = "Full advocacy strategy integrates moral framing, audience segmentation, and contextual tailoring to ensure maximum impact. Include multiple examples, case studies, and concrete calls to action."
framing = "Messages should highlight real-life examples of harm reduction, fairness, and ethical responsibility, and include stories about individuals or communities positively impacted by advocacy actions."
coalition = "Partner with local organizations, influencers, and community leaders to amplify reach and credibility."
policy = "Identify existing policy levers, regulatory frameworks, and institutional entry points for advocacy interventions."
risk_analysis = "Assess potential opposition, societal backlash, or misunderstandings that could reduce message effectiveness and plan mitigation strategies."

# ------------------- GENERATE REPORT BUTTON -------------------
if st.button("Generate BAAMT Strategy Report"):

    # Display all results in Streamlit
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

    # ------------------- PDF REPORT -------------------
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
        pdf.cell(0, 8, title, ln=True)
        pdf.set_font("Arial", "", 11)
        wrapped = textwrap.wrap(text, 90)
        for line in wrapped:
            pdf.multi_cell(0, 7, line)  # Using multi_cell to handle line breaks

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

    pdf_bytes = pdf.output(dest="S").encode("latin-1")

    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf",
    )

    # ------------------- EMAIL SHARING OPTION -------------------
    st.markdown("""
    **Share your BAAMT report via email**  
    Copy the downloaded PDF and attach it in your email client to share with colleagues, partners, or stakeholders.  
    In the future, we can integrate a direct email feature to send the report from within the app.
    """)
