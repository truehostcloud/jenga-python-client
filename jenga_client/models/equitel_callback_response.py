# coding: utf-8

"""
    Jenga API

    API for Jenga payment processing and transaction management

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class EquitelCallbackResponse(BaseModel):
    """
    EquitelCallbackResponse
    """ # noqa: E501
    status: Optional[StrictBool] = Field(default=None, description="Transaction status")
    code: Optional[StrictInt] = Field(default=None, description="Status code")
    message: Optional[StrictStr] = Field(default=None, description="Status message")
    transaction_reference: Optional[StrictStr] = Field(default=None, description="Transaction reference number", alias="transactionReference")
    telco_reference: Optional[StrictStr] = Field(default=None, description="Telco reference number", alias="telcoReference")
    mobile_number: Optional[StrictStr] = Field(default=None, description="Payer's mobile number", alias="mobileNumber")
    debited_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount debited from payer", alias="debitedAmount")
    request_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Original requested amount", alias="requestAmount")
    charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Service charge")
    currency: Optional[StrictStr] = Field(default=None, description="Transaction currency")
    telco: Optional[StrictStr] = Field(default=None, description="Telco provider")
    __properties: ClassVar[List[str]] = ["status", "code", "message", "transactionReference", "telcoReference", "mobileNumber", "debitedAmount", "requestAmount", "charge", "currency", "telco"]

    @field_validator('code')
    def code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2, 3, 4, 5, 6, 7]):
            raise ValueError("must be one of enum values (0, 1, 2, 3, 4, 5, 6, 7)")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EquitelCallbackResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EquitelCallbackResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "code": obj.get("code"),
            "message": obj.get("message"),
            "transactionReference": obj.get("transactionReference"),
            "telcoReference": obj.get("telcoReference"),
            "mobileNumber": obj.get("mobileNumber"),
            "debitedAmount": obj.get("debitedAmount"),
            "requestAmount": obj.get("requestAmount"),
            "charge": obj.get("charge"),
            "currency": obj.get("currency"),
            "telco": obj.get("telco")
        })
        return _obj


