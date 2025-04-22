**Example 1: 获取索引元数据**

获取索引元数据

Input: 

```
tccli es DescribeIndexList --cli-unfold-argument  \
    --Username elastic \
    --IndexName index_test \
    --IndexType auto \
    --InstanceId es-abcdefgh \
    --Limit 0 \
    --Offset 10 \
    --Password ascq23***********cjaw
```

Output: 
```
{
    "Response": {
        "IndexMetaFields": [
            {
                "IndexType": "auto",
                "IndexName": "index_test",
                "IndexMetaJson": "{\"f1\":52}",
                "IndexStatus": "green",
                "IndexStorage": 0,
                "IndexCreateTime": "2024-12-05 17:22:44",
                "BackingIndices": [
                    {
                        "IndexName": "index_test0",
                        "IndexStatus": "green",
                        "IndexStorage": 0,
                        "IndexPhrase": "data_hot",
                        "IndexCreateTime": "2024-12-05 17:22:44"
                    }
                ],
                "ClusterId": "es-hhio223",
                "ClusterName": "test-cluster",
                "ClusterVersion": "7.14.0",
                "IndexPolicyField": {
                    "WarmEnable": "true",
                    "WarmMinAge": "16",
                    "ColdEnable": "true",
                    "ColdMinAge": "8",
                    "FrozenEnable": "false",
                    "FrozenMinAge": "0",
                    "ColdAction": "migrate"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "1d",
                    "ExpireMaxSize": "1024",
                    "RolloverMaxAge": "1d",
                    "RolloverDynamic": "true",
                    "ShardNumDynamic": "true",
                    "TimestampField": "TIMESTAMP",
                    "WriteMode": "append_only"
                },
                "IndexSettingsField": {
                    "NumberOfShards": "2",
                    "NumberOfReplicas": "1",
                    "RefreshInterval": "30s"
                },
                "AppId": 1,
                "IndexDocs": 1
            }
        ],
        "TotalCount": 0,
        "RequestId": "ah782-j*************c-ih89"
    }
}
```

