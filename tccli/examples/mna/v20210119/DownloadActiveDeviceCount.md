**Example 1: 下载活跃设备数量统计**

下载活跃设备数量统计

Input: 

```
tccli mna DownloadActiveDeviceCount --cli-unfold-argument  \
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
        "FilePath": "http://cos.com",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

