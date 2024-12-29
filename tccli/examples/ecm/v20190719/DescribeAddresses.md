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
                "AddressName": "demo",
                "AddressIp": "123.121.34.33",
                "AddressStatus": "BINDED",
                "AddressType": "EIP",
                "InstanceId": "ins-11221122",
                "NetworkInterfaceId": "eni-2regnhmp",
                "PrivateAddressIp": "10.212.0.26",
                "IsArrears": false,
                "IsBlocked": false,
                "IsEipDirectConnection": true,
                "CascadeRelease": false,
                "CreatedTime": "2024-12-03T02:19:31Z",
                "Bandwidth": 2048,
                "PayMode": "BANDWIDTH_PACKAGE",
                "InternetServiceProvider": "CUCC"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

