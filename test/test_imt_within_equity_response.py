# coding: utf-8

"""
    Jenga API

    API for Jenga payment processing and transaction management

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jenga_client.models.imt_within_equity_response import IMTWithinEquityResponse

class TestIMTWithinEquityResponse(unittest.TestCase):
    """IMTWithinEquityResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IMTWithinEquityResponse:
        """Test IMTWithinEquityResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IMTWithinEquityResponse`
        """
        model = IMTWithinEquityResponse()
        if include_optional:
            return IMTWithinEquityResponse(
                status = True,
                code = 0,
                message = 'success',
                data = jenga_client.models.imt_within_equity_response_data.IMTWithinEquityResponse_data(
                    transaction_id = '', 
                    status = 'SUCCESS', )
            )
        else:
            return IMTWithinEquityResponse(
        )
        """

    def testIMTWithinEquityResponse(self):
        """Test IMTWithinEquityResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
