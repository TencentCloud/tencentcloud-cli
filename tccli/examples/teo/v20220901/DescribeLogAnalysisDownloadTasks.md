**Example 1: 查询日志分析日志下载任务列表**

查询站点 ID 为 “zone-2z55fgysdtmc” 站点下，数据归属地区为中国大陆、日志类型为七层访问日志的日志分析的下载任务列表。

Input: 

```
tccli teo DescribeLogAnalysisDownloadTasks --cli-unfold-argument  \
    --ZoneId zone-2z55fgysdtmc \
    --Area mainland \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "88e4f1a4-ee44-42e9-8aa8-a9b1631ecc5e",
        "TotalCount": 1,
        "Tasks": [
            {
                "TaskId": "export-c99fd900-1bcb-4137-8405-496462dce729",
                "ZoneId": "zone-2z55fgysdtmc",
                "Area": "mainland",
                "StartTime": "2025-07-10T00:00:00+08:00",
                "EndTime": "2025-07-11T00:00:00+08:00",
                "LogType": "l7-access-logs",
                "Condition": "${RequestHost} in ['www.example.com'] AND ${EdgeCacheStatus} in ['hit','miss']",
                "Format": "csv",
                "Status": "loading",
                "Sort": "desc",
                "CreateTime": "2025-07-15T00:00:00+08:00",
                "ExpireTime": "2025-07-18T23:59:59+08:00"
            },
            {
                "TaskId": "export-d2ee4f62-54ea-4a9b-8fb8-850e3fd56038",
                "ZoneId": "zone-2z55fgysdtmc",
                "Area": "mainland",
                "StartTime": "2025-07-11T00:00:00+08:00",
                "EndTime": "2025-07-12T00:00:00+08:00",
                "LogType": "l7-access-logs",
                "Condition": "${RequestHost} in ['www.example.com'] AND ${EdgeCacheStatus} in ['hit','miss']",
                "Format": "csv",
                "Status": "completed",
                "Url": "https://export-gz-1254077820.cos.ap-guangzhou.myqcloud.com/%2Fexport/20260611/log_438167613_337ec735-21bc-4079-af63-7895ded64a92_20260611_expo*********************************************************************************************************************************************168%3B1781184768&q-key-time=1781181168%3B1781184768&q-header-list=host&q-url-param-list=&q-signature=c8a72b4c4c70443e55901c25cf489112ce85329a",
                "Sort": "desc",
                "CreateTime": "2025-07-16T00:00:00+08:00",
                "ExpireTime": "2025-07-19T23:59:59+08:00"
            }
        ]
    }
}
```

