from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAdd(Action):
    def name(self) -> Text:
        return "action_add"  

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num1 = tracker.get_slot("number_1")
        num2 = tracker.get_slot("number_2")
        sum = int(num1) + int(num2)
        dispatcher.utter_message(text= "The sum of {number_1} and {number_2} is {sum}.")
        return []


class ActionSubtract(Action):
    def name(self) -> Text:
        return "action_subtract"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num1 = tracker.get_slot("number_1")
        num2 = tracker.get_slot("number_2")
        diff = int(num1) - int(num2)
        if(diff<0):
            dispatcher.utter_message( text= "The difference between {number_1} and {number_2} is -{diff}.")
        else:
            dispatcher.utter_message( text= "The difference between {number_1} and {number_2} is {diff}.")
        return []


class ActionMultiply(Action):
    def name(self) -> Text:
        return "action_multiply"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num1 = tracker.get_slot("number_1")
        num2 = tracker.get_slot("number_2")
        product = int(num1) * int(num2)
        dispatcher.utter_message(text= "The product of {number_1} and {number_2} is {product}.")
        return []


class ActionDivide(Action):
    def name(self) -> Text:
        return "action_divide"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num1 = tracker.get_slot("number_1")
        num2 = tracker.get_slot("number_2")
        if int(num2) == 0:
            dispatcher.utter_message( text= "Sorry, I can't divide {number_1} by {number_2} because the second number is zero.")
        else:
            quotient = int(num1) / int(num2)
            dispatcher.utter_message(text= "{number_1} divided by {number_2} is {quotient}.")
        return []
