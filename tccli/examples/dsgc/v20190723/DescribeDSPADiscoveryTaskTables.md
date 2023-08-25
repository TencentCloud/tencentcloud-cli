**Example 1: 获取分级分级扫描的表集合**

xx

Input: 

```
tccli dsgc DescribeDSPADiscoveryTaskTables --cli-unfold-argument  \
    --DbResultId 1 \
    --DspaId dspa-001 \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "Items": [
            {
                "TableName": "test"
            }
        ]
    }
}
```

