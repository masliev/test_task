from api_service import api_service
from template_generator import template_generator 

class ConfigService:

    def __init__(self, api_service, template_generator):
        api_service = api_service
        self.answers = self._get_answers()
        self.template_generator = template_generator

    def _get_answers(self):
        return api_service.prepared_results()

    def create_config(self):
        return self.template_generator(**self.answers)

    def update_config(self):
        pass


def config_service_factory(api_service, template_generator):
    return ConfigService(api_service, template_generator)

service = config_service_factory(api_service, template_generator)
