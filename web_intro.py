import requests

# r = requests.get('https://api.github.com/repos/dward2/BME547/branches') #It
# # goes to https://github.com/dward2/BME547
#
# print(r)
# print(type(r))
# print(r.text)
# if r.status.code == 200:
#     answer = r.json()
#     print(type(answer))
#     for branch in answer:
#         print(branch['name'])
# else:
#     print('Bad request: {}'.format(r.text))


# Professor has a server that can read out the information you send (part of
# the in-class exercise)
# output_info = {'name': 'Junqi Lu',
#                'net_id': 'jl922',
#                'e-mail': 'junqi.lu@duke.edu'}
#
# r = requests.post('http://vcm-21170.vm.duke.edu:5000/student',
#                   json=output_info)
#
# print(r)
# print(r.text)
#
# r = requests.get('http://vcm-21170.vm.duke.edu:5000/list')
# print(r.text)


# In-class exercise with a classmate
message = {'user': 'jl922', 'message': 'Hello world'}
r = requests.post('http://vcm-21170.vm.duke.edu:5001/add_message',
                  json=message)

get = requests.get('http://vcm-21170.vm.duke.edu:5001/get_messages/Ziwei_He')
print(get.text)
