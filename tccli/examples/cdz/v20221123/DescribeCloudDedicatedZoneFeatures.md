**Example 1: 查询专属可用区可用区级特性**

查询专属可用区可用区级特性

Input: 

```
tccli cdz DescribeCloudDedicatedZoneFeatures --cli-unfold-argument  \
    --Filters.0.Name zone-id \
    --Filters.0.Values 2000800003 \
    --Filters.1.Name feature-key \
    --Filters.1.Values CDZ_CLB_PUSH_SWITCH \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "FeatureSet": [
            {
                "ZoneId": "2000800003",
                "FeatureKey": "CDZ_CLB_PUSH_SWITCH",
                "FeatureValue": "0",
                "FeatureName": "负载均衡CLB不推量",
                "FeatureDescription": ""
            }
        ],
        "RequestId": "2628d149-a59c-4cf0-abc7-79ba9dc78522"
    }
}
```

