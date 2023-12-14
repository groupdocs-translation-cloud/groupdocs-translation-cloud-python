import time

import groupdocs_translation_cloud

api = groupdocs_translation_cloud.api.TranslationApi()
api.api_client.configuration.client_id = "translate.cloud"
api.api_client.configuration.client_secret = "5d0da472782620373473703904631795"

text_request = groupdocs_translation_cloud.TextRequest(source_language="en"
                                                       , target_languages=["es", "fr", "ru"]
                                                       , texts=["Hello World!", "This is a test text"]
                                                       , origin="your_application_name"
                                                       , contains_markdown=False)
response = api.text_post(text_request)
if response.status == 202:
    while True:
        status_response = api.text_request_id_get(response.id)
        if status_response.status == 200:
            for lang in status_response.translations:
                print(lang.key)
            break
        time.sleep(2)
