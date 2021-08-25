import os

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'
}

MYSQL_USER = os.getenv('MYSQL_USER', '')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
SQLALCHEMY_DATABASE_URI = \
    'mysql://{u}:{p}@mysql:3306/superset?charset=utf8mb4'.format(u=MYSQL_USER, p=MYSQL_PASSWORD)
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.getenv('SECRET_KEY', '')
