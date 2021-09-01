**Example 1: 修改监测任务的属性**

修改监测任务的属性

Input: 

```
tccli cws ModifyMonitorAttribute --cli-unfold-argument  \
    --MonitorId 1 \
    --Urls http%3A%2F%2Fwww.qcloud.com \
    --Name 漏洞扫描监测 \
    --MonitorStatus 1 \
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

