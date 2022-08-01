**Example 1: 查询监测列表**



Input: 

```
tccli bma DescribeCRMonitors --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "Monitors": [
            {
                "TortURLNum": 0,
                "MonitorStatus": 1,
                "WorkId": 39,
                "TortPlatNum": 0,
                "WorkName": "xx",
                "InsertTime": "xx",
                "WorkCategory": "xx",
                "MonitorNote": "xx",
                "MonitorTime": "xx",
                "WorkType": "xx"
            },
            {
                "TortURLNum": 0,
                "MonitorStatus": 1,
                "WorkId": 38,
                "TortPlatNum": 0,
                "WorkName": "xx",
                "InsertTime": "xx",
                "WorkType": "xx",
                "MonitorNote": "xx",
                "MonitorTime": "xx",
                "WorkCategory": "xx"
            },
            {
                "TortURLNum": 0,
                "MonitorStatus": 1,
                "WorkId": 37,
                "TortPlatNum": 0,
                "WorkName": "xx",
                "InsertTime": "xx",
                "WorkType": "xx",
                "MonitorNote": "xx",
                "MonitorTime": "xx",
                "WorkCategory": "xx"
            },
            {
                "TortURLNum": 4,
                "MonitorStatus": 1,
                "WorkId": 36,
                "TortPlatNum": 4,
                "WorkName": "xx",
                "InsertTime": "xx",
                "WorkType": "xx",
                "MonitorNote": "xx",
                "MonitorTime": "xx",
                "WorkCategory": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

