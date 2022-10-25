import requests

# r = requests.get('http://127.0.0.1:5000/info')
# print(r.status_code)
# print(r.text)

# out_data = {'name': 'Junqi Lu', 'hdl_value': 10}
# r = requests.post('http://127.0.0.1:5000/hdl_check', json=out_data)
# print(r.status_code)
# print(r.text)


# out_data = {'a': 50, 'b': 11}
# r = requests.post('http://127.0.0.1:5000/add_numbers', json=out_data)
# print(r.status_code)
# print(r.text)  # r.text is a text str
# answer = r.json()  # Now whatever in r has been decoded, in this case, into a
# # real int
# print(type(answer))


r = requests.get('http://127.0.0.1:5000/add/2/3')
print(r.status_code)
print(r.json())
