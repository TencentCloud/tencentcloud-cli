**Example 1: 运行时查询文件查杀实时监控设置信息**

运行时查询文件查杀实时监控设置信息

Input: 

```
tccli tcss DescribeVirusMonitorConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EnableScan": false,
        "IsIncludePath": true,
        "ScanPath": [],
        "ScanPathMode": "SCAN_PATH_DEFAULT",
        "RequestId": "3850591f-7654-4491-a704-15d7e6050afb"
    }
}
```

