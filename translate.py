import six
from google.cloud import translate_v2 as translate


def translate_to(text, target):
    """
    Function takes text and target. Return translated text in target language.
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    return translate_client.translate(text, target_language=target)["translatedText"]
