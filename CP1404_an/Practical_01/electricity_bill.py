"""
CP1404 -electricity_bill.py
extension
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
kwh_price = int(input("""Which Tariff are you using?
Tariff 11 or 31?
>>> """))
daily_use = float(input("Daily use in kWh: "))
billing_days = int(input("Number of billing days: "))
total = kwh_price * daily_use * billing_days
print(f"Bill: ${total:,.2f}")


