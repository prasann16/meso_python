import boto3
client = boto3.client(service_name='comprehendmedical', region_name='us-east-2')
def get_summary(text):
    result = client.detect_entities(Text= text)
    entities = result['Entities']
    result_dict={}
    result_dict['medications']=get_medications(entities)
    result_dict['tests']=get_tests(entities)
    result_dict['things_to_remember']=get_things_to_remember(entities)
    return result_dict
def get_medications(entities):
    medication_dict = {}
    for entity in entities:
        if(entity['Category']=='MEDICATION'):
            medication_dict[entity['Text']] = {}
            try:
                for at in entity['Attributes']:
                    medication_dict[entity['Text']][at['Type']] = at['Text']
            except:
                pass
    return medication_dict

def get_tests(entities):
    tests_dict = {}
    for entity in entities:
        if(entity['Category']=='TEST_TREATMENT_PROCEDURE'):
            if(entity['Type']=='TEST_NAME'):
                tests_dict[entity['Text']]={} 
            try:
                for at in entity['Attributes']:
                    tests_dict[entity['Text']][at['Type']] = at['Text']
            except:
                pass
    return tests_dict

def get_things_to_remember(entities):
    remember_dict={}
    for entity in entities:
        if(entity['Category']=='TEST_TREATMENT_PROCEDURE'):
            if(entity['Type']=='TREATMENT_NAME'):
                remember_dict[entity['Text']]={}
            try:
                for at in entity['Attributes']:
                    remember_dict[entity['Text']][at['Type']] = at['Text']
            except:
                pass

    return remember_dict