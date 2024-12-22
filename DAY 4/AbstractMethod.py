from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def process_payment(self):
        print("Default Payment")

class CreditCardPayment(Payment):

    def process_payment(self):
        print("Creadit Card Payment")

    def show_payment():
        pass

cardPayment = CreditCardPayment()
cardPayment.process_payment()