# -*- coding: utf-8 -*-
import datetime
import pandas as pd
from typing import Dict, Text, Any, List, Union
from rasa_sdk.events import SlotSet,AllSlotsReset
from rasa_sdk import Action
from rasa_sdk import ActionExecutionRejection
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet, UserUtteranceReverted,ConversationPaused, FollowupAction, Form


class ActionAppointment(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "appointment_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        # type: () -> List[Text]
        """A list of required slots that the form has to fill"""

        return ["dept", "time"]

    def slot_mapping(self):
        # type: () -> Dict[Text: Union[Text, Dict, List[Text, Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"dept": self.from_entity(entity="dept",
                                            intent="schedule_appointment"),
                "time": self.from_entity(entity="time")
                }

    @staticmethod
    def dept_db():
        # type: () -> List[Text]
        """Database of supported cuisines"""
        return ['cardiology','neurology','pediatrics','family medicine','intensive care',
                        'emergency','psychiatry','opthalmology','ent','gastroenterology','gynaecology',
                        'microbiology','nephrology','oncology','orthopaedics']

    


    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
    #def validate(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """"Validate extracted requested slot else raise an error"""
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))



        for slot, value in slot_values.items():
            
            if slot == 'dept':
                if value.lower() not in self.dept_db():
                    dispatcher.utter_template('utter_incorrect_dept', tracker)
                    slot_values[slot] = None
                    # validation failed, set this slot to None
            elif slot == 'time':
                dept=tracker.get_slot('dept')
                if value[11:19] == "00:00:00":
                    dispatcher.utter_template("utter_incorrect_time",tracker)
                    slot_values[slot] = None
                else:
                    flag=0
                    file = pd.read_csv('DocAvail.csv')
                    date = value[0:10]
                    time_slot = value[11:19]
                    date_time = datetime.datetime.strptime(date,"%Y-%m-%d")
                    weekday = datetime.datetime.strftime(date_time,"%A")
                    Dept= file[file['Department'].str.lower()==dept].reset_index().drop('index',axis=1)[['Physician name',weekday]]
                    print (Dept)
                    for i in range(len(Dept)):
                        avail_time=Dept.ix[i,weekday].split('-')
                        low=int(avail_time[0].split(':')[0])
                        high=int(avail_time[1].split(':')[0])
                        time_slot_int= int(value[11:19].split(':')[0])
                        if time_slot_int > low and time_slot_int<high:
                            flag=1
                            break
                    if flag==1:
                        pass
                    else:
                        dispatcher.utter_template("utter_incorrect_time",tracker)
                        slot_values[slot] = None
             
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_finish', tracker)
        return []


class ValidateInputs(Action):
    def name(self):
        return 'validate_inputs'

    def run(self, dispatcher, tracker, domain):
        time =  tracker.get_slot('time') #duckling time entity
        dept = tracker.get_slot('dept')
        date_slot=tracker.get_slot('date_slot')
        doc_slot=tracker.get_slot('doc_slot')
        print(time,dept)
        department = ['cardiology','neurology','pediatrics','family medicine','intensive care',
                        'emergency','psychiatry','opthalmology','ent','gastroenterology','gynaecology',
                        'microbiology','nephrology','oncology','orthopaedics']
        return_slots = []
        
        
        file = pd.read_csv('DocAvail.csv')
        #doc='Oh,fuck'
        if dept == None:
            pass
        elif dept.lower() not in department:
            dispatcher.utter_template('utter_incorrect_dept', tracker)
            return_slots.append(SlotSet("dept", None))

        if time == None:
            pass
        else:

            date = time[0:10]
            time_slot = time[11:19]
            print(date,time_slot)         
            if date_slot != None:
                pass
            else:
                date_time = datetime.datetime.strptime(date,"%Y-%m-%d")
                weekday = datetime.datetime.strftime(date_time,"%A")
                month = datetime.datetime.strftime(date_time,"%B")
                day = datetime.datetime.strftime(date_time,"%d")
                str_dt=weekday+' '+month+' '+day
                return_slots.append(SlotSet("date_slot", str_dt))
                Dept= file[file['Department'].str.lower()==dept].reset_index().drop('index',axis=1)[['Physician name',weekday]]
                flag=0
                for i in range(len(Dept)):
                    avail_time=Dept.ix[i,weekday].split('-')
                    low=int(avail_time[0].split(':')[0])
                    high=int(avail_time[1].split(':')[0])
                    time_slot_int= int(time_slot.split(':')[0])
                    if time_slot_int > low and time_slot_int<high:
                        flag=1
                        break
                if flag==1:
                    doc ='Dr.'+Dept.ix[i,'Physician name']
                else:
                    time_slot= "00:00:00"
                    dispatcher.utter_template('utter_incorrect_time', tracker)
                    return_slots.append(SlotSet("time", None))
                    return_slots.append(SlotSet("date_slot",None))

            
            if time_slot != "00:00:00" and doc_slot== None:
                print(doc,time_slot)

                tym=int(time_slot[0:2])
                dayt=''
                if tym>7 and tym <=11:
                    dayt='morning'
                elif tym>11 and tym <=15:
                    dayt='afternoon'
                elif tym>15 and tym <=19:
                    dayt='evening'
                else:
                    dayt ='night'
                str_tim = dayt+ ' at '+str(tym%12)+' o clock'
                return_slots.append(SlotSet("time_slot", str_tim))
                return_slots.append(SlotSet("doc_slot",doc))
            else: 
                pass
        print(return_slots)
            #return_slots.append(SlotSet("time", None))

        return return_slots





class ActionGoodBye(Action):
    def name(self):
        return 'action_bye'
  
    def run(self, dispatcher, tracker, domain):
        #dispatcher.utter_template("utter_bye",tracker)
        return[AllSlotsReset()]
            
class ActionRestarted(Action):  
    def name(self):         
        return 'action_restarted'   
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()]
        
class ActionSlotReset(Action):  
    def name(self):         
        return 'action_slot_reset'  
    def run(self, dispatcher, tracker, domain):         
        return [SlotSet('dept',None),SlotSet('time',None)]