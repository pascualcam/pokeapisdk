import os
import json
from urllib.parse import urlencode
import requests

def create_params(**kwargs):
    url = kwargs
    params = kwargs.get('params')
    if params:
        query_string = urlencode(eval(params))
    return f'{url}?{query_string}'


class PathBuilder:
    '''
    PathBuilder is a class that builds a path for the API request.
    '''
    def __init__(self, base_url, domain, version):
        self.base_url = base_url
        self.domain = domain
        self.version = version

    def build(self):
        paths = {
            "domains": {
                "pokemon": {
                    "generations": {
                        "generation": {
                            "id": None
                        }
                    }
                }
            }
        }
        domain_info = paths['domains'][self.domain]
        sections = [domain_info['path']]
        if self.profile_id:
            sections.append(self.profile_id)
        if domain_info["name"]:
            sections.append(domain_info["name"])
            if self.domain_id:
                sections.append(self.domain_id)
                if domain_info["actions"]:
                    sections.append(domain_info["actions"][self.domain_action])
        path = f'/{"/".join(sections)}'
        url = f'{self.base_url}/{path}'
        
        # params and filtering
        params = {}
        operators = ["e", "lt", "lte", "gt", "gte"]
        for param in self.params.keys():
            if param in operators:
                params['pokemon.id'] = f'{param}={self.params[param]}'
            else:
                params[param] = self.params[param]
        if params:
            url = create_params(url, params)
        
        return [path, url]


class APIRequester:
    '''
    APIRequester is a class that makes requests to the API.
    '''
    def __init__(self, **kwargs):
        self.method = kwargs.get('method')
        self.url = kwargs.get('url')
        self.headers = kwargs.get('headers')
        self.data = kwargs.get('data')
    
    def get(self):
        response = requests.get(self.url, headers=self.headers)
        return response


class Client(object):
    '''
    Client is a class that is used to interact with the PokeAPI.
    '''
    def __init__(self, version=None, env=None, environ=None):
        environ = environ or os.environ
        self.pokeapi_version = version or environ.get('POKEAPI_VERSION', 'v1')
        self.env = env or environ.get('ENV', 'dev')
        
        self.base_url = environ.get("POKEAPI_BASE_URL")
        self._pokemon = None
        
    def requests(self, method, base_url, domain, version, profile_id=None, domain_id=None, domain_action=None, params=None, data=None, headers=None, auth=None):
        headers = headers or {}
        params = params or {}
        method = method.upper()
        
        path, url = PathBuilder(base_url, domain, version).build()
        api = APIRequester(url=url)
        response = api.get()
        
        print(
            f'Response:\nStatus:\n{response.status_code}\nJSON:\n{response.json()}'
        )
        
    @property
    def pokemon(self):
        '''
        Access the sdk pokemon API
        '''
        if self._pokemon is None:
            from sdk.models.pokemon import Pokemon
            self._pokemon = Pokemon(self, self.base_url, 'pokemon', self.pokeapi_version)
        return self._pokemon
