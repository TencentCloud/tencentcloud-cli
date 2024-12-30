**Example 1: 按ID过滤查询CCN列表**

按ID过滤查询CCN列表

Input: 

```
tccli vpc DescribeCcns --cli-unfold-argument  \
    --CcnIds ccn-8j0phqix
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "73159790-39b3-48e8-9d61-29e11eed1acd",
        "CcnSet": [
            {
                "InstanceCount": 1,
                "TagSet": [
                    {
                        "Value": "env",
                        "Key": "ccn-1"
                    }
                ],
                "RoutePriorityFlag": true,
                "CcnId": "ccn-8j0phqix",
                "CcnDescription": "ccn-1",
                "State": "AVAILABLE",
                "InstanceChargeType": "POSTPAID",
                "CcnName": "ccn-1",
                "QosLevel": "AU",
                "BandwidthLimitType": "INTER_REGION_LIMIT",
                "CreateTime": "2020-09-22 00:00:00",
                "RouteTableFlag": false,
                "RouteTableCount": 1,
                "RouteBroadcastPolicyFlag": false,
                "IsSecurityLock": false
            }
        ]
    }
}
```

**Example 2: 按名称过滤查询CCN列表**

按名称过滤查询CCN列表

Input: 

```
tccli vpc DescribeCcns --cli-unfold-argument  \
    --Filters.0.Values ccn-1 \
    --Filters.0.Name ccn-name
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "73159790-39b3-48e8-9d61-29e11eed1acd",
        "CcnSet": [
            {
                "InstanceCount": 1,
                "TagSet": [
                    {
                        "Value": "env",
                        "Key": "ccn-1"
                    }
                ],
                "RoutePriorityFlag": true,
                "CcnId": "ccn-8j0phqix",
                "CcnDescription": "ccn-1",
                "State": "AVAILABLE",
                "InstanceChargeType": "POSTPAID",
                "CcnName": "ccn-1",
                "QosLevel": "AU",
                "BandwidthLimitType": "INTER_REGION_LIMIT",
                "CreateTime": "2020-09-22 00:00:00",
                "RouteTableFlag": false,
                "RouteTableCount": 1,
                "RouteBroadcastPolicyFlag": false,
                "IsSecurityLock": false
            }
        ]
    }
}
```

**Example 3: 查询绑定了标签的CCN列表**

查询绑定了标签键值对（env:ccn-1）的ccn。

Input: 

```
tccli vpc DescribeCcns --cli-unfold-argument  \
    --Filters.0.Values ccn-1 \
    --Filters.0.Name tag:ccn-1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "73159790-39b3-48e8-9d61-29e11eed1acd",
        "CcnSet": [
            {
                "InstanceCount": 1,
                "TagSet": [
                    {
                        "Value": "env",
                        "Key": "ccn-1"
                    }
                ],
                "RoutePriorityFlag": true,
                "CcnId": "ccn-8j0phqix",
                "CcnDescription": "ccn-1",
                "State": "AVAILABLE",
                "InstanceChargeType": "POSTPAID",
                "CcnName": "ccn-1",
                "QosLevel": "AU",
                "BandwidthLimitType": "INTER_REGION_LIMIT",
                "CreateTime": "2020-09-22 00:00:00",
                "RouteTableFlag": false,
                "RouteTableCount": 1,
                "RouteBroadcastPolicyFlag": false,
                "IsSecurityLock": false
            }
        ]
    }
}
```

