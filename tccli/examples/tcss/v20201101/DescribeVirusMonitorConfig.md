**Example 1: 运行时查询文件查杀实时监控设置信息**

运行时查询文件查杀实时监控设置信息

Input: 

```
tccli tcss DescribeVirusMonitorConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EnableScan": true,
        "IsIncludePath": true,
        "ScanPath": [
            "abc"
        ],
        "ScanPathMode": "abc",
        "RequestId": "abc"
    }
}
```

