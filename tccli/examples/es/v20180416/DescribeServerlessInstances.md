**Example 1: Serverless获取索引列表**



Input: 

```
tccli es DescribeServerlessInstances --cli-unfold-argument  \
    --IndexNames test \
    --InstanceIds index-abcdefgh \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "IndexMetaFields": [
            {
                "IndexOptionsField": {
                    "ExpireMaxAge": "xx",
                    "TimestampField": "xx"
                },
                "IndexName": "xx",
                "IndexSettingsField": {
                    "NumberOfShards": "xx",
                    "RefreshInterval": "xx"
                },
                "IndexNetworkField": null,
                "IndexCreateTime": "xx",
                "IndexStorage": 0
            }
        ]
    }
}
```

