import pprint

list_1 = ['rider', 'electric_scooter', 'electric_scooter_person', 'person', 'none_person_bicycle', 'none_person_electric_scooter', 'unknown_person_electric_scooter', 'unknown_person_tricycle', 'bicycle', 'bicycle_person', 'unknown_person_bicycle', 'none_person_auto_tricycle', 'auto_tricycle', 'none_person_motorbike', 'motorbike', 'none_person_tricycle', 'tricycle', 'tricycle_person', 'unknown_person_auto_tricycle', 'auto_tricycle_person', 'motorbike_person', 'unknown_person_motorbike']
list_2 = ['fixed_stall', 'sunshade']
list_3 = ['other_sign', 'billboard', 'traffic_sign']
list_4 = ['drying_object', 'sunshade', 'fixed_stall']
list_5 = ['garbage_bag', 'person', 'bottle', 'carton', 'construction_waste', 'cigarette_case', 'toilet_paper']
list_6 = ['person', 'carton', 'garbage_bag', 'construction_waste', 'bottle', 'toilet_paper', 'cigarette_case']
list_7 = ['garbage_bag', 'carton', 'bottle', 'toilet_paper', 'cigarette_case', 'person', 'construction_waste']
list_8 = []

class_names = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + list_8

NewList = list(set(class_names))
pprint.pp(NewList)
