# coding: utf-8

"""
    Jenga API

    API for Jenga payment processing and transaction management

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jenga_client.models.m_pesa_stk_push_response_data_order import MPesaStkPushResponseDataOrder

class TestMPesaStkPushResponseDataOrder(unittest.TestCase):
    """MPesaStkPushResponseDataOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MPesaStkPushResponseDataOrder:
        """Test MPesaStkPushResponseDataOrder
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MPesaStkPushResponseDataOrder`
        """
        model = MPesaStkPushResponseDataOrder()
        if include_optional:
            return MPesaStkPushResponseDataOrder(
                order_amount = 100.0,
                amount_paid = 0.0,
                order_reference = 'ORD1748939052F6DD4B',
                order_status = 'Expired',
                created_on = 1748939182287
            )
        else:
            return MPesaStkPushResponseDataOrder(
        )
        """

    def testMPesaStkPushResponseDataOrder(self):
        """Test MPesaStkPushResponseDataOrder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
