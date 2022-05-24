**Example 1: 获取索引元数据**



Input: 

```
tccli es DescribeIndexList --cli-unfold-argument  \
    --Username xx \
    --IndexName xx \
    --IndexType xx \
    --InstanceId xx \
    --Limit 0 \
    --Offset 0 \
    --Password xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "IndexMetaFields": [
            {
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
                "IndexStorage": 0
            }
        ]
    }
}
```

