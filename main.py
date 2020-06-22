import json

mocked_response = json.dumps({
    "platform_name": "AwesomeMarketplace",
    "body_text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
})

configuration_template = {
    "platform_name":"",
    "site_title": "",
    "body_text": "",
    "footer": {
        "footer_header": "",
        "footer_body": "",
    },
}
