**Example 1: 获取索引元数据**



Input: 

```
tccli es DescribeIndexMeta --cli-unfold-argument  \
    --InstanceId xx \
    --Username xx \
    --Password xx \
    --IndexName xx \
    --IndexType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "IndexMetaField": {
            "BackingIndices": [
                {
                    "IndexPhrase": "xx",
                    "IndexStatus": "xx",
                    "IndexStorage": 0,
                    "IndexName": "xx",
                    "IndexCreateTime": "xx"
                }
            ],
            "IndexOptionsField": {
                "WriteMode": "xx",
                "RolloverMaxAge": "xx",
                "ExpireMaxAge": "xx",
                "RolloverDynamic": "xx",
                "ExpireMaxSize": "xx",
                "ShardNumDynamic": "xx",
                "TimestampField": "xx"
            },
            "IndexName": "xx",
            "IndexType": "xx",
            "IndexPolicyField": {
                "WarmEnable": "xx",
                "WarmMinAge": "xx",
                "ColdMinAge": "xx",
                "FrozenEnable": "xx",
                "FrozenMinAge": "xx",
                "ColdEnable": "xx"
            },
            "ClusterName": "xx",
            "IndexStatus": "xx",
            "ClusterId": "xx",
            "IndexCreateTime": "xx",
            "ClusterVersion": "xx",
            "IndexStorage": 0,
            "IndexSettingsField": {
                "NumberOfShards": "xx",
                "NumberOfReplicas": "xx",
                "RefreshInterval": "xx"
            }
        }
    }
}
```

