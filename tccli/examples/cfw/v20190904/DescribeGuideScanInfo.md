**Example 1: DescribeGuideScanInfo新手引导扫描接口信息**

DescribeGuideScanInfo新手引导扫描接口信息

Input: 

```
tccli cfw DescribeGuideScanInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "ScanPercent": 1,
            "ScanResultInfo": {
                "BanStatus": true,
                "IPNum": 34,
                "IPStatus": true,
                "IdpStatus": true,
                "LeakNum": 209,
                "PortNum": 0
            },
            "ScanStatus": 1,
            "ScanTime": "2024-11-01 03:11:01"
        },
        "RequestId": "e2633cf5-9a5f-48d9-84c6-ee4e762dab49"
    }
}
```

