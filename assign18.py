"""18. Find a package in the Python standard library for dealing with JSON.
Import the library module and inspect the attributes of the module.
Use the help function to learn more about how to use the module.
Serialize a dictionary mapping 'name' to your name and 'age' to your
age, to a JSON string. Deserialize the JSON back into Python."""


#python standard library for json is json
#importing json library
import json

print(dir(json))

# ['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__',
#  '__author__', '__builtins__', '__cached__', '__doc__', '__file__',
#  '__loader__', '__name__', '__package__', '__path__', '__spec__',
#  '__version__', '_default_decoder', '_default_encoder', 'codecs',
#  'decoder', 'detect_encoding', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']

# help(json)

people = {
    "first_name": "yuvi",
    "age": 26
}
json_data = json.dumps(people, indent=2)
print(json_data)
print(json.loads(json_data))































#
#
# import json
# #help(json)
#
# # Serializing
# info = {
#   "name": "Salina",
#   "age": 22
# }
# with open("info.json", "w") as write_file:
#     json.dump(info, write_file)
#
# # Deserializing
# with open("info.json", "r") as read_file:
#     result = json.load(read_file)
#
