**Example 1: DescribeGuideScanInfo 新手引导扫描接口**



Input: 

```
tccli cfw DescribeGuideScanInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "ScanResultInfo": {
                "LeakNum": 1,
                "IPNum": 1,
                "PortNum": 1,
                "IPStatus": true,
                "IdpStatus": true,
                "BanStatus": true
            },
            "ScanStatus": 0,
            "ScanPercent": 0,
            "ScanTime": "abc"
        },
        "RequestId": "abc"
    }
}
```

