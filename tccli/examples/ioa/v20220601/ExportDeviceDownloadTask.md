**Example 1: 测试全网终端分组（ID=1120）的数据导出**

测试全网终端分组（ID=1120）的数据导出

Input: 

```
tccli ioa ExportDeviceDownloadTask --cli-unfold-argument  \
    --OsType 0 \
    --DomainInstanceId 1 \
    --GroupId 1120 \
    --ExportType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadURL": "",
            "TaskId": 186954
        },
        "RequestId": "23b2ad49-f082-401c-a3f1-8b903291d5a6"
    }
}
```

