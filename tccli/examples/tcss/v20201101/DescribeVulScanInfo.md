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
        "FoundRiskImageCount": 0,
        "FoundVulCount": 0,
        "IgnoreVulCount": 0,
        "LocalImageScanCount": 0,
        "LocalTaskID": 0,
        "RegistryFoundVulCount": 0,
        "RegistryImageScanCount": 0,
        "RegistryTaskID": 0,
        "RemainingTime": 0,
        "RequestId": "b6cffd6d-b5a4-41d2-8ffc-21e5cbdee3b5",
        "ScanEndTime": "2020-11-21 15:16:00",
        "ScanProgress": 0,
        "ScanStartTime": "2020-11-21 15:16:00",
        "Status": "NOT_SCAN"
    }
}
```

