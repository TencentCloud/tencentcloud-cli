**Example 1: 新增监测任务**

新增一个或多个站点的监测任务

Input: 

```
tccli cws CreateMonitors --cli-unfold-argument  \
    --Urls http%3A%2F%2Fwww.qcloud.com \
    --Name 漏洞扫描监测 \
    --ScannerType normal \
    --RateLimit 10 \
    --Crontab 24 \
    --FirstScanStartTime '2018-03-23 02:00:00'
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

