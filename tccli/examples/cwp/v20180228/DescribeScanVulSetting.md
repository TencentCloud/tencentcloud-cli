**Example 1: 查询定时检测配置信息**

使用appid查询定时检测配置的信息

Input: 

```
tccli cwp DescribeScanVulSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ClickTimeout": 0,
        "EnableScan": 0,
        "EndTime": "23:50",
        "RequestId": "54111d3a-373d-4175-80dd-8d855b595647",
        "ScanMethod": 0,
        "StartTime": "00:40",
        "TimerInterval": 1,
        "TimerTime": "00:40",
        "Uuids": [],
        "VulCategories": "4;5;1;2",
        "VulEmergency": 1,
        "VulLevels": "1;2;3;4"
    }
}
```

