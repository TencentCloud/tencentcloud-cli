**Example 1: 示例**



Input: 

```
tccli trocket DescribeFusionInstanceList --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --TagFilters.0.TagKey abc \
    --TagFilters.0.TagValues abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Data": [
            {
                "InstanceId": "abc",
                "InstanceName": "abc",
                "Version": "abc",
                "InstanceType": "abc",
                "InstanceStatus": "abc",
                "TopicNumLimit": 0,
                "GroupNumLimit": 0,
                "PayMode": "abc",
                "ExpiryTime": 0,
                "Remark": "abc",
                "TopicNum": 0,
                "GroupNum": 0,
                "TagList": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "SkuCode": "abc",
                "TpsLimit": 0,
                "ScaledTpsLimit": 0,
                "MessageRetention": 0,
                "MaxMessageDelay": 0,
                "RenewFlag": 0,
                "InstanceItemExtraInfo": {
                    "IsVip": true,
                    "VipInstanceStatus": 0,
                    "MaxBandWidth": 0,
                    "SpecName": "abc",
                    "NodeCount": 0,
                    "MaxStorage": 0,
                    "MaxRetention": 0,
                    "MinRetention": 0,
                    "InstanceStatus": 0
                },
                "DestroyTime": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

