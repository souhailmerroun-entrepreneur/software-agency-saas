import streamlit as st

# Streamlit page configuration
st.title("Subscription Service Pricing Calculator")

# Input fields with default values
role = st.text_input("Enter the Role", value="Wordpress Developer")
annual_salary = st.number_input("Enter the Average Annual Salary", min_value=0, value=54000)
hours_per_client = st.number_input("Enter Number of Hours per Client", min_value=1, max_value=8, value=2)
number_of_clients = st.number_input("Enter Number of Clients", min_value=1, value=1)
number_of_developers = st.number_input("Enter Number of Developers", min_value=1, value=1)

# Constants
WORKING_DAYS_PER_YEAR = 250
HOURS_IN_WORKDAY = 8
ADDITIONAL_MARGIN_PER_CLIENT = 0.10  # 10% additional margin
MONTHS_IN_YEAR = 12

# Button for calculation
if st.button("Calculate Costs and Profits"):
    if annual_salary > 0 and hours_per_client > 0 and number_of_clients > 0 and number_of_developers > 0:
        # Calculations
        daily_cost_per_developer = annual_salary / WORKING_DAYS_PER_YEAR
        monthly_cost_per_developer = annual_salary / MONTHS_IN_YEAR  # Correct monthly cost calculation
        monthly_cost = monthly_cost_per_developer * number_of_developers  # Total cost for all developers
        full_monthly_salary = annual_salary / MONTHS_IN_YEAR
        total_hours_per_month_per_developer = WORKING_DAYS_PER_YEAR / MONTHS_IN_YEAR * HOURS_IN_WORKDAY
        total_hours_per_month = total_hours_per_month_per_developer * number_of_developers
        booked_hours_per_month = number_of_clients * hours_per_client * (WORKING_DAYS_PER_YEAR / MONTHS_IN_YEAR)
        
        # Adjusted Developer Time Utilization calculation
        utilization_ratio = booked_hours_per_month / total_hours_per_month

        # Calculate the amount to invoice per client
        clients_needed = (HOURS_IN_WORKDAY / hours_per_client) * number_of_developers
        cost_per_client = monthly_cost / clients_needed
        invoice_per_client = cost_per_client * (1 + ADDITIONAL_MARGIN_PER_CLIENT)

        # Revenue and Net Profit Calculations
        total_revenue = invoice_per_client * number_of_clients
        net_profit = total_revenue - monthly_cost

        # Revenue per Client
        revenue_per_client = invoice_per_client * 1.10  # includes the 10% profit margin

        # Profit per Client
        profit_per_client = revenue_per_client - cost_per_client

        # Percentage savings calculation
        savings_percentage = 100 * (1 - revenue_per_client / full_monthly_salary)

        # Display results
        st.markdown("### Financial Analysis")
        st.write(f"Monthly Cost of {number_of_developers} Developer(s): ${round(monthly_cost)}")
        st.write(f"Monthly Cost per Developer: ${round(monthly_cost_per_developer)}")
        st.write(f"Monthlu Developer Time Utilization: {round(booked_hours_per_month)}/{round(total_hours_per_month)} hours ({utilization_ratio:.2%})")
        st.write(f"Monthly Each client gets {round(hours_per_client * WORKING_DAYS_PER_YEAR / MONTHS_IN_YEAR)} hours per month.")
        st.write(f"Monthly Amount to Invoice per Client: ${round(invoice_per_client)}")
        st.write(f"Monthly Amount to Invoice per Client + 10% Profit: ${round(invoice_per_client * 1.10)}")
        st.write(f"Monthly By opting for this service, customers pay {round(savings_percentage)}% less than the full monthly salary of ${full_monthly_salary:.2f}.")
        st.write(f"Monthly Revenue per Client: ${round(revenue_per_client)}")
        st.write(f"Monthly Profit per Client: ${round(profit_per_client)}")
        st.write(f"Monthly Total Revenue from Clients: ${round(total_revenue)}")
        st.write(f"Monthly Net Profit: ${round(net_profit)}")
    else:
        st.error("Please enter valid values.")
