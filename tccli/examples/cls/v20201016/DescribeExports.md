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
                "FileName": "log_2075178708_ee20bb16-3025-4048-b81a-dd436373062f_20210107_57196a6a-7622-47be-bc92-d2ebea959a0f_1610001073.tar.gz",
                "CosPath": "https://clstest01-12541396564.cos.ap-shanghai.myqcloud.com/%2Fexport%2F20210107%2Flog_2075178708_ee20bb16-3025-4048-b81a-dd436373062f_20210107_57196a6a-7622-47be-bc92-d2ebea959a0f_1610001073.tar.gz?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDnQ16HN6rFjOXItk4ziOpX1tkRxHT57bH%26q-sign-time%3D1610011156%3B1610014756%26q-key-time%3D1610011156%3B1610014756%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D951640af88654d735dd98fd1e62b96ce75eb39f3",
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

