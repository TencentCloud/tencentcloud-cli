**Example 1: 获取索引元数据**

获取索引元数据

Input: 

```
tccli es DescribeIndexMeta --cli-unfold-argument  \
    --InstanceId abc \
    --Username abc \
    --Password abc \
    --IndexName abc \
    --IndexType abc
```

Output: 
```
{
    "Response": {
        "IndexMetaField": {
            "IndexType": "abc",
            "IndexName": "abc",
            "IndexMetaJson": "abc",
            "IndexStatus": "abc",
            "IndexStorage": 0,
            "IndexCreateTime": "abc",
            "BackingIndices": [
                {
                    "IndexName": "abc",
                    "IndexStatus": "abc",
                    "IndexStorage": 0,
                    "IndexPhrase": "abc",
                    "IndexCreateTime": "abc"
                }
            ],
            "ClusterId": "abc",
            "ClusterName": "abc",
            "ClusterVersion": "abc",
            "IndexPolicyField": {
                "WarmEnable": "abc",
                "WarmMinAge": "abc",
                "ColdEnable": "abc",
                "ColdMinAge": "abc",
                "FrozenEnable": "abc",
                "FrozenMinAge": "abc",
                "ColdAction": "abc"
            },
            "IndexOptionsField": {
                "ExpireMaxAge": "abc",
                "ExpireMaxSize": "abc",
                "RolloverMaxAge": "abc",
                "RolloverDynamic": "abc",
                "ShardNumDynamic": "abc",
                "TimestampField": "abc",
                "WriteMode": "abc"
            },
            "IndexSettingsField": {
                "NumberOfShards": "abc",
                "NumberOfReplicas": "abc",
                "RefreshInterval": "abc"
            },
            "AppId": 1,
            "IndexDocs": 1
        },
        "RequestId": "abc"
    }
}
```

