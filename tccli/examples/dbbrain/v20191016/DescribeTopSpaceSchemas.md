**Example 1: 获取Top库的空间统计信息**

获取Top库的空间统计信息。

Input: 

```
tccli dbbrain DescribeTopSpaceSchemas --cli-unfold-argument  \
    --InstanceId cdb-test \
    --Limit 2 \
    --SortBy TableRows
```

Output: 
```
{
    "Response": {
        "RequestId": "ed279d8b-a9d9-48d6-9429-e0fde000994a",
        "Timestamp": 1603819881,
        "TopSpaceSchemas": [
            {
                "DataFree": 0,
                "TotalLength": 0.1,
                "TableSchema": "test_bak",
                "FragRatio": 0,
                "DataLength": 0.1,
                "PhysicalFileSize": 0.1,
                "TableRows": 9,
                "IndexLength": 0
            },
            {
                "DataFree": 0,
                "TotalLength": 0.1,
                "TableSchema": "test_bak",
                "FragRatio": 0,
                "DataLength": 0.1,
                "PhysicalFileSize": 0.1,
                "TableRows": 9,
                "IndexLength": 0
            }
        ]
    }
}
```

