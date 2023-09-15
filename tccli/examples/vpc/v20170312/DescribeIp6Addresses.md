**Example 1: 根据Ip6AddressIds查询IPV6信息**

根据Ip6AddressIds查询IPV6信息。

Input: 

```
tccli vpc DescribeIp6Addresses --cli-unfold-argument  \
    --Ip6AddressIds eip-lrhy2lpe
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "AddressSet": [
            {
                "AddressId": "abc",
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

**Example 2: 根据Filter查询IPV6信息**

根据Filter查询IPV6信息。

Input: 

```
tccli vpc DescribeIp6Addresses --cli-unfold-argument  \
    --Filters.0.Name address-ip \
    --Filters.0.Values 2402:4e00:1000:2d00:0:8f3f:6:9895
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "AddressSet": [
            {
                "AddressId": "abc",
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

