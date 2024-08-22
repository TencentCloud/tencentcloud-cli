**Example 1: 查询定时检测配置信息**

使用appid查询定时检测配置的信息

Input: 

```
tccli cwp DescribeScanVulSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "VulCategories": "abc",
        "VulLevels": "abc",
        "TimerInterval": 1,
        "TimerTime": "abc",
        "VulEmergency": 1,
        "StartTime": "abc",
        "EnableScan": 1,
        "EndTime": "abc",
        "ClickTimeout": 1,
        "Uuids": [
            "abc"
        ],
        "ScanMethod": 1,
        "RequestId": "abc"
    }
}
```

