**Example 1: 查询定时检测配置信息**

使用appid查询定时检测配置的信息

Input: 

```
tccli cwp DescribeScanVulSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "VulCategories": "xx",
        "TimerTime": "xx",
        "VulLevels": "xx",
        "VulEmergency": 1,
        "RequestId": "xx",
        "TimerInterval": 1,
        "EndTime": "",
        "EnableScan": 1,
        "StartTime": "",
        "ClickTimeout": 0,
        "Uuids": []
    }
}
```

