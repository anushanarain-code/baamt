import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
Advocacy campaigns often fail because they assume all audiences respond to the same moral arguments.

**BAAMT (Behavioural Advocacy and Messaging Tool)** helps advocacy organisations identify the **moral values most salient to a target audience**, and suggests **strategic messaging frames** based on behavioural science research.

Complete the assessment below to generate an **audience moral profile and messaging strategy**.
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

st.markdown("Rate the following statements from **1 (Strongly Disagree)** to **5 (Strongly Agree)**.")

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
# GENERATE STRATEGY BUTTON
# ---------------------------------------------------

generate = st.button("Generate Behavioural Strategy")

# ---------------------------------------------------
# RESULTS
# ---------------------------------------------------

if generate:

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
    # RADAR CHART
    # ---------------------------------------------------

    st.subheader("Moral Foundations Profile")

    labels = ['Care', 'Fairness', 'Authority', 'Loyalty', 'Purity']
    values = [care_score, fairness_score, authority_score, loyalty_score, purity_score]

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)

    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)

    st.pyplot(fig)

    st.markdown("---")

    # ---------------------------------------------------
    # AUDIENCE SEGMENTATION
    # ---------------------------------------------------

    if care_score > 4 and fairness_score > 4:
        audience_profile = "Compassion-driven reform audience"

    elif authority_score > 4:
        audience_profile = "Institutionally oriented audience"

    elif loyalty_score > 4:
        audience_profile = "Community identity audience"

    elif purity_score > 4:
        audience_profile = "Moral purity audience"

    else:
        audience_profile = "Mixed moral orientation audience"

    st.subheader("Audience Behavioural Segment")

    st.write(audience_profile)

    st.markdown("---")

    # ---------------------------------------------------
    # DOMINANT VALUE
    # ---------------------------------------------------

    dominant_value = max(
        care_score,
        fairness_score,
        authority_score,
        loyalty_score,
        purity_score
    )

    st.header("Recommended Messaging Strategy")

    # ---------------------------------------------------
    # CARE FRAME
    # ---------------------------------------------------

    if dominant_value == care_score:

        st.success("Primary Frame: Compassion and Harm Reduction")

        st.write("Strategic Guidance:")
        st.write("- Emphasize suffering and protection of vulnerable beings")
        st.write("- Use emotional storytelling")
        st.write("- Highlight moral responsibility to reduce harm")

        st.subheader("Example Campaign Message")

        st.info(
            "Every year millions of animals suffer in factory farms. "
            "By choosing plant-based foods we can prevent immense suffering."
        )

    # ---------------------------------------------------
    # FAIRNESS FRAME
    # ---------------------------------------------------

    elif dominant_value == fairness_score:

        st.success("Primary Frame: Justice and Fairness")

        st.write("Strategic Guidance:")
        st.write("- Frame issue as injustice or unfair system")
        st.write("- Highlight economic inequities")
        st.write("- Emphasize ethical responsibility")

        st.subheader("Example Campaign Message")

        st.info(
            "Taxpayers subsidize industries that harm animals and the environment. "
            "A fair food system should support sustainable alternatives."
        )

    # ---------------------------------------------------
    # AUTHORITY FRAME
    # ---------------------------------------------------

    elif dominant_value == authority_score:

        st.success("Primary Frame: Institutional Responsibility")

        st.write("Strategic Guidance:")
        st.write("- Emphasize regulation and governance")
        st.write("- Use expert endorsements")
        st.write("- Highlight responsible leadership")

        st.subheader("Example Campaign Message")

        st.info(
            "Stronger regulation is needed to ensure responsible treatment of animals "
            "and protect public health."
        )

    # ---------------------------------------------------
    # LOYALTY FRAME
    # ---------------------------------------------------

    elif dominant_value == loyalty_score:

        st.success("Primary Frame: Community Protection")

        st.write("Strategic Guidance:")
        st.write("- Frame issue as protecting shared values")
        st.write("- Use collective identity messaging")
        st.write("- Appeal to cultural responsibility")

        st.subheader("Example Campaign Message")

        st.info(
            "Protecting animals and the environment is part of protecting our "
            "shared national values and future generations."
        )

    # ---------------------------------------------------
    # PURITY FRAME
    # ---------------------------------------------------

    else:

        st.success("Primary Frame: Moral Integrity and Purity")

        st.write("Strategic Guidance:")
        st.write("- Emphasize clean and ethical consumption")
        st.write("- Highlight contamination and moral degradation")
        st.write("- Promote purity of lifestyle choices")

        st.subheader("Example Campaign Message")

        st.info(
            "Choosing plant-based foods is a cleaner and more ethical way "
            "to live in harmony with nature."
        )

    st.markdown("---")

    st.info(
        "BAAMT provides behavioural guidance for advocacy messaging. "
        "Strategies should always be adapted to the cultural and political context."
    )
