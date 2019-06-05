
## Generated Story -2827604014098265773
* greet
    - utter_greet
* schedule_appointment{"time": "2018-11-05T17:00:00.000-08:00", "dept": "neurology"}
    - slot{"dept": "neurology"}
    - slot{"time": "2018-11-05T17:00:00.000-08:00"}
    - validate_inputs
    - slot{"date_slot": "Monday November 05"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Karissa Gable"}
    - appointment_form
    - form{"name": "appointment_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}


## Generated Story -2827604014098265773
* greet
    - utter_greet
* schedule_appointment{"time": "2018-11-05T17:00:00.000-08:00", "dept": "opthalmology"}
    - slot{"dept": "opthalomology"}
    - slot{"time": "2018-11-05T17:00:00.000-08:00"}
    - validate_inputs
    - slot{"date_slot": "Monday November 05"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Arun Ayyar"}
    - appointment_form
    - form{"name": "appointment_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

## Generated Story -2827604014098265773
* greet
    - utter_greet
* schedule_appointment{"time": "2018-11-05T17:00:00.000-08:00", "dept": "pediatrics"}
    - slot{"dept": "pediatrics"}
    - slot{"time": "2018-11-05T17:00:00.000-08:00"}
    - validate_inputs
    - slot{"date_slot": "Monday November 05"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Jeffrey Baker"}
    - appointment_form
    - form{"name": "appointment_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

## Generated Story 2478315885794407558
* greet
    - utter_greet
* schedule_appointment{"dept": "neurology", "time": "2018-11-05T20:00:00.000-08:00"}
    - slot{"dept": "neurology"}
    - slot{"time": "2018-11-05T20:00:00.000-08:00"}
    - validate_inputs
    - slot{"date_slot": "Monday November 05"}
    - slot{"time": null}
    - slot{"date_slot": null}
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-11-05T19:00:00.000-08:00"}
    - slot{"time": "2018-11-05T19:00:00.000-08:00"}
    - form: appointment_form
    - slot{"time": null}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-11-05T17:00:00.000-08:00"}
    - slot{"time": "2018-11-05T17:00:00.000-08:00"}
    - form: appointment_form
    - slot{"time": "2018-11-05T17:00:00.000-08:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Monday November 05"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Karissa Gable"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

## Generated Story 2478315885794407558
* greet
    - utter_greet
* schedule_appointment{"dept": "opthalmology", "time": "2018-11-05T20:00:00.000-08:00"}
    - slot{"dept": "opthalomology"}
    - slot{"time": "2018-11-05T20:00:00.000-08:00"}
    - validate_inputs
    - slot{"date_slot": "Monday November 05"}
    - slot{"time": null}
    - slot{"date_slot": null}
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-11-05T19:00:00.000-08:00"}
    - slot{"time": "2018-11-05T19:00:00.000-08:00"}
    - form: appointment_form
    - slot{"time": null}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-11-05T17:00:00.000-08:00"}
    - slot{"time": "2018-11-05T17:00:00.000-08:00"}
    - form: appointment_form
    - slot{"time": "2018-11-05T17:00:00.000-08:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Monday November 05"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Arun Ayyar"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}


## Generated Story 401659288267778721
* greet
    - utter_greet
* schedule_appointment
    - validate_inputs
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "opthalmology"}
    - slot{"dept": "opthalmology"}
    - form: appointment_form
    - slot{"dept": "opthalmology"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-11-06T10:00:00.000-08:00"}
    - slot{"time": "2018-11-06T10:00:00.000-08:00"}
    - form: appointment_form
    - slot{"time": "2018-11-06T10:00:00.000-08:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Tuesday November 06"}
    - slot{"time_slot": "morning at 10 o clock"}
    - slot{"doc_slot": "Dr.Shravan Mohan"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

## Generated Story 401659288267778721
* schedule_appointment
    - validate_inputs
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "opthalmology"}
    - slot{"dept": "opthalmology"}
    - form: appointment_form
    - slot{"dept": "opthalmology"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-11-06T10:00:00.000-08:00"}
    - slot{"time": "2018-11-06T10:00:00.000-08:00"}
    - form: appointment_form
    - slot{"time": "2018-11-06T10:00:00.000-08:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Tuesday November 06"}
    - slot{"time_slot": "morning at 10 o clock"}
    - slot{"doc_slot": "Dr.Shravan Mohan"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

## Generated Story 6662386764541498929
* greet
    - utter_greet
* schedule_appointment
    - validate_inputs
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "cardiology"}
    - slot{"dept": "cardiology"}
    - form: appointment_form
    - slot{"dept": "cardiology"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-10-31T14:00:00.000-07:00"}
    - slot{"time": "2018-10-31T14:00:00.000-07:00"}
    - form: appointment_form
    - slot{"time": "2018-10-31T14:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Wednesday October 31"}
    - slot{"time_slot": "afternoon at 2 o clock"}
    - slot{"doc_slot": "Dr.Melissa Daubert"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}


## Generated Story 6662386764541498929
* schedule_appointment
    - validate_inputs
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "cardiology"}
    - slot{"dept": "cardiology"}
    - form: appointment_form
    - slot{"dept": "cardiology"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-10-31T14:00:00.000-07:00"}
    - slot{"time": "2018-10-31T14:00:00.000-07:00"}
    - form: appointment_form
    - slot{"time": "2018-10-31T14:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Wednesday October 31"}
    - slot{"time_slot": "afternoon at 2 o clock"}
    - slot{"doc_slot": "Dr.Melissa Daubert"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

## Generated Story 6662386764541498929
* greet
    - utter_greet
* schedule_appointment
    - validate_inputs
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "pediatrics"}
    - slot{"dept": "pediatrics"}
    - form: appointment_form
    - slot{"dept": "pediatrics"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-10-31T14:00:00.000-07:00"}
    - slot{"time": "2018-10-31T14:00:00.000-07:00"}
    - form: appointment_form
    - slot{"time": "2018-10-31T14:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Wednesday October 31"}
    - slot{"time_slot": "afternoon at 2 o clock"}
    - slot{"doc_slot": "Dr.Jeffrey Baker"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

    
## Generated Story 6662386764541498929
* schedule_appointment
    - validate_inputs
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "pediatrics"}
    - slot{"dept": "pediatrics"}
    - form: appointment_form
    - slot{"dept": "pediatrics"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-10-31T14:00:00.000-07:00"}
    - slot{"time": "2018-10-31T14:00:00.000-07:00"}
    - form: appointment_form
    - slot{"time": "2018-10-31T14:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Wednesday October 31"}
    - slot{"time_slot": "afternoon at 2 o clock"}
    - slot{"doc_slot": "Dr.Jeffrey Baker"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}
## Generated Story -9059338358852154849
* schedule_appointment
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "neurology"}
    - slot{"dept": "neurology"}
    - form: appointment_form
    - slot{"dept": "neurology"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-10-31T17:00:00.000-07:00"}
    - slot{"time": "2018-10-31T17:00:00.000-07:00"}
    - form: appointment_form
    - slot{"time": "2018-10-31T17:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Wednesday October 31"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Karissa Gable"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

    
## Generated Story -9059338358852154849
* schedule_appointment
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "cardiology"}
    - slot{"dept": "cardiology"}
    - form: appointment_form
    - slot{"dept": "cardiology"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-10-31T17:00:00.000-07:00"}
    - slot{"time": "2018-10-31T17:00:00.000-07:00"}
    - form: appointment_form
    - slot{"time": "2018-10-31T17:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Wednesday October 31"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Melissa Daubert"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

## Generated Story -9059338358852154849
* schedule_appointment
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "pediatrics"}
    - slot{"dept": "pediatrics"}
    - form: appointment_form
    - slot{"dept": "pediatrics"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-10-31T17:00:00.000-07:00"}
    - slot{"time": "2018-10-31T17:00:00.000-07:00"}
    - form: appointment_form
    - slot{"time": "2018-10-31T17:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Wednesday October 31"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Aimee Chung"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

## Generated Story 1817009052378471652
* schedule_appointment
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "neurology"}
    - slot{"dept": "neurology"}
    - form: appointment_form
    - slot{"dept": "neurology"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-11-01T17:00:00.000-07:00"}
    - slot{"time": "2018-11-01T17:00:00.000-07:00"}
    - form: appointment_form
    - slot{"time": "2018-11-01T17:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Thursday November 01"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Karissa Gable"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

## Generated Story 4108030719924692656
* schedule_appointment
    - appointment_form
    - form{"name": "appointment_form"}
    - slot{"requested_slot": "dept"}
* form: schedule_appointment{"dept": "cardiology"}
    - slot{"dept": "cardiology"}
    - form: appointment_form
    - slot{"dept": "cardiology"}
    - slot{"requested_slot": "time"}
* form: schedule_appointment{"time": "2018-11-01T17:00:00.000-07:00"}
    - slot{"time": "2018-11-01T17:00:00.000-07:00"}
    - form: appointment_form
    - slot{"time": "2018-11-01T17:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - validate_inputs
    - slot{"date_slot": "Thursday November 01"}
    - slot{"time_slot": "evening at 5 o clock"}
    - slot{"doc_slot": "Dr.Melissa Daubert"}
    - utter_schedule_appointment
* affirmative
    - utter_affirmative
* bye
    - utter_bye
    - action_bye
    - reset_slots
    - action_slot_reset
    - slot{"dept": null}
    - slot{"time": null}

