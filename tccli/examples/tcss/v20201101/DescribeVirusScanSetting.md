**Example 1: 运行时查询文件查杀设置**

运行时查询文件查杀设置

Input: 

```
tccli tcss DescribeVirusScanSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BeginScanAt": "10:59:00",
        "ClickTimeout": 0,
        "Cycle": 1,
        "EnableScan": true,
        "RequestId": "def074cf-2ad4-4895-bc34-e1607b094a4e",
        "ScanIds": [
            "ad297b24a4f818d9da49c9bec10d54c179b6751fc362802b077f710b3638e0f0"
        ],
        "ScanPath": [
            "/tmp"
        ],
        "ScanPathAll": false,
        "ScanPathMode": "SCAN_PATH_USER_DEFINE",
        "ScanPathType": 0,
        "ScanRangeAll": false,
        "ScanRangeType": 0,
        "Timeout": 5
    }
}
```

