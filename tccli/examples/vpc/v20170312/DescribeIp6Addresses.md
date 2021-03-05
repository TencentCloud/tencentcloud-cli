**Example 1: 根据Ip6AddressIds查询IPV6信息**



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
                "AddressIp": "2402:4e00:1000:2d00:0:8f3f:6:9895",
                "AddressStatus": "BIND",
                "InstanceId": "ins-190087yw",
                "NetworkInterfaceId": "eni-rw4fh3gn",
                "IsArrears": false,
                "CreatedTime": "2020-01-13T04:09:52Z",
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "Bandwidth": 6
            }
        ],
        "RequestId": "bfe06911-32f5-4862-9d42-6bb4954dcb59"
    }
}
```

**Example 2: 根据Filter查询IPV6信息**



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
        "TotalCount": 1,
        "AddressSet": [
            {
                "AddressId": "eip-lrhy2lpe",
                "AddressIp": "2402:4e00:1000:2d00:0:8f3f:6:9895",
                "AddressStatus": "BIND",
                "InstanceId": "ins-190087yw",
                "NetworkInterfaceId": "eni-rw4fh3gn",
                "IsArrears": false,
                "CreatedTime": "2020-01-13T04:09:52Z",
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "Bandwidth": 6
            }
        ],
        "RequestId": "d3ac2762-ae08-44ed-98fc-65c002d916b7"
    }
}
```

