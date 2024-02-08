import requests


class RandomPassGenerator():

    def __init__(self, lenght: int, numbers: bool, special: bool, uppercase: bool, lowercase: bool):
        self.__lenght = lenght
        self.__numbers = numbers
        self.__special = special
        self.__uppercase = uppercase
        self.__lowercase = lowercase
        self.__base_url = 'https://api.genratr.com'
        self.__query_params_list = {'&numbers': self.__numbers, '&special': self.__special, '&uppercase': self.__uppercase, '&lowercase': self.__lowercase}

    def __make_url(self):
        params = ''
        for key, value in self.__query_params_list.items():
            if value:
                params += f'{key}'

        full_url = f'{self.__base_url}/?length={self.__length}' + params
        return full_url
    
    def gen_pass(self):
        res = requests.get(self.__make_url())
        if res.status_code == requests.codes.ok:
            return eval(res.text)
        else:
            raise Exception('Not possible to gen pass right now')
        