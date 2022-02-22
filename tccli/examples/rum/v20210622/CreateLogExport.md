**Example 1: 创建日志下载任务**



Input: 

```
tccli rum CreateLogExport --cli-unfold-argument  \
    --ID 1 \
    --StartTime 2022-01-20 00:00:00 \
    --EndTime 2022-01-21 00:00:00 \
    --Count 1 \
    --Query *
```

Output: 
```
{
    "Response": {
        "ExportID": "export-xxx",
        "RequestId": "ec04a9c2-2815-4314-abf8-bc648de7b7b2"
    }
}
```

