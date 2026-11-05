**Example 1: 活跃设备数量统计**

查询活跃设备数量统计

Input: 

```
tccli mna GetActiveDeviceCount --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ActiveDeviceList": [
            {
                "Count": 0,
                "Time": "2026-09-03"
            }
        ],
        "DevGroup": "",
        "EndTime": "2026-09-10",
        "LicenseType": "",
        "Period": 0,
        "StartTime": "2026-09-03",
        "RequestId": "ef73557b-01ee-4961-b597-2c062b2c495e"
    }
}
```

**Example 2: 按应用活跃设备数量统计**

查询指定应用活跃设备数量

Input: 

```
tccli mna GetActiveDeviceCount --cli-unfold-argument  \
    --ApplicationId app-zdsbik***e
```

Output: 
```
{
    "Response": {
        "ActiveDeviceList": [
            {
                "Count": 0,
                "Time": "2026-09-02"
            }
        ],
        "DevGroup": "app-zdsbik***e",
        "EndTime": "2026-09-09",
        "LicenseType": "",
        "Period": 0,
        "StartTime": "2026-09-02",
        "RequestId": "09ae639a-2650-40f4-8bf5-abc2ceda8bb0"
    }
}
```

