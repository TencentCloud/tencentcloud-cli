**Example 1: 根据IPv6AddressIds查询IPv6信息**

	
根据IPv6AddressIds查询IPv6信息。

Input: 

```
tccli vpc DescribeIPv6Addresses --cli-unfold-argument  \
    --IPv6AddressIds eipv6-11112222
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "AddressSet": [
            {
                "AddressId": "eipv6-11112222",
                "AddressName": "abc",
                "AddressStatus": "abc",
                "AddressIp": "abc",
                "InstanceId": "abc",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "NetworkInterfaceId": "abc",
                "PrivateAddressIp": "abc",
                "IsArrears": true,
                "IsBlocked": true,
                "IsEipDirectConnection": true,
                "AddressType": "abc",
                "CascadeRelease": true,
                "EipAlgType": {
                    "Ftp": true,
                    "Sip": true
                },
                "InternetServiceProvider": "abc",
                "LocalBgp": true,
                "Bandwidth": 1,
                "InternetChargeType": "abc",
                "TagSet": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "DeadlineDate": "2020-09-22",
                "InstanceType": "abc",
                "Egress": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

