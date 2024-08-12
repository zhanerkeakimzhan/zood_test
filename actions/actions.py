from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker # type: ignore
from rasa_sdk.executor import CollectingDispatcher # type: ignore
from rasa_sdk.events import ActionExecuted, Restarted # type: ignore
import random

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
    
class ActionOperator(Action):

    def name(self) -> Text:
        return "action_restart_robot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [Restarted()]