import requests
from decouple import config

BASE_URL = config('BASE_URL')
lang_id = {
    'uz_latn': 'uz-latn',
    'uz_cyrl': 'uz-cyrl',
    'ru': 'ru',
    'en': 1,
}

class IntegrationSSP:
    @staticmethod
    def get_token():
        url = 'https://ssp.uz/api/v1/auth/login'
        data = {
            "username": "admin",
            "password": "admin"
        }
        response = requests.post(url, json=data)
        return response.json()['token']

    @staticmethod
    def get_all_application_type(lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/ApplicantTypeSelectList?__lang={lang_id[lang]}', verify=False)
        return responce.json()

    @staticmethod
    def get_application_type(id, lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/ApplicantTypeSelectList?__lang={lang_id[lang]}', verify=False)
        for i in responce.json():
            if i['value'] == int(id):
                return i['text']

    @staticmethod
    def business_sector_list(lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/BusinessSectorSelectList?__lang={lang_id[lang]}', verify=False)
        return responce.json()

    @staticmethod
    def get_business_sector(id, lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/BusinessSectorSelectList?__lang={lang_id[lang]}', verify=False)
        for i in responce.json():
            if i['value'] == int(id):
                return i['text']

    @staticmethod
    def proposal_subject_list(lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/ProposalSubjectSelectList?__lang={lang_id[lang]}', verify=False)
        return responce.json()

    @staticmethod
    def get_proposal_subject(id, lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/ProposalSubjectSelectList?__lang={lang_id[lang]}', verify=False)
        for i in responce.json():
            if i['value'] == int(id):
                return i['text']

    @staticmethod
    def get_contractor_from_soliq(inn):
        url = f'{BASE_URL}/Proposal/GetContractorFromSoliq?inn={inn}'
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.json(), response.status_code
        return response.json(), response.status_code

    @staticmethod
    def get_company_type_list(lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/CompanyTypeSelectList?__lang={lang_id[lang]}', verify=False)
        return responce.json()

    @staticmethod
    def get_company_type(id, lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/CompanyTypeSelectList?__lang={lang_id[lang]}', verify=False)
        for i in responce.json():
            if i['value'] == int(id):
                return i['text']

    @staticmethod
    def create_proposal(data):
        url = f'{BASE_URL}/Proposal/Create'
        data = {
            "proposalTypeId": data.get('application_type', None),
            "businessSectorId": data.get('business_center', None),
            "externalSourceTypeId": 3,
            "nameLatin": data.get('fullname', None),
            "phoneNumber": data.get('phone', None),
            "proposalSubjectId": data.get('business_type', None),
            "companyName": data.get('company_name', False),
            "companyInn": data.get('company_inn', False),
            "appealText": data.get('appeal', False),
            "proposalText": data.get('offer', False),
            "companyTypeId": data.get('company_type', False),
        }
        if not data.get('companyName', False):
            data.pop('companyName')
        if not data.get('companyInn', False):
            data.pop('companyInn')
        if not data.get('businessSectorId', False):
            data.pop('businessSectorId')
        print(data)
        response = requests.post(url, json=data, verify=False)
        print(response.json())
        return response.status_code


if __name__ == '__main__':
    print(IntegrationSSP.get_company_type_list())
