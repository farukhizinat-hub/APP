class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class DebitCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card.")

class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

class NetBanking:
    def pay(self, amount):
        print(f"Paid ₹{amount} using NetBanking.")

class PaymentProcessor:
    def __init__(self, Payment_method):
        self.Payment_method = Payment_method

    def processor_payment(self, amount):
        self.Payment_method.pay(amount)

print("\nSelect payment method")
print("1.CreditCard")
print("2.DebitCard")
print("3.UPI")
print("4.NetBanking")

choice = int(input("Enter choice:"))
amount = int(input("Enter your amount:"))

if choice == 1:
    Payment = CreditCard()
elif choice == 2:
    Payment = DebitCard()
elif choice == 3:
    Payment = UPI()
elif choice == 4:
    Payment = NetBanking()
else:
    print("Invalid choice")
    exit()

payment = PaymentProcessor(Payment)
payment.processor_payment(amount)