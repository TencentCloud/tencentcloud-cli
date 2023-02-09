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
                        "Key": "test"
                    }
                ],
                "RoutePriorityFlag": true,
                "CcnId": "ccn-8j0phqix",
                "CcnDescription": "test",
                "State": "AVAILABLE",
                "InstanceChargeType": "POSTPAID",
                "CcnName": "test",
                "QosLevel": "AU",
                "BandwidthLimitType": "INTER_REGION_LIMIT",
                "CreateTime": "2020-09-22 00:00:00",
                "RouteTableFlag": null,
                "RouteTableCount": null
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
    --Filters.0.Values test \
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
                        "Key": "test"
                    }
                ],
                "RoutePriorityFlag": true,
                "CcnId": "ccn-8j0phqix",
                "CcnDescription": "test",
                "State": "AVAILABLE",
                "InstanceChargeType": "POSTPAID",
                "CcnName": "test",
                "QosLevel": "AU",
                "BandwidthLimitType": "INTER_REGION_LIMIT",
                "CreateTime": "2020-09-22 00:00:00",
                "RouteTableFlag": null,
                "RouteTableCount": null
            }
        ]
    }
}
```

**Example 3: 查询绑定了标签的CCN列表**

查询绑定了标签键值对（env:test）的ccn。

Input: 

```
tccli vpc DescribeCcns --cli-unfold-argument  \
    --Filters.0.Values test \
    --Filters.0.Name tag:env
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
                        "Key": "test"
                    }
                ],
                "RoutePriorityFlag": true,
                "CcnId": "ccn-8j0phqix",
                "CcnDescription": "test",
                "State": "AVAILABLE",
                "InstanceChargeType": "POSTPAID",
                "CcnName": "test",
                "QosLevel": "AU",
                "BandwidthLimitType": "INTER_REGION_LIMIT",
                "CreateTime": "2020-09-22 00:00:00",
                "RouteTableFlag": null,
                "RouteTableCount": null
            }
        ]
    }
}
```

