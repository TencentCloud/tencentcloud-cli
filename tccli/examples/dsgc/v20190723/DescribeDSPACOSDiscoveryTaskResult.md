**Example 1: DescribeCOSTaskResult**



Input: 

```
tccli dsgc DescribeDSPACOSDiscoveryTaskResult --cli-unfold-argument  \
    --DspaId dspa-2jnk9scx \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name DataSourceId \
    --Filters.0.Values cos-1bhjsad71h2eb21j2134b1jh
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BucketResultId": 1,
                "TaskId": 1,
                "TaskName": "cos分类分级测试",
                "ResultId": 1,
                "DataSourceId": "cos-1bhjsad71h2eb21j2134b1jh",
                "BucketName": "cos_bucket",
                "TotalFiles": 20,
                "SensitiveDataNums": 120,
                "EndTime": "2024-10-10 12:00:00",
                "DataSourceName": "cos数据源1",
                "Status": 0,
                "ErrorInfo": "没有错误则为空，有错误可能报错如：连接数据源错误",
                "ResourceRegion": "ap-guangzhou",
                "OverSize": "OverQuotaSuccess"
            }
        ],
        "TotalCount": 1,
        "RequestId": "826f0635-b168-52a7-8db9-45b1d46d2c8a"
    }
}
```

