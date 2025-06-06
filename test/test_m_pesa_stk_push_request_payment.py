# coding: utf-8

"""
    Jenga API

    API for Jenga payment processing and transaction management

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jenga_client.models.m_pesa_stk_push_request_payment import MPesaStkPushRequestPayment

class TestMPesaStkPushRequestPayment(unittest.TestCase):
    """MPesaStkPushRequestPayment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MPesaStkPushRequestPayment:
        """Test MPesaStkPushRequestPayment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MPesaStkPushRequestPayment`
        """
        model = MPesaStkPushRequestPayment()
        if include_optional:
            return MPesaStkPushRequestPayment(
                payment_reference = 'MKQR28922980073',
                payment_currency = 'KES',
                channel = 'MOBILE',
                service = 'MPESA',
                provider = 'JENGA',
                callback_url = 'https://webhook.site/5c74a733-1caa-4f10-b876-3df9c0d7453c',
                details = jenga_client.models.m_pesa_stk_push_request_payment_details.MPesaStkPushRequest_payment_details(
                    msisdn = '0722000000', 
                    payment_amount = 2, )
            )
        else:
            return MPesaStkPushRequestPayment(
                payment_reference = 'MKQR28922980073',
                payment_currency = 'KES',
                channel = 'MOBILE',
                service = 'MPESA',
                provider = 'JENGA',
                callback_url = 'https://webhook.site/5c74a733-1caa-4f10-b876-3df9c0d7453c',
                details = jenga_client.models.m_pesa_stk_push_request_payment_details.MPesaStkPushRequest_payment_details(
                    msisdn = '0722000000', 
                    payment_amount = 2, ),
        )
        """

    def testMPesaStkPushRequestPayment(self):
        """Test MPesaStkPushRequestPayment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
