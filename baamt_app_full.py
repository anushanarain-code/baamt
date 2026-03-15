import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="BAAMT",
    page_icon="🧠",
    layout="centered"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")

st.markdown("""
BAAMT helps advocacy organizations design messaging strategies based on
the moral values of their target audience.

Complete the assessment below to generate a behavioural profile and
recommended messaging strategy.
""")

st.markdown("---")

# ---------------------------------------------------
# AUDIENCE INFORMATION
# ---------------------------------------------------

st.header("Audience Information")

audience_type = st.selectbox(
    "Select Target Audience",
    [
        "General Public",
        "Students",
        "Policy Makers",
        "Industry Stakeholders",
        "Civil Society",
        "Other"
    ]
)

geography = st.selectbox(
    "Select Geography",
    [
        "India",
        "Global",
        "Other"
    ]
)

campaign_type = st.selectbox(
    "Select Campaign Type",
    [
        "Behaviour Change",
        "Policy Advocacy",
        "Corporate Engagement",
        "Public Awareness"
    ]
)

st.markdown("---")

# ---------------------------------------------------
# MORAL QUESTIONNAIRE
# ---------------------------------------------------

st.header("Behavioural Assessment")

st.markdown("Rate the following statements from **1 (Strongly Disagree) to 5 (Strongly Agree)**.")

q1 = st.slider("Preventing suffering should be a top priority in public policy.", 1, 5)
q2 = st.slider("Fair treatment matters even if it requires economic trade-offs.", 1, 5)
q3 = st.slider("Society functions best when people respect authority and institutions.", 1, 5)
q4 = st.slider("Loyalty to one's community should guide political decision-making.", 1, 5)
q5 = st.slider("Purity and moral cleanliness are important social values.", 1, 5)

q6 = st.slider("Avoiding harm to vulnerable beings is an ethical responsibility.", 1, 5)
q7 = st.slider("Rules and laws should be followed even when inconvenient.", 1, 5)
q8 = st.slider("People should prioritize fairness in markets and economic systems.", 1, 5)
q9 = st.slider("Communities should protect their cultural traditions.", 1, 5)
q10 = st.slider("Certain practices are morally wrong regardless of consequences.", 1, 5)

st.markdown("---")

# ---------------------------------------------------
# CALCULATE SCORES
# ---------------------------------------------------

care_score = (q1 + q6) / 2
fairness_score = (q2 + q8) / 2
authority_score = (q3 + q7) / 2
loyalty_score = (q4 + q9) / 2
purity_score = (q5 + q10) / 2

# ---------------------------------------------------
# RESULTS
# ---------------------------------------------------

st.header("Audience Moral Profile")

st.write("Care / Harm:", round(care_score, 2))
st.progress(care_score / 5)

st.write("Fairness:", round(fairness_score, 2))
st.progress(fairness_score / 5)

st.write("Authority:", round(authority_score, 2))
st.progress(authority_score / 5)

st.write("Loyalty:", round(loyalty_score, 2))
st.progress(loyalty_score / 5)

st.write("Purity:", round(purity_score, 2))
st.progress(purity_score / 5)

st.markdown("---")

# ---------------------------------------------------
# MESSAGING STRATEGY
# ---------------------------------------------------

st.header("Recommended Messaging Strategy")

dominant_value = max(
    care_score,
    fairness_score,
    authority_score,
    loyalty_score,
    purity_score
)

if dominant_value == care_score:
    st.success(
        "Primary Frame: Compassion and harm reduction.\n\n"
        "Messaging should highlight suffering, humane responsibility, "
        "and protecting vulnerable beings."
    )

elif dominant_value == fairness_score:
    st.success(
        "Primary Frame: Justice and fairness.\n\n"
        "Messaging should focus on ethical systems, fairness, "
        "and correcting imbalances."
    )

elif dominant_value == authority_score:
    st.success(
        "Primary Frame: Respect for institutions and rules.\n\n"
        "Messaging should highlight regulation, governance, "
        "and responsible leadership."
    )

elif dominant_value == loyalty_score:
    st.success(
        "Primary Frame: Community protection.\n\n"
        "Messaging should emphasize collective responsibility, "
        "national or community values, and protecting shared identity."
    )

else:
    st.success(
        "Primary Frame: Purity and moral integrity.\n\n"
        "Messaging should focus on moral standards, "
        "ethical consumption, and avoiding contamination."
    )

st.markdown("---")

st.info("BAAMT provides indicative behavioural guidance. Messaging strategies should be adapted to local context.")
