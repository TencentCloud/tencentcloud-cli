**Example 1: 活跃设备数量统计**

查询活跃设备数量统计

Input: 

```
tccli mna GetActiveDeviceCount --cli-unfold-argument  \
    --Period 0 \
    --StartTime 1732176361 \
    --EndTime 1732176362 \
    --DevGroup comollit \
    --LicenseType 3
```

Output: 
```
{
    "Response": {
        "ActiveDeviceList": [
            {
                "Count": 1,
                "Time": "2024-11-20"
            }
        ],
        "DevGroup": "group1",
        "EndTime": "2024-11-20",
        "LicenseType": "1",
        "Period": 0,
        "StartTime": "2024-11-20",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

