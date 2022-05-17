**Example 1: 七层离线日志**



Input: 

```
tccli teo DownloadL7Logs --cli-unfold-argument  \
    --PageNo 0 \
    --PageSize 0 \
    --Zones xx \
    --StartTime 2022-05-04T03:27:00+08:00 \
    --Domains xx \
    --EndTime 2022-05-10T23:59:00+08:00
```

Output: 
```
{
    "Response": {
        "PageSize": 0,
        "PageNo": 0,
        "TotalSize": 0,
        "RequestId": "xx",
        "Data": [
            {
                "Url": "xx",
                "Domain": "xx",
                "LogPacketName": "xx",
                "LogTime": 0,
                "Size": 0
            }
        ],
        "Pages": 0
    }
}
```

