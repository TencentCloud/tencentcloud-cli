**Example 1: 运行时查询文件查杀新设置**

运行时查询文件查杀新设置

Input: 

```
tccli tcss DescribeVirusScanConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EnableScan": true,
        "Cycle": 1,
        "BeginScanAt": "abc",
        "Timeout": 1,
        "ScanRangeType": "abc",
        "ScanIDs": [
            {
                "IsAll": true,
                "RangeType": "abc",
                "IDs": [
                    "abc"
                ]
            }
        ],
        "ScanPath": [
            "abc"
        ],
        "ScanPathMode": "abc",
        "IsIncludePath": true,
        "RequestId": "abc"
    }
}
```

