**Example 1: 获取漏洞扫描配置（周期扫描）**



Input: 

```
tccli csip DescribeVulScanPeriodic --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AssetList": [
            "1****************************566****"
        ],
        "AssetRange": 0,
        "CycleType": 2,
        "CycleValue": [
            3
        ],
        "EndTime": "03:00",
        "Level": [
            "MEDIUM"
        ],
        "Method": "VersionCompare",
        "StartTime": "01:00",
        "Status": 0,
        "Timeout": 3600,
        "VulCategory": [
            "LINUX"
        ],
        "RequestId": "a9d0215e-0255-4b0a-8406-722d59c62f75"
    }
}
```

