import os

import celery
import requests
from app.logic.pipeline import process, load_model, predict

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

app = celery.Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)


class Model(celery.Task):

    def __init__(self):
        self._model = load_model()

    @property
    def model(self):
        return self._model


@app.task(base=Model)
def invoke_predict(json_data):
    # Preprocess data
    data = process(invoke_predict.model, json_data)

    # Preform predictions
    result = predict(invoke_predict.model, data)

    # Send prediction to callback_uri
    requests.post(url=json_data['callback_uri'],
                  json=result)

    return result


Model = app.register_task(Model())
