**Example 1: 获取索引元数据**

获取索引元数据

Input: 

```
tccli es DescribeIndexMeta --cli-unfold-argument  \
    --InstanceId es-ikbe4ku1 \
    --Username elastic \
    --Password G7j#kL9p$2w \
    --IndexName log_xxx \
    --IndexType auto
```

Output: 
```
{
    "Response": {
        "IndexMetaField": {
            "AppId": 1256050235,
            "ClusterId": "es-ikbe4ku1",
            "ClusterName": "AT-ES索引测试",
            "ClusterVersion": "7.14.2",
            "IndexType": "normal",
            "IndexName": "at-20250306061507",
            "IndexMetaJson": "{\"mappings\":{\"properties\":{\"at_field_20250306062058\":{\"analyzer\":\"ik_max_word\",\"type\":\"text\"},\"charge\":{\"type\":\"keyword\"},\"codea\":{\"type\":\"keyword\"},\"lat\":{\"type\":\"keyword\"},\"level\":{\"type\":\"keyword\"},\"location\":{\"type\":\"keyword\"},\"log\":{\"type\":\"keyword\"},\"name\":{\"type\":\"keyword\"},\"prov\":{\"type\":\"keyword\"},\"remark\":{\"type\":\"keyword\"}}},\"settings\":{\"index.number_of_replicas\":\"2\",\"index.number_of_shards\":\"1\",\"index.refresh_interval\":\"1m\"}}",
            "IndexStatus": "green",
            "IndexStorage": 366412,
            "IndexCreateTime": "2025-03-06 06:15:07",
            "IndexDocs": 348,
            "IndexSettingsField": {
                "NumberOfShards": "1",
                "NumberOfReplicas": "2",
                "RefreshInterval": "1m"
            },
            "IndexAliasesField": [],
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
            "BackingIndices": [
                {
                    "IndexName": "index_test0",
                    "IndexStatus": "green",
                    "IndexStorage": 0,
                    "IndexPhrase": "data_hot",
                    "IndexCreateTime": "2024-12-05 17:22:44"
                }
            ]
        },
        "RequestId": "8b051ef0-5802-49cd-a73f-efe0e68662cf"
    }
}
```

