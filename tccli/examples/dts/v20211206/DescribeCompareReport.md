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
            "CheckedTables": 1,
            "Conclusion": "same",
            "DifferentRows": 0,
            "DifferentTables": 0,
            "DstSampleRows": 0,
            "FinishedAt": "2024-12-20 19:07:20",
            "NearlyTableCount": 1,
            "Objects": {
                "AdvancedObjects": [],
                "ObjectItems": [
                    {
                        "DbMode": "partial",
                        "DbName": "db_1",
                        "SchemaName": "",
                        "TableMode": "partial",
                        "Tables": [
                            {
                                "ColumnMode": "all",
                                "Columns": [],
                                "TableName": "tb_1"
                            }
                        ],
                        "ViewMode": "partial",
                        "Views": null
                    }
                ],
                "ObjectMode": "partial"
            },
            "Options": {
                "Method": "dataCheck",
                "SampleRate": 100,
                "ThreadCount": 1,
                "Type": "builtin"
            },
            "SkippedTables": 0,
            "SrcSampleRows": 0,
            "StartedAt": "2024-12-20 19:04:03",
            "Status": "success",
            "TotalTables": 1
        },
        "Detail": {
            "Difference": {
                "Items": [],
                "TotalCount": 0
            },
            "DifferenceAdvancedObjects": {
                "Items": null,
                "TotalCount": 0
            },
            "DifferenceData": {
                "Items": null,
                "TotalCount": 0
            },
            "DifferenceRow": {
                "Items": null,
                "TotalCount": 0
            },
            "Skipped": {
                "Items": [],
                "TotalCount": 0
            }
        },
        "RequestId": "a3365b29-2042-4565-9206-8df9e2af1a17"
    }
}
```

