
class APIClient:
    def __init__(self, api_key):
        self.__api_key = api_key  # Приватный атрибут для хранения ключа API

    def connect(self):
        self.__authenticate()
        print("Соединение установлено")

    def __authenticate(self):
        # Приватный метод для выполнения аутентификации
        print(f"Аутентификация с API ключом: {self.__api_key}")
