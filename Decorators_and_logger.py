import logging
import time
import hashlib
import json


def dec_log(func):

    def wrapper(path):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        start = time.ctime(time.time())
        result = func(path)
        file_handler = logging.FileHandler('logger.log')
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        logger.info(f'Название функции: {func}\nДата и время вызова функции: {start}\nАргумент: {path}\n'
                    f'Возвращаемое значение {result}')

        return result

    return wrapper


@dec_log
def data_hashing(path):
    with open(path, encoding='utf-8') as f:
        file_json = json.load(f)
        for dictionary in file_json:
            countries = dictionary['name']['common']
            hash_object = hashlib.md5(str.encode(countries))
            yield hash_object.hexdigest()


for hashed_data in data_hashing('countries.json'):
    print(hashed_data)
