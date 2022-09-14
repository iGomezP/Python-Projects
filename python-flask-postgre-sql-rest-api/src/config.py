# Permite trabajar con variables de entorno
from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')


# Otra clase que hereda de config e indica el debug para que el haber cambios de reinicie solo
class DevelopmentConfig(Config):
    DEBUG = True


# diccionario
config = {
    'development': DevelopmentConfig
}
