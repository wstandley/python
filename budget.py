"""
    This is for assignemnt PE1 2.6: Interacting with the User: Input
    This helps calculate a monthly budget.
    In my programs case "m" stands for monthly and "p" stands for percentage. 
"""

# Variables
total_month = 0
total_budget_left = 0

# Input Lines

m_budget = float(input("What is your total monthly budget? ")) # Total Budget

m_housing = float(input("How much is your rent/mortgage? "))
m_utilities = float(input("How much is your average utility bill? "))
m_groceries = float(input("How much do you spend, on average, on groceries monthly? "))
m_transportation = float(input("How much do you spend, on average, monthly on transportation? "))
m_health_care = float(input("How much do you spend monthly, on average, on health care? "))
m_personal_care = float(input("How much do you spend monthly, on average, on personal care? "))
m_clothing = float(input("How much do you spend monthly, on average, on clothing? "))
m_debt = float(input("How much do you spend monthly, on average, on paying off debts? "))

total_month = m_housing + m_utilities + m_groceries +  m_transportation + m_health_care + m_personal_care + m_clothing + m_debt
# Total Monthly Spending

# Percentage Calculations

p_housing = (m_housing / m_budget) * 100
p_utilities = (m_utilities / m_budget) * 100
p_groceries = (m_groceries / m_budget) * 100
p_transportation = (m_transportation / m_budget) * 100
p_health_care = (m_health_care / m_budget) * 100
p_personal_care = (m_personal_care / m_budget) * 100
p_clothing = (m_clothing / m_budget) * 100
p_debt = (m_debt / m_budget) * 100

# Percent of monthly budget used

p_budget_used = (total_month / m_budget) * 100

# Print Statement

print(f"Currently you are spending %{p_budget_used:.2f} of your monthly budget. \n\nEach category uses as follows of your monthly budget: \n\nHousing:  %{p_housing:.2f} \nUtilities:  %{p_utilities:.2f} \nGroceries:  %{p_groceries:.2f} \nTransportation:  %{p_transportation:.2f} \nHealth Care:  %{p_health_care:.2f} \nPersonal Care:  %{p_personal_care:.2f} \nClothing:  %{p_clothing:.2f} \nDebt:  %{p_debt:.2f}")