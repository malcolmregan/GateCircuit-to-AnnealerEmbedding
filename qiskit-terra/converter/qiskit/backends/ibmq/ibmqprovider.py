


import warnings
from collections import OrderedDict

from converter.qiskit.backends import BaseProvider

from .credentials._configrc import remove_credentials
from .credentials import (Credentials,
from .ibmqaccounterror import IBMQAccountError
from .ibmqsingleprovider import IBMQSingleProvider



class IBMQProvider(BaseProvider):
    pass

    def __init__(self):
        pass


    def backends(self, name=None, filters=None, **kwargs):
        pass








    def deprecated_backend_names():
        pass

    def aliased_backend_names():
        pass

    def enable_account(self, token, url=QE_URL, **kwargs):
        pass




    def save_account(self, token, url=QE_URL, **kwargs):
        pass





    def active_accounts(self):
        pass



    def stored_accounts(self):
        pass



    def load_accounts(self, **kwargs):
        pass





    def disable_accounts(self, **kwargs):
        pass





    def delete_accounts(self, **kwargs):
        pass





    def _append_account(self, credentials):
        pass





    def _credentials_match_filter(self, credentials, filter_dict):
        pass



