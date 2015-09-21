# coding: utf-8
import hashlib
import types

import requests

from ._compat import json


class FreshMailAdapter(object):

    base_url = 'https://api.freshmail.com/'
    postfix = 'rest/'
    api_key = None
    api_secret = None
    post_methods_list = (
        'ping',
        'campaigns_edit', 'campaigns_delete', 'campaigns_sendTest', 'campaigns_send', 'campaigns_create',
        'subscriber_addMultiple', 'subscriber_editMultiple', 'subscriber_updateFieldValue',
        'account_create',
        'subscribers_list_create', 'subscribers_list_update', 'subscribers_list_delete', 'subscribers_list_lists',
        'subscribers_list_addField', 'subscribers_list_getFields',
        'spam_test_check',
        'subscriber_add', 'subscriber_edit', 'subscriber_delete', 'subscriber_getHistory',
    )

    def __init__(self, api_key='', api_secret=''):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_sign(self, data, method_name):
        return hashlib.sha1(
            ''.join((self.api_key, '/', self.postfix, method_name, data, self.api_secret)).encode('utf8')
        ).hexdigest()

    def _post(self, data, method_name):
        data = json.dumps(data)
        method_name = method_name.replace('_', '/')
        return requests.post(
            ''.join((self.base_url, self.postfix, method_name)),
            data=data,
            headers={
                'content-type': 'application/json',  # It super-header is required for freshmail...
                'X-Rest-ApiKey': self.api_key,
                'X-Rest-ApiSign': self.get_sign(data, method_name)
            }
        )

    def __getattr__(self, method_name):
        if method_name not in self.post_methods_list:
            raise AttributeError(method_name)

        def wrapper(self, data=None):
            return self._post(data or {}, method_name)

        return types.MethodType(wrapper, self)
