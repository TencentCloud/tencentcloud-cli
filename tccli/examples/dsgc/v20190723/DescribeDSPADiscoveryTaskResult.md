**Example 1: 获取分类分级任务结果**



Input: 

```
tccli dsgc DescribeDSPADiscoveryTaskResult --cli-unfold-argument  \
    --DataSourceType cdb \
    --DspaId dspa-8u9asd2h \
    --Limit 10 \
    --TaskId 1 \
    --Offset 0 \
    --TaskName 自定义分类分级任务结果获取实验
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "TotalCount": 1,
        "Items": [
            {
                "DbResultId": 5640,
                "TaskId": 14596,
                "TaskName": "通用规则集验证",
                "DataSourceId": "cdb-6cfae42v",
                "DataSourceName": "新采集实验数据源",
                "ResourceRegion": "ap-guangzhou",
                "ResultId": 4242,
                "DbName": "dsgctest001",
                "TotalTables": 1,
                "SensitiveTables": 0,
                "SensitiveField": 0,
                "TotalField": 51,
                "EndTime": "2024-11-05 17:17:30",
                "Status": 3,
                "ErrorInfo": "没有错误则为空，有错误可能报错如：连接数据源错误"
            }
        ]
    }
}
```

