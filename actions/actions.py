from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker # type: ignore
from rasa_sdk.executor import CollectingDispatcher # type: ignore
from rasa_sdk.events import ActionExecuted, Restarted # type: ignore
import random
import logging

class ActionRepeat(Action):
    def name(self) -> Text:
        return "action_repeat"
    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        events = tracker.events
        all_utters = []
        user_event_encountered = False
        for event in reversed(events):
            if event['event'] == 'user' and user_event_encountered:
                break
            elif event['event'] == 'user':
                user_event_encountered = True
            elif user_event_encountered and event['event'] == 'action' and event['name'].startswith('utter'):
                all_utters.append(event['name'])
        print(all_utters)

        for utter in reversed(all_utters):
            response = utter
            dispatcher.utter_message(response=response)

        return [ActionExecuted(response)]

class ActionOperatorRU(Action):
    def name(self) -> Text:
        return "action_operatorRU"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        events = tracker.events
        action_names = [event.get('name') for event in events if event.get('event') == 'action']
        print(f"Collected action_names: {action_names}")

        has_operatorRU = False
        has_operatorUZ = False

        for action_name in action_names:
            if action_name == 'action_operatorRU':
                has_operatorRU = True
            elif action_name == 'action_operatorUZ':
                has_operatorUZ = True
        
        if has_operatorRU or has_operatorUZ:
            response = 'utter_operator2RU'
        else:
            response = 'utter_operatorRU'

        dispatcher.utter_message(response=response)

        return [ActionExecuted(response)]

class ActionOperatorRU(Action):
    def name(self) -> Text:
        return "action_operatorUZ"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        events = tracker.events
        action_names = [event.get('name') for event in events if event.get('event') == 'action']
        print(f"Collected action_names: {action_names}")

        has_operatorRU = False
        has_operatorUZ = False

        for action_name in action_names:
            if action_name == 'action_operatorRU':
                has_operatorRU = True
            elif action_name == 'action_operatorUZ':
                has_operatorUZ = True
        
        if has_operatorRU or has_operatorUZ:
            response = 'utter_operator2UZ'
        else:
            response = 'utter_operatorUZ'

        dispatcher.utter_message(response=response)

        return [ActionExecuted(response)]

class ActionRestart(Action):

    def name(self) -> Text:
        return "action_restart_robot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [Restarted()]