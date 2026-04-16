**Example 1: 查询不一致数据详情信息**



Input: 

```
tccli dts DescribeCompareDiffItems --cli-unfold-argument  \
    --JobId dts-test \
    --CompareTaskId dts-test-cmp-1234 \
    --ChunkId 2 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Items": [
            {
                "DBName": "db1",
                "TableName": "t1",
                "ChunkId": 0,
                "Identifier": "pk",
                "DiffType": "data",
                "SchemaInfo": [
                    "c1"
                ],
                "SrcItem": [
                    "value1"
                ],
                "DstItem": [
                    "value2"
                ],
                "FinishedAt": "2023-12-19 15:54:18"
            }
        ],
        "RequestId": "9efd789e-5d6a-4031-b5b8-6d1f031ec614"
    }
}
```

