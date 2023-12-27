import streamlit as st

# Streamlit page configuration
st.title("Subscription Service Pricing Calculator")

# Input fields with default values
role = st.text_input("Enter the Role", value="Wordpress Developer")
annual_salary = st.number_input("Enter the Average Annual Salary", min_value=0, value=50000)
hours_per_client_per_day = st.number_input("Enter Number of Hours per Client per Day", min_value=1, max_value=8, value=8)
number_of_clients = st.number_input("Enter Number of Clients", min_value=1, value=1)
number_of_developers = st.number_input("Enter Number of Developers", min_value=1, value=1)
utilization_rate = st.number_input("Enter Utilization Rate (%)", min_value=0, max_value=100, value=100, help="Percentage of working hours that are billable.")

# Constants
WORKING_DAYS_PER_YEAR = 250
HOURS_IN_WORKDAY = 8
MONTHS_IN_YEAR = 12
WORKING_DAYS_PER_MONTH = WORKING_DAYS_PER_YEAR / MONTHS_IN_YEAR

# Button for calculation
if st.button("Calculate Costs and Profits"):
    if annual_salary > 0 and hours_per_client_per_day > 0 and number_of_clients > 0 and number_of_developers > 0 and utilization_rate > 0:
        # Calculations
        monthly_cost_per_developer = annual_salary / MONTHS_IN_YEAR
        monthly_cost = monthly_cost_per_developer * number_of_developers
        full_monthly_salary = annual_salary / MONTHS_IN_YEAR

        # Adjust for Utilization Rate
        total_available_hours_per_month = WORKING_DAYS_PER_MONTH * HOURS_IN_WORKDAY * (utilization_rate / 100)
        total_adjusted_hours_per_month = total_available_hours_per_month * number_of_developers
        booked_hours_per_month = number_of_clients * hours_per_client_per_day * WORKING_DAYS_PER_MONTH
        
        # Developer Time Utilization calculation
        utilization_ratio = booked_hours_per_month / total_adjusted_hours_per_month

        # Calculate the amount to invoice per client
        cost_per_client = monthly_cost / number_of_clients
        invoice_per_client = cost_per_client

        # Revenue and Net Profit Calculations
        revenue_per_client = invoice_per_client * 1.20
        total_revenue = revenue_per_client * number_of_clients
        net_profit = total_revenue - monthly_cost

        # Display results
        st.markdown("### Financial Analysis")
        st.write(f"Monthly Cost of {number_of_developers} Developer(s): ${round(monthly_cost)}")
        st.write(f"Monthly Cost per Developer: ${round(monthly_cost_per_developer)}")
        st.write(f"Monthly Developer Time Utilization: {round(booked_hours_per_month)}/{round(total_adjusted_hours_per_month)} hours ({utilization_ratio:.2%})")
        if utilization_ratio > 1:
            st.warning("You are using more hours than available. This indicates you are using more developers than you have.")
        else:
            st.success("You are using less hours than available. This indicates you have more developers than you need.")
        st.write(f"Monthly Each client gets {round(hours_per_client_per_day * WORKING_DAYS_PER_MONTH)} hours per month.")
        st.write(f"Monthly Amount to Invoice per Client: ${round(invoice_per_client)}")
        st.write(f"Monthly Amount to Invoice per Client + 20% Profit: ${round(revenue_per_client)}")
        st.write(f"Monthly By opting for this service, customers pay {round(100 * (1 - invoice_per_client / full_monthly_salary))}% less than the full monthly salary of ${full_monthly_salary:.2f}.")
        st.write(f"Monthly Revenue per Client: ${round(revenue_per_client)}")
        st.write(f"Monthly Profit per Client: ${round(revenue_per_client - cost_per_client)}")
        st.write(f"Monthly Total Revenue from Clients: ${round(total_revenue)}")
        st.write(f"Monthly Net Profit: ${round(net_profit)}")
    else:
        st.error("Please enter valid values.")
