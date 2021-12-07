**Example 1: 运行时查询文件查杀设置**



Input: 

```
tccli tcss DescribeVirusScanSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "b9cd345d-9d88-4e3b-86b6-e0e5c971731a",
        "EnableScan": true,
        "Cycle": 1,
        "BeginScanAt": "01:00:00",
        "ScanPathAll": true,
        "ScanPathType": 0,
        "Timeout": 2,
        "ScanRangeType": 0,
        "ClickTimeout": 1,
        "ScanRangeAll": true,
        "ScanIds": [],
        "ScanPath": []
    }
}
```

