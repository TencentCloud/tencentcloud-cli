**Example 1: 运营端获取虚拟集群列表**



Input: 

```
tccli tdmq DescribeAllTenants --cli-unfold-argument  \
    --ClusterName gz_cluster_1 \
    --TenantName devName \
    --Limit 0 \
    --SortBy createTime \
    --Offset 0 \
    --TenantId pulsar-xk3ne8k2qkp8 \
    --Types http \
    --SortOrder desc
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
                "MaxRetentionSizeInMB": 1,
                "ClusterName": "cluster001",
                "MaxMsgBacklogSize": 1,
                "UsedTopics": 0,
                "CustomerUin": "712340148907",
                "UsedNamespaces": 0,
                "MaxPublishRateInBytes": 1,
                "CreateTime": 1,
                "MaxNamespaces": 0,
                "UsedPartitions": 0,
                "CustomerAppId": "25122936212a",
                "TenantName": "devTest",
                "MaxPartitions": 0,
                "TenantId": "pulsar-xk3ne8k2qkp8",
                "Type": "TDMQ",
                "MaxDispatchRateInBytes": 1,
                "MaxPublishTps": 1,
                "PublicAccessEnabled": true
            }
        ],
        "RequestId": "d4a162ca-0c45-4244-bc14-4463b72d5e13"
    }
}
```

