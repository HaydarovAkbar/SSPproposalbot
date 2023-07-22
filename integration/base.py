import requests
from decouple import config

BASE_URL = config('BASE_URL')
lang_id = {
    'uz_latn': 3,
    'uz_cyrl': 2,
    'ru': 1,
    'en': 4,
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
        responce = requests.get(f'{BASE_URL}/Manual/ApplicantTypeSelectList?languageId={lang_id[lang]}')
        return responce.json()

    @staticmethod
    def business_sector_list(lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/BusinessSectorSelectList?languageId={lang_id[lang]}')
        return responce.json()

    @staticmethod
    def proposal_subject_list(lang='uz_latn'):
        responce = requests.get(f'{BASE_URL}/Manual/ProposalSubjectSelectList?languageId={lang_id[lang]}')
        return responce.json()

    @staticmethod
    def create_proposal(data):
        url = f'{BASE_URL}/Proposal/Create'
        data = {
            "proposalTypeId": data.get('application_type', None),
            "businessSectorId": data.get('business_sector', None),
            "externalSourceTypeId": 3,
            "nameLatin": data.get('fullname', None),
            "phoneNumber": data.get('phone', None),
            "proposalSubjectId": data.get('business_type', None),
            "companyName": data.get('company_name', None),
            "companyInn": data.get('company_inn', None),
        }
        response = requests.post(url, json=data)
        return response.status_code


if __name__ == '__main__':
    IntegrationSSP.proposal_subject_list()
