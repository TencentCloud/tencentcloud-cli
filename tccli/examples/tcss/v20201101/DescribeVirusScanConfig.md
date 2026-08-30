**Example 1: 运行时查询文件查杀新设置**

运行时查询文件查杀新设置

Input: 

```
tccli tcss DescribeVirusScanConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BeginScanAt": "",
        "Cycle": 0,
        "EnableScan": false,
        "IsIncludePath": false,
        "ScanIDs": [],
        "ScanPath": [],
        "ScanPathMode": "SCAN_PATH_DEFAULT",
        "ScanRangeType": "",
        "Timeout": 0,
        "RequestId": "0b3485e4-f03f-4df6-9bd5-ab7bc2f75c51"
    }
}
```

