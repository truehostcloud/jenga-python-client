# coding: utf-8

"""
    Jenga API

    API for Jenga payment processing and transaction management

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jenga_client.models.m_pesa_transaction_status_data_order import MPesaTransactionStatusDataOrder

class TestMPesaTransactionStatusDataOrder(unittest.TestCase):
    """MPesaTransactionStatusDataOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MPesaTransactionStatusDataOrder:
        """Test MPesaTransactionStatusDataOrder
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MPesaTransactionStatusDataOrder`
        """
        model = MPesaTransactionStatusDataOrder()
        if include_optional:
            return MPesaTransactionStatusDataOrder(
                order_amount = 2.0,
                amount_paid = 2.0,
                order_reference = 'OR28922980077',
                order_status = 'Paid',
                created_on = 1723209757300
            )
        else:
            return MPesaTransactionStatusDataOrder(
        )
        """

    def testMPesaTransactionStatusDataOrder(self):
        """Test MPesaTransactionStatusDataOrder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
