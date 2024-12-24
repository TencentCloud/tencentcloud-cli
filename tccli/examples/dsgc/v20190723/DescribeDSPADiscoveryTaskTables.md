**Example 1: 获取分级分级扫描的表集合**

获取分级分级扫描的表集合

Input: 

```
tccli dsgc DescribeDSPADiscoveryTaskTables --cli-unfold-argument  \
    --DbResultId 1 \
    --DspaId dspa-890ad3cv \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "Items": [
            {
                "TableName": "t_order"
            }
        ]
    }
}
```

