def test_add_test_to_patient():
    from db_server import init_server, add_patient, add_test_to_patient
    # Set-up my database for test

    patient_id = 123
    patient_name = 'David'
    added_patient = add_patient(patient_name, patient_id, "A+")

    test_name = 'XXX'
    test_result = 200
    out_data = {'id': patient_id,
                'test_name': test_name,
                'test_result': test_result}
    answer = add_test_to_patient(out_data)
    patient_from_db = Patient.objects.raw({'_id': patient_id}).first()

    # clean up database
    added_patient.delete()

    # asserts
    assert patient_from_db.test_name[-1] == test_name
    assert patient_from_db.test_result[-1] == test_result
