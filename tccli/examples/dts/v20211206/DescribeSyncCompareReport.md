**Example 1: 查询一致性校验任务详情**



Input: 

```
tccli dts DescribeSyncCompareReport --cli-unfold-argument  \
    --JobId dts-amm1jw5q \
    --CompareTaskId dts-amm1jw5q-cmp-bmuum7jk
```

Output: 
```
{
    "Response": {
        "Abstract": {
            "Options": {
                "Method": "dataCheck",
                "SampleRate": 0,
                "ThreadCount": 0
            },
            "Objects": {
                "ObjectMode": "partial",
                "ObjectItems": [
                    {
                        "DbName": "db1",
                        "SchemaName": "s1",
                        "DbMode": "partial",
                        "TableMode": "partial",
                        "Tables": [
                            {
                                "TableName": "t1",
                                "ColumnMode": "partial",
                                "Columns": [
                                    {
                                        "ColumnName": "c1"
                                    }
                                ]
                            }
                        ],
                        "ViewMode": "partial",
                        "Views": [
                            {
                                "ViewName": "v1"
                            }
                        ]
                    }
                ],
                "AdvancedObjects": [
                    "test_t"
                ]
            },
            "CheckedTables": 4,
            "Conclusion": "same",
            "DifferentRows": 0,
            "DifferentTables": 0,
            "SkippedTables": 0,
            "Status": "success",
            "TotalTables": 4,
            "SrcSampleRows": 1,
            "DstSampleRows": 1,
            "StartedAt": "2023-11-02 10:20:30",
            "FinishedAt": "2023-11-02 10:20:30",
            "NearlyTableCount": 1
        },
        "Detail": {
            "Difference": {
                "Items": [],
                "TotalCount": 0
            },
            "Skipped": {
                "Items": [],
                "TotalCount": 0
            }
        },
        "RequestId": "ac300ff0-00f2-11ed-b005-4930e69d89c2"
    }
}
```

