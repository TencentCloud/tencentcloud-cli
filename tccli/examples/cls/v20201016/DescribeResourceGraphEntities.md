**Example 1: 带过滤条件查询**



Input: 

```
tccli cls DescribeResourceGraphEntities --cli-unfold-argument  \
    --ResourceGraphId badc7d81-70a6-4979-aa54-59ae51a4870a \
    --Filters.0.Key Product \
    --Filters.0.Values tke
```

Output: 
```
{
    "Response": {
        "EntityInfos": [
            {
                "Attributes": [
                    {
                        "Key": "cluster_id",
                        "Value": "cls-3js81lg0"
                    }
                ],
                "Domain": "k8s",
                "EntityClassName": "k8s.node",
                "EntityId": "0db13f1dc7b4e58d90cb1e00d506516e",
                "EntityName": "172.16.0.37",
                "Product": "",
                "RelatedLogTopics": [],
                "Tags": []
            }
        ],
        "HasMore": 0,
        "NextCursor": "",
        "RequestId": "32666ac9-87d7-49ab-aa01-98c569817625"
    }
}
```

