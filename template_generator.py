
template_required_fields = ('platform_name', 'body_text')

def template_generator(*args, **kwargs):
    for i in template_required_fields:
        if kwargs[i]:
            pass
        else:
            raise Exception('Required fields are empty, required fields is {}'.format(template_required_fields))
    configuration_template = {
        "platform_name":"{}".format(kwargs[platform_name]),
        "site_title": "{}".format(kwargs[platform_name]),
        "body_text": "{}".format(kwargs[body_text]),
        "footer": {
            "footer_header": "Copyright by {}".format(kwargs[platform_name]),
        },
    }
    return configuration_template
