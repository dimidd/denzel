from enum import Enum

SERVICES = ['api', 'denzel', 'monitor', 'redis']

DENZEL_IMAGE_NAME = 'denzel'
DENZEL_IMAGE_TAG = '1.0.0'

DENZEL_IMAGE_SERVICES = ['api', 'denzel', 'monitor']

REDIS_IMAGE_TAG = '4'

WORKER_LOG_PATH = 'logs/worker.log'

PIP_REQUIREMENTS_FILE = 'requirements.txt'

# PORTS
API_PORT = 8000
MONITOR_PORT = 5555


class Status(Enum):
    UP = 'UP'
    PIP = 'PIP INSTALLING...'
    BUILDING = 'building'
    NA = 'UNAVAILABLE'
    ERROR = 'ERROR'
    LOADING = 'LOADING...'
    DOWN = 'DOWN'

# Colors
class Colors(Enum):
    SUCCESS = 'green'
    FAILURE = 'red'
    DESCRIPTOR = 'blue'
    NEUTRAL = 'yellow'
