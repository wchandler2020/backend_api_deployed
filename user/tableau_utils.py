from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils import querying
from dotenv import load_dotenv
import os
import json

load_dotenv()  # take environment variables from .env.

jorie_server = os.getenv('JORIE_SERVER')
jorie_token_name = os.getenv('JORIE_TOKEN_NAME')
jorie_token_value = os.getenv('JORIE_TOKEN_VALUE')
jorie_site_url = os.getenv('JORIE_SITE_URL')
jorie_site_name = os.getenv('JORIE_SITE_NAME')

jorie_username = os.getenv('JORIE_USERNAME')
jorie_password = os.getenv('JORIE_PASSWORD')

tableau_config = {
    'jorie_tableau_dev': {
        'server': jorie_server,
        'api_version': '3.22',
        'personal_access_token_name': jorie_token_name,
        'personal_access_token_secret': jorie_token_value,
        'site_name': jorie_site_name,
        'site_url': jorie_site_url,
    },
    # 'test_tableau_dev': {
    #     'server': server,
    #     'api_version': '3.22',
    #     'username': username,
    #     'password': password,
    #     'site_name': site_name,
    #     'site_url': site_url,
    # },
}

connection = TableauServerConnection(config_json=tableau_config, env='jorie_tableau_dev')
connection.sign_in()

def fetch_data(data_id):
    orth_one_view_id = str(data_id)
    visual_orho_one_data = querying.get_view_data_dataframe(connection, view_id=orth_one_view_id)
    data = visual_orho_one_data.to_json()
    return  data