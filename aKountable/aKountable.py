import os
import requests
import hashlib
import ast
import keras.backend as K
from keras.models import Sequential, Model
HASHAPI_URL = 'https://hashapi.tierion.com/v1'
DATAAPI_URL = 'https://api.tierion.com/v1'

class aKountable(object):
    def __init__(self, model, username=None, password=None, api_key=None):
        assert isinstance(model, Sequential) or isinstance(model, Model), '`model` needs to be a valid Keras model'
        self.model = model
        self.is_stamped = False
        self.receipt_id = None
        self.blockchain_receipt = None
        self.is_valid = None
        if username is None:
            username = os.environ['TIERION_USERNAME']
        if password is None:
            password = os.environ['TIERION_PASSWORD']
        if api_key is None:
            api_key = os.environ['TIERION_API_KEY']
        self.headers = {
            'username': username,
            'password': password,
        }
        self.data_credentials = {
            'X-Username': username,
            'X-Api-Key': api_key
        }
        self._refresh_auth()

    def _refresh_auth(self):
        req = requests.post(HASHAPI_URL + '/auth/token', json=self.headers)
        print req.json()
        token = req.json()['access_token']
        self.auth = {'Authorization': 'Bearer ' + token}

    def _get_model_hash(self):
        model_hash = hashlib.sha256()
        model_hash.update(self.model.to_json())
        for W in self.model.trainable_weights:
            w = K.get_value(W)
            model_hash.update(w)
        return model_hash

    def stamp(self):
        assert not self.is_stamped, 'You model has been previously stamped. Create a new aKountable object with your model.'
        model_hash = self._get_model_hash().hexdigest()
        print("Model hash: " + model_hash)
        req = requests.post(HASHAPI_URL + '/hashitems', json={'hash': model_hash}, headers=self.auth)
        print(req.json())
        self.receipt_id = req.json()['receiptId']
        self.timestamp = req.json()['timestamp']
        self.is_stamped = True

    def receipt(self):
        assert self.receipt_id is not None, 'You should `stamp` your model before requesting a receipt.'
        req = requests.get(HASHAPI_URL + '/receipts/'+self.receipt_id, headers=self.auth)
        print(req.json())
        try:
            self.blockchain_receipt = {u"blockchain_receipt": req.json()['receipt']}
        except:
            print("Couldn not retreive receipt. See message above.")


    def validate(self):
        assert self.blockchain_receipt is not None, 'You should `stamp` your model and get a `receipt` before trying to validate it.'
        req = requests.post(DATAAPI_URL + '/validatereceipt', json=self.blockchain_receipt, headers=self.data_credentials)
        model_hash = self._get_model_hash().hexdigest()
        blockchain_receipt = ast.literal_eval(self.blockchain_receipt['blockchain_receipt'])
        is_same_model = model_hash == blockchain_receipt['targetHash']
        if is_same_model:
            if req.json() == {u'success': u'Receipt is valid.'}:
                self.is_valid = True
            else:
                print('We could not verify this model: ', req.json())
        else:
            self.is_valid = False
            print('Your model has changed since it was stamped.')
        return self.is_valid
