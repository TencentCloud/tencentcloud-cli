**Example 1: 获取日志导出列表**



Input: 

```
tccli cls DescribeExports --cli-unfold-argument  \
    --TopicId ee20bb16-3025-4048-b81a-dd436373062e \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "Exports": [
            {
                "TopicId": "ee20bb16-3025-4048-b81a-dd436373062e",
                "ExportId": "export-57196a6a-7622-47be-bc92-d2ebea959a0f",
                "Query": "status:200",
                "FileName": "log_2075178708_ee20bb16-3025-4048-b81a-dd436373062f_20210107_xxxxxx_1610001073.tar.gz",
                "CosPath": "https://clstest01-xxxxxx.cos.ap-shanghai.myqcloud.com/xxxxxx",
                "FileSize": 6112993,
                "Order": "desc",
                "Format": "json",
                "Count": 100000,
                "Status": "Completed",
                "From": 1607499207000,
                "To": 1607499207000,
                "CreateTime": "2020-08-08 12:12:12"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

