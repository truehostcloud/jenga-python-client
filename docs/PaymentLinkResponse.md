# PaymentLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status | [optional] 
**code** | **int** | Response code | [optional] 
**message** | **str** | Response message | [optional] 
**metadata** | **object** | Additional metadata | [optional] 
**data** | [**PaymentLinkResponseData**](PaymentLinkResponseData.md) |  | [optional] 

## Example

```python
from jenga_client.models.payment_link_response import PaymentLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkResponse from a JSON string
payment_link_response_instance = PaymentLinkResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkResponse.to_json())

# convert the object into a dict
payment_link_response_dict = payment_link_response_instance.to_dict()
# create an instance of PaymentLinkResponse from a dict
payment_link_response_from_dict = PaymentLinkResponse.from_dict(payment_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


