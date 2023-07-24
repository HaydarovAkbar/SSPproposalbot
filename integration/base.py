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
    def business_sector_list(lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/BusinessSectorSelectList?__lang={lang_id[lang]}', verify=False)
        return responce.json()

    @staticmethod
    def proposal_subject_list(lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/ProposalSubjectSelectList?__lang={lang_id[lang]}', verify=False)
        return responce.json()

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
        }
        if not data.get('companyName', False):
            data.pop('companyName')
        if not data.get('companyInn', False):
            data.pop('companyInn')
        if not data.get('businessSectorId', False):
            data.pop('businessSectorId')
        response = requests.post(url, json=data, verify=False)
        return response.status_code


if __name__ == '__main__':
    print(IntegrationSSP.proposal_subject_list())
