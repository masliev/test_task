import requests
from functools import lru_cache

URL = "https://api.typeform.com/forms/j9oU327F/responses"
TOKEN = "5smhCM5PaTWX1aEnKkyBxKMjZa23tpAaLdGjshmxPXAt"
QUESTIONS_MAP = {
    "lUSCoWCfRBjz": "platform_name",
    "xzEOKIHDo4SA": "body_text",
}
QUESTIONNAIRE_ID = 1

class APIService:
    def __init__(self, url, token, questions_map, questionnaire_id):
        self.url = url
        self.token = token
        self.questions_map = questions_map
        self.questionnaire_id = questionnaire_id

    @lru_cache(maxsize=128, typed=False)
    def _api_get_results(self, url, token):
        headers = {'authorization': 'Bearer {}'.format(token)}
        response = requests.get(url, headers=headers)
        return response.json()
    
    def prepared_results(self):
        q_id = self.questionnaire_id
        answers = self._api_get_results(self.url, self.token)\
                                        ['items'][q_id]['answers']
        key_value_arguments = {}
        for answer in answers:
            answer_id = answer['field']['id']
            alias_name = self.questions_map[answer_id]
            key_value_arguments.update({alias_name: answer['text']})
        return key_value_arguments


def apiservice_factory(url, token, questions_map, questionnaire_id):
    return APIService(url, token, questions_map, questionnaire_id)

api_service = apiservice_factory(URL, TOKEN, QUESTIONS_MAP, QUESTIONNAIRE_ID)
