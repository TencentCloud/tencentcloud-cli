**Example 1: 使用AddressIds查询EIP**



Input: 

```
tccli vpc DescribeAddresses --cli-unfold-argument  \
    --AddressIds eip-hxlqja90
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AddressSet": [
            {
                "AddressId": "eip-hxlqja90",
                "AddressName": "test",
                "AddressIp": "123.121.34.33",
                "AddressStatus": "BINDED",
                "InstanceId": "ins-m2j0thu6",
                "NetworkInterfaceId": null,
                "PrivateAddressIp": null,
                "IsArrears": false,
                "IsBlocked": false,
                "CreatedTime": "2017-09-12T07:52:00Z"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

