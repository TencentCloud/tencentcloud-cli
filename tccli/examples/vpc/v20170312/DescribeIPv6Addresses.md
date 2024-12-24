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
                "AddressName": "demo",
                "AddressStatus": "BIND",
                "AddressIp": "2402:4e00:1200:310d:0:9c6a:ffde:f722",
                "InstanceId": "ins-qfuu0g3x",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "NetworkInterfaceId": "eni-gl7hf76q",
                "PrivateAddressIp": "2402:4e00:1200:310d:0:9c6a:ffde:f722",
                "IsArrears": true,
                "IsBlocked": true,
                "IsEipDirectConnection": true,
                "AddressType": "EIP6",
                "CascadeRelease": true,
                "EipAlgType": {
                    "Ftp": true,
                    "Sip": true
                },
                "InternetServiceProvider": "BGP",
                "LocalBgp": true,
                "Bandwidth": 1,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "TagSet": [
                    {
                        "Key": "name",
                        "Value": "Sam"
                    }
                ],
                "DeadlineDate": "2020-09-22",
                "InstanceType": "CVM",
                "Egress": "CENTER_EGRESS_1"
            }
        ],
        "RequestId": "95eb79b9-2e72-45b1-a1ac-03138778521a"
    }
}
```

