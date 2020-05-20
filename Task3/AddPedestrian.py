import json
import sys


def get_dynamicElements_from_scenario(file_name): # returns dynamicElements array
  with open(file_name) as json_file:
    data = json.load(json_file)
    dynamic = data["scenario"]["topography"]["dynamicElements"] #probably empty array at first
  return dynamic, data

def read_new_pedestrian_info():
  with open("add_pedestrian.json") as pedestrian_infos:
    pedestrian_data_arr = json.load(pedestrian_infos) # reading the file to get pedestrian attributes to add the scenario
  return pedestrian_data_arr

def read_template(template_name): 
  with open(template_name) as template:
    temp = json.load(template) # reading the file to get attributes to add the scenario
  return temp[0]

def create_dynamicElements_field(pedestrian_data_arr, dynamicElements):
  pedestrian_temp = read_template("template.json") #json.dumps(dynamic_element) # read the template
  dynamic_new = []
  dynamic = dynamicElements

  for pedestrian in pedestrian_data_arr: # for each pedestrian object read from the file
    pedestrian_template = pedestrian_temp.copy()
    for key in pedestrian.keys(): # creating the dynamicElements for each pedestrian
      pedestrian_template[key] = pedestrian[key]  # change values of pedestrian_template
  
    dynamic_new.append(pedestrian_template) 

  if len(sys.argv) > 2 and sys.argv[2] == "1": # If we give 1 as argument, it means we will apend to existing pedestrians, not override
    for each in dynamic_new:
      dynamic.append(each)
    return dynamic
  elif len(sys.argv) == 2 or sys.argv[2] == "0": # If we want to override the existing dynamicElements with the infos in the add_pedestrian
    return dynamic_new




def main():
  file_name = sys.argv[1] # taking scenario name as system argument, like rimea_6.scenario
  dynamicElements, data = get_dynamicElements_from_scenario(file_name)
  pedestrian_data_arr = read_new_pedestrian_info()
  new_dynamicElements = create_dynamicElements_field(pedestrian_data_arr,dynamicElements)
  data["scenario"]["topography"]["dynamicElements"] = new_dynamicElements
  new_file_name = file_name.split(".")[0] +"_new"
  data["name"] = new_file_name

  with open(new_file_name + ".scenario", 'w') as f:
    json.dump(data, f)


# "python AddPedestrian.py" or "python AddPedestrian.py 0" for overriding
# "python AddPedestrian.py 1" for appending

if __name__ == '__main__':
  main()





















