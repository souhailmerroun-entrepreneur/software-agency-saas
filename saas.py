import streamlit as st

# Streamlit app layout
st.title("SaaS Health Metrics Calculator")

# Function to calculate SaaS health metrics
def calculate_saas_health_metrics(mrr, churn_rate, cac, ltv):
    # Monthly Recurring Revenue (MRR)
    mrr_annualized = mrr * 12

    # Assuming average customer lifetime is 3 years for LTV calculation
    average_customer_lifetime = 1
    ltv_calculated = mrr_annualized * average_customer_lifetime

    # LTV to CAC Ratio
    ltv_to_cac_ratio = ltv_calculated / cac

    # Health Summary
    if ltv_to_cac_ratio > 3 and churn_rate < 10:
        health_summary = "Healthy"
    elif ltv_to_cac_ratio > 1 and churn_rate < 20:
        health_summary = "Moderate"
    else:
        health_summary = "Needs Improvement"

    return mrr_annualized, average_customer_lifetime, ltv_to_cac_ratio, health_summary

# Input form for SaaS metrics
with st.form("saas_metrics_form"):
    st.subheader("Enter SaaS Metrics")
    mrr = st.number_input("Monthly Recurring Revenue (MRR) ($)", min_value=0)
    churn_rate = st.number_input("Churn Rate (%)", min_value=0.0, max_value=100.0)
    cac = st.number_input("Customer Acquisition Cost (CAC) ($)", min_value=0)
    ltv = mrr * 12 * 3  # Calculating LTV based on 3 years lifespan

    # Form submission button
    submit_button = st.form_submit_button("Calculate SaaS Health Metrics")

    if submit_button:
        # Calculating SaaS health metrics
        mrr_annualized, avg_customer_lifetime, ltv_to_cac_ratio, health_summary = calculate_saas_health_metrics(
            mrr, churn_rate, cac, ltv
        )

        # Displaying results
        st.subheader("Calculated SaaS Health Metrics")
        st.write(f"Annualized MRR: ${mrr_annualized}")
        st.write(f"Average Customer Lifetime: {avg_customer_lifetime} years")
        st.write(f"LTV to CAC Ratio: {ltv_to_cac_ratio}")
        st.markdown(f"**SaaS Health Summary:** {health_summary}")

        # Recap sentence
        st.markdown(f"### Overall Health Recap")
        st.write(f"This SaaS is currently **{health_summary}** with an LTV to CAC ratio of {ltv_to_cac_ratio} and a churn rate of {churn_rate}%.")

