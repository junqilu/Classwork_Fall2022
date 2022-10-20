import requests


def main():
    """
    Get the dict that contains the donor and recipient id and post the match
    result to the server
    """
    r = requests.get('http://vcm-7631.vm.duke.edu:5002/get_patients/jl922')

    if r.status_code == 200:
        returned_dict = r.json()
        # print(returned_dict)

        """
        Obtain the blood_type_dict by person's id
        """
        blood_type_dict = {}
        for person_type, id in returned_dict.items():
            r = requests.get('http://vcm-7631.vm.duke.edu:5002/get_blood_type'
                             '/{}'.format(id))

            if r.status_code == 200:
                blood_type_dict[person_type] = {'id': id, 'blood_type':
                    r.text}

        print(blood_type_dict)

        """
        Judge whether it's a match for blood_type between donor and recipient
        """
        blood_match = ''
        if blood_type_dict['Donor']['blood_type'] == blood_type_dict[
            'Recipient']['blood_type']:
            blood_match = 'Yes'
        else:
            blood_match = 'No'

        """
        Send out a POST request to see whether your judgement on the 
        blood_type match is Correct or Incorrect
        """
        post_dict = {'Name': 'jl922', 'Match': blood_match}
        r = requests.post('http://vcm-7631.vm.duke.edu:5002/match_check',
                          json=post_dict)
        if r.status_code == 200:
            print(r.text)

    return 0


if __name__ == '__main__':
    main()
