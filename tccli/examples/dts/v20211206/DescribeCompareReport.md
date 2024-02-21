**Example 1: 查询一致性校验任务详情**



Input: 

```
tccli dts DescribeCompareReport --cli-unfold-argument  \
    --JobId dts-amm1jw5q \
    --CompareTaskId dts-amm1jw5q-cmp-bmuum7jk
```

Output: 
```
{
    "Response": {
        "Abstract": {
            "Options": {
                "Method": "abc",
                "SampleRate": 0,
                "ThreadCount": 0
            },
            "Objects": {
                "ObjectMode": "abc",
                "ObjectItems": [
                    {
                        "DbName": "abc",
                        "SchemaName": "abc",
                        "DbMode": "abc",
                        "TableMode": "abc",
                        "Tables": [
                            {
                                "TableName": "abc",
                                "ColumnMode": "abc",
                                "Columns": [
                                    {
                                        "ColumnName": "abc"
                                    }
                                ]
                            }
                        ],
                        "ViewMode": "abc",
                        "Views": [
                            {
                                "ViewName": "abc"
                            }
                        ]
                    }
                ],
                "AdvancedObjects": [
                    "abc"
                ]
            },
            "Conclusion": "abc",
            "Status": "abc",
            "TotalTables": 1,
            "CheckedTables": 1,
            "DifferentTables": 1,
            "SkippedTables": 1,
            "NearlyTableCount": 1,
            "DifferentRows": 1,
            "SrcSampleRows": 1,
            "DstSampleRows": 1,
            "StartedAt": "abc",
            "FinishedAt": "abc"
        },
        "Detail": {
            "Difference": {
                "TotalCount": 1,
                "Items": [
                    {
                        "Db": "abc",
                        "Table": "abc",
                        "Chunk": 0,
                        "SrcItem": "abc",
                        "DstItem": "abc",
                        "IndexName": "abc",
                        "LowerBoundary": "abc",
                        "UpperBoundary": "abc",
                        "CostTime": 0,
                        "FinishedAt": "abc"
                    }
                ]
            },
            "Skipped": {
                "TotalCount": 1,
                "Items": [
                    {
                        "Db": "abc",
                        "Table": "abc",
                        "Reason": "abc"
                    }
                ]
            }
        },
        "RequestId": "abc"
    }
}
```

