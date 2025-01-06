**Example 1: 根据Filter查询IPv6信息**

根据Filter查询IPv6信息。

Input: 

```
tccli vpc DescribeIp6Addresses --cli-unfold-argument  \
    --Filters.0.Values 2402:4e00:1000:2d00:0:8f3f:6:9895 \
    --Filters.0.Name address-ip
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AddressSet": [
            {
                "AddressId": "eip-lrhy2lpe",
                "AddressName": "demo",
                "AddressStatus": "BIND",
                "AddressIp": "2402:4e00:1000:2d00:0:8f3f:6:9895",
                "InstanceId": "ins-0cu6wix4",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "NetworkInterfaceId": "eni-85sohtb7",
                "PrivateAddressIp": "2402:4e00:1000:2d00:0:8f3f:6:9895",
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
                        "Key": "role",
                        "Value": "developer"
                    }
                ],
                "DeadlineDate": "2020-09-22",
                "InstanceType": "CVM",
                "Egress": "center_egress1"
            }
        ],
        "RequestId": "64b212c4-d541-44c3-80ff-1131967a77c5"
    }
}
```

**Example 2: 根据Ip6AddressIds查询IPv6信息**

根据Ip6AddressIds查询IPv6信息。

Input: 

```
tccli vpc DescribeIp6Addresses --cli-unfold-argument  \
    --Ip6AddressIds eip-lrhy2lpe
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AddressSet": [
            {
                "AddressId": "eip-lrhy2lpe",
                "AddressName": "demo",
                "AddressStatus": "BIND",
                "AddressIp": "2402:4e00:1000:2d00:0:8f3f:6:9895",
                "InstanceId": "ins-0cu6wix4",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "NetworkInterfaceId": "eni-85sohtb7",
                "PrivateAddressIp": "2402:4e00:1000:2d00:0:8f3f:6:9895",
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
                        "Key": "role",
                        "Value": "developer"
                    }
                ],
                "DeadlineDate": "2020-09-22",
                "InstanceType": "CVM",
                "Egress": "center_egress1"
            }
        ],
        "RequestId": "64b212c4-d541-44c3-80ff-1131967a77c5"
    }
}
```

