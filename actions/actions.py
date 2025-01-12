from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from cryptography.fernet import Fernet
import json

# Encryption setup
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data.encode()).decode()

# Custom action to add a transaction
class ActionAddTransaction(Action):
    def name(self):
        return "action_add_transaction"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        amount = tracker.get_slot("amount")
        category = tracker.get_slot("category")

        if amount and category:
            encrypted_data = encrypt_data(json.dumps({"amount": amount, "category": category}))
            print(f"Encrypted Transaction: {encrypted_data}")
            print(f"Decrypted Transaction: {decrypt_data(encrypted_data)}")

            dispatcher.utter_message(text=f"Transaction of ${amount} under '{category}' added successfully.")
            return [SlotSet("amount", None), SlotSet("category", None)]
        else:
            dispatcher.utter_message(text="I need both amount and category to add the transaction.")
            return []
