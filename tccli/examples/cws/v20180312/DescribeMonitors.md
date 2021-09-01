**Example 1: 查看监控任务**

查询一个或多个监控任务的详细信息。

Input: 

```
tccli cws DescribeMonitors --cli-unfold-argument  \
    --Filters.0.Name Name \
    --Filters.0.Values QQ 微信 \
    --Filters.1.Name MonitorStatus \
    --Filters.1.Values 1
```

Output: 
```
{
    "Response": {
        "Monitors": [
            {
                "Basic": {
                    "Appid": 1251001047,
                    "CreatedAt": "2018-03-24T15:25:37+08:00",
                    "Crontab": 2,
                    "CurrentScanStartTime": "2018-03-25T15:43:46+08:00",
                    "FirstScanStartTime": "2018-03-23T02:23:34+08:00",
                    "Id": 1,
                    "IncludedVulsTypes": "",
                    "LastScanFinishTime": "2018-03-25T15:44:00+08:00",
                    "MonitorStatus": 1,
                    "Name": "aisec相关",
                    "RateLimit": 20,
                    "ScanStatus": 2,
                    "ScannerType": "normal",
                    "UpdatedAt": "2018-03-25T15:44:00+08:00"
                },
                "ImpactSiteNumber": 2,
                "ImpactSites": [
                    {
                        "SiteId": "1",
                        "Url": "http://demo.aisec.cn/demo/aisec/"
                    },
                    {
                        "SiteId": "2",
                        "Url": "http://demo.aisec.cn/demo/wvs/"
                    }
                ],
                "SiteNumber": 2,
                "Sites": [
                    {
                        "SiteId": "1",
                        "Url": "http://demo.aisec.cn/demo/aisec/"
                    },
                    {
                        "SiteId": "2",
                        "Url": "http://demo.aisec.cn/demo/wvs/"
                    }
                ],
                "VulsHighNumber": 8,
                "VulsLowNumber": 0,
                "VulsMiddleNumber": 2,
                "VulsNoticeNumber": 2
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 1
    }
}
```

