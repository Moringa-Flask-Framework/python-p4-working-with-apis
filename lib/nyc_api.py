
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://data.cityofchicago.org/resource/f7f2-ggz5.json"

    response = requests.get(URL)
    return response.content
  
  def program_cities(self):
    programs_list= []
    programs= json.loads(self.get_programs())
    for program in programs:
      programs_list.append(program['city'])
    return programs_list


# programs = GetPrograms().get_programs()
# print(programs)
programs= GetPrograms()
cities= programs.program_cities()

for city in set(cities):
  print(city)
