**Example 1: DescribeGuideScanInfo 新手引导扫描接口**



Input: 

```
tccli cfw DescribeGuideScanInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "ScanTime": "xx",
            "ScanPercent": 0.0,
            "ScanResultInfo": {
                "LeakNum": 1,
                "IPNum": 1,
                "IdpStatus": true,
                "PortNum": 1,
                "BanStatus": true,
                "IPStatus": true
            },
            "ScanStatus": 0
        },
        "RequestId": "xx"
    }
}
```

