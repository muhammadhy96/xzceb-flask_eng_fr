"""this module use Watson translator to translate English text to french and vice versa"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-01-14',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """function to translate english text to french"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation.get('translations')[0].get('translation')
    return french_text

def french_to_english(french_text):
    """function to translate french text to english"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation.get('translations')[0].get('translation')
    return english_text
