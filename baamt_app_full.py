# baamt_app_full.py
import streamlit as st
from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Function to generate PDF
# -----------------------------
def generate_pdf(results, filename="BAAMT_Report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Helvetica", 'B', 16)
    pdf.multi_cell(0, 10, "BAAMT - Behavioural Advocacy and Messaging Tool", align='C')
    pdf.ln(5)
    pdf.set_font("Arial", size=12)

    # Add each section
    for section, text in results.items():
        pdf.set_font("Arial", 'B', 14)
        pdf.multi_cell(0, 8, str(text))
        pdf.set_font("Helvetica", size=12)
        pdf.multi_cell(0, 8, text)
        pdf.ln(5)

    pdf.output(filename)
    return filename

# -----------------------------
# Streamlit App
# -----------------------------
st.title("BAAMT - Behavioural Advocacy and Messaging Tool")
st.write("BAAMT helps advocacy organizations design messaging strategies based on the moral values of their target audience. Users answer a short questionnaire estimating how their target audience might respond to various moral statements. The tool then generates a moral communication profile and recommended advocacy strategies.")

st.write("**Instructions:** Please answer based on how strongly you believe your target audience would agree with the following statements (1=Strongly disagree, 5=Strongly agree).")

# -----------------------------
# Audience Inputs
# -----------------------------
st.subheader("Audience Information")
target_audience = st.selectbox("Select Target Audience", ["Policymakers", "Corporations", "Consumers", "Scientists", "NGOs"])
geography = st.selectbox("Select Geography", ["Global", "US", "EU", "India", "Other"])
stakeholder_level = st.selectbox("Select Stakeholder Level", ["Institutional", "Corporate", "Public"])
campaign_type = st.selectbox("Select Campaign Type", ["Awareness", "Corporate commitment", "Regulation", "Welfare standards", "Behaviour change"])

# -----------------------------
# Moral Questionnaire
# -----------------------------
st.subheader("Moral Questionnaire")
questions = [
    "1. Preventing suffering should be a top priority in public policy.",
    "2. Fair treatment matters even if it requires economic trade-offs.",
    "3. Society functions best when people respect authority and institutions.",
    "4. Loyalty to one's community should guide political decision-making.",
    "5. Purity and moral cleanliness are important social values.",
    "6. Avoiding harm to vulnerable beings is an ethical responsibility.",
    "7. Rules and laws should be followed even when inconvenient.",
    "8. People should prioritize fairness in markets and economic systems.",
    "9. Communities should protect their cultural traditions.",
    "10. Certain practices are morally wrong regardless of consequences."
]

responses = []
for q in questions:
    responses.append(st.slider(q, 1, 5, 3))

# -----------------------------
# Moral Foundation Calculation
# -----------------------------
care_score = (responses[0] + responses[5]) / 2
fairness_score = (responses[1] + responses[7]) / 2
authority_score = (responses[2] + responses[6]) / 2
loyalty_score = (responses[3] + responses[8]) / 2
purity_score = (responses[4] + responses[9]) / 2

scores = {
    "Care/Harm": care_score,
    "Fairness": fairness_score,
    "Authority": authority_score,
    "Loyalty": loyalty_score,
    "Purity": purity_score
}

primary_moral = max(scores, key=scores.get)

# -----------------------------
# Strategy Messages (sample)
# -----------------------------
strategy_texts = {
    "Care/Harm": {
        "Primary Message": "Audiences scoring highly on Care/Harm respond strongly to messaging emphasizing compassion, humane treatment, and preventing unnecessary suffering. Build campaigns around empathy and harm reduction.",
        "Secondary Message": "Use stories, visual evidence, and narratives illustrating suffering and humane solutions.",
        "Campaign Strategy": "Public awareness campaigns focused on animal welfare and harm reduction.",
        "Advocacy Lever": "Emphasize compassion, welfare standards, and humane treatment.",
        "Moral Interpretation": "Focus on empathy, care, and protection of vulnerable beings."
    },
    "Fairness": {
        "Primary Message": "Audiences scoring highly on Fairness respond to messaging highlighting justice, ethical responsibility, and equity.",
        "Secondary Message": "Use examples showing fairness in policy and corporate practices.",
        "Campaign Strategy": "Policy advocacy campaigns emphasizing fairness and equity.",
        "Advocacy Lever": "Regulatory reform and ethical standards.",
        "Moral Interpretation": "Emphasize justice and ethical responsibility."
    },
    "Authority": {
        "Primary Message": "Audiences scoring highly on Authority respond to messaging emphasizing respect for institutions and compliance with rules.",
        "Secondary Message": "Highlight standards, regulations, and institutional frameworks.",
        "Campaign Strategy": "Institutional engagement and regulatory compliance campaigns.",
        "Advocacy Lever": "Law, regulation, and institutional norms.",
        "Moral Interpretation": "Focus on respect for authority and rules."
    },
    "Loyalty": {
        "Primary Message": "Audiences scoring highly on Loyalty respond to messaging emphasizing community protection and shared values.",
        "Secondary Message": "Highlight local traditions and communal responsibility.",
        "Campaign Strategy": "Coalition building and national policy campaigns.",
        "Advocacy Lever": "Community and cultural norms.",
        "Moral Interpretation": "Focus on protecting the group and shared values."
    },
    "Purity": {
        "Primary Message": "Audiences scoring highly on Purity respond to messaging emphasizing moral cleanliness and ethical boundaries.",
        "Secondary Message": "Use examples highlighting ethical and cultural norms.",
        "Campaign Strategy": "Cultural messaging and social norms campaigns.",
        "Advocacy Lever": "Ethical and social purity.",
        "Moral Interpretation": "Focus on moral boundaries and preventing contamination."
    }
}

# -----------------------------
# Show Results
# -----------------------------
st.subheader("Audience Moral Profile")
for foundation, score in scores.items():
    st.write(f"{foundation}: {score}")

st.write(f"**Dominant Moral Foundation:** {primary_moral}")

# -----------------------------
# Bar Chart
# -----------------------------
st.subheader("Moral Foundations Chart")
plt.bar(scores.keys(), scores.values(), color='skyblue')
plt.ylim(0, 5)
plt.ylabel("Score")
plt.xlabel("Moral Foundations")
st.pyplot(plt)

# -----------------------------
# Show Strategy
# -----------------------------
st.subheader("Recommended Messaging Strategy")
strategy = strategy_texts[primary_moral]

for section, text in strategy.items():
    st.write(f"**{section}:** {text}")

# -----------------------------
# Download PDF Button
# -----------------------------
st.subheader("Download Full Strategy Report")
results_for_pdf = {
    "Audience Moral Profile": "\n".join([f"{k}: {v}" for k,v in scores.items()]),
    "Primary Message": strategy["Primary Message"],
    "Secondary Message": strategy["Secondary Message"],
    "Campaign Strategy": strategy["Campaign Strategy"],
    "Advocacy Lever": strategy["Advocacy Lever"],
    "Moral Interpretation": strategy["Moral Interpretation"],
}

# pdf_file = generate_pdf(results_for_pdf)

#st.download_button(
#    label="Download PDF Report",
#    data=open(pdf_file, "rb"),
#    file_name="BAAMT_Report.pdf",
#    mime="application/pdf"
# )
