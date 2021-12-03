**Example 1: 运营端获取虚拟集群列表**



Input: 

```
tccli tdmq DescribeAllTenants --cli-unfold-argument  \
    --ClusterName xx \
    --TenantName xx \
    --Limit 0 \
    --SortBy xx \
    --Offset 0 \
    --TenantId xx \
    --Types xx \
    --SortOrder xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Tenants": [
            {
                "MaxRetention": 1,
                "MaxDispatchTps": 1,
                "UpdateTime": 1,
                "MaxTopics": 0,
                "ClusterName": "xx",
                "MaxMsgBacklogSize": 1,
                "UsedTopics": 0,
                "CustomerUin": "xx",
                "UsedNamespaces": 0,
                "MaxNamespaces": 0,
                "UsedPartitions": 0,
                "CustomerAppId": "xx",
                "TenantName": "xx",
                "MaxPartitions": 0,
                "TenantId": "xx",
                "Type": "xx",
                "CreateTime": 1,
                "MaxPublishTps": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

