import json


class ConfigService:

    def __init__(self, questionnaire_data, config_template):
        self.input_data = self._parsed_api_response(questionnaire_data)
        self.config_template = config_template

    def _parsed_api_response(self, questionnaire_data):
        return json.loads(questionnaire_data)

    def create_config(self):
        pass

    def update_config(self):
        pass

