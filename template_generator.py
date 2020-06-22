template_required_fields = ('platform_name', 'body_text')


def template_generator(*args, **kwargs):
    for i in template_required_fields:
        try: 
            kwargs[i]
        except KeyError:
            raise Exception('Required fields are empty, required fields are {}'\
                            .format(template_required_fields))
    configuration_template = {
        "platform_name":"{}".format(kwargs['platform_name']),
        "site_title": "{}".format(kwargs['platform_name']),
        "body_text": "{}".format(kwargs['body_text']),
        "footer": {
            "footer_header": "Copyright by {}".format(kwargs['platform_name']),
        },
    }

    new_fields = list(set(kwargs).difference(set(template_required_fields)))
    if len(new_fields) > 0:
        for field in new_fields:
            configuration_template.update({field: kwargs[field]})
    return configuration_template
