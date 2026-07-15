**Example 1: 创建日志分析日志下载任务**

下载 ID 为 “zone-2z55fgysdtmc” 的站点下，归属地区为中国大陆境内北京时间 2025-07-10 00:00:00 ～ 2025-07-11 00:00:00 之间的七层访问日志，按时间倒序，文件格式为 csv。 
日志匹配条件：请求域名为"www.example.com"，并且命中状态为“命中”或"未命中"。

Input: 

```
tccli teo CreateLogAnalysisDownloadTask --cli-unfold-argument  \
    --ZoneId zone-2z55fgysdtmc \
    --Area mainland \
    --StartTime 2025-07-10T00:00:00+08:00 \
    --EndTime 2025-07-11T00:00:00+08:00 \
    --LogType l7-access-logs \
    --Condition ${RequestHost} in ['www.example.com'] AND ${EdgeCacheStatus} in ['hit','miss'] \
    --Format csv \
    --Sort desc
```

Output: 
```
{
    "Response": {
        "RequestId": "88e4f1a4-ee44-42e9-8aa8-a9b1631ecc5e",
        "TaskId": "task-1a4wdeq2wsda"
    }
}
```

