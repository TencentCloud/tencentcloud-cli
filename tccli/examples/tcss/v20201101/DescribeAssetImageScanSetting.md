**Example 1: 获取镜像扫描设置信息**



Input: 

```
tccli tcss DescribeAssetImageScanSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "All": false,
        "Enable": true,
        "Images": [
            "sha256:f8d1d3fe96d0bb9d04eab9043b53ed5280a409db58f2506e9f65caa11bb39ad1"
        ],
        "RequestId": "6732aa52-9940-49c3-a8be-361c312b1ee5",
        "ScanPeriod": 1,
        "ScanRisk": false,
        "ScanTime": "11:05:00",
        "ScanVirus": true,
        "ScanVul": false
    }
}
```

