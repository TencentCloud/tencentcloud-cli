**Example 1: 使用AddressIds查询EIP**



Input: 

```
tccli ecm DescribeAddresses --cli-unfold-argument  \
    --AddressIds eip-11221122 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AddressSet": [
            {
                "AddressId": "eip-11221122",
                "AddressName": "test",
                "AddressIp": "123.121.34.33",
                "AddressStatus": "BINDED",
                "InstanceId": "ins-11221122",
                "NetworkInterfaceId": null,
                "PrivateAddressIp": null,
                "IsArrears": false,
                "IsBlocked": false,
                "CreatedTime": "2020-01-12T07:52:00Z"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

