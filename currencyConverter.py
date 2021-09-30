from currency_converter import CurrencyConverter
import locale
c = CurrencyConverter()

amount = float(input("Enter the amount: "))
x = input("Enter your currency: ").upper()
y = input("Enter the currency you're trying to convert to: ").upper()
locale.setlocale(locale.LC_ALL, y)

amount = locale.currency(c.convert(amount, x, y), symbol= True, grouping= True)

print(amount, y)

