**Example 1: 运行时查询文件查杀设置**

运行时查询文件查杀设置

Input: 

```
tccli tcss DescribeVirusScanSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EnableScan": true,
        "Cycle": 1,
        "BeginScanAt": "xx",
        "ScanPathAll": true,
        "ScanPathType": 1,
        "Timeout": 1,
        "ScanRangeType": 1,
        "ScanRangeAll": true,
        "ScanIds": [
            "xx"
        ],
        "ScanPath": [
            "xx"
        ],
        "ClickTimeout": 1,
        "ScanPathMode": "SCAN_PATH_DEFAULT",
        "RequestId": "xx"
    }
}
```

