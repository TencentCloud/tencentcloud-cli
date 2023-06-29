**Example 1: 运行时查询文件查杀实时监控设置**

运行时查询文件查杀实时监控设置

Input: 

```
tccli tcss DescribeVirusMonitorSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "b9cd345d-9d88-4e3b-86b6-e0e5c971731a",
        "EnableScan": true,
        "ScanPathAll": true,
        "ScanPathType": 0,
        "ScanPathMode": "SCAN_PATH_DEFAULT",
        "ScanPath": []
    }
}
```

