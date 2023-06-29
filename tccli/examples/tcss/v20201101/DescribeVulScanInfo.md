**Example 1: 查询漏洞扫描任务信息**



Input: 

```
tccli tcss DescribeVulScanInfo --cli-unfold-argument  \
    --LocalTaskID 1 \
    --RegistryTaskID 1
```

Output: 
```
{
    "Response": {
        "Status": "xx",
        "IgnoreVulCount": 0,
        "LocalImageScanCount": 1,
        "ScanEndTime": "xx",
        "ScanProgress": 0.0,
        "ScanStartTime": "xx",
        "RegistryImageScanCount": 1,
        "RegistryTaskID": 0,
        "RemainingTime": 0.0,
        "RegistryFoundVulCount": 0,
        "RequestId": "xx",
        "LocalTaskID": 0,
        "FoundRiskImageCount": 0,
        "FoundVulCount": 0
    }
}
```

