**Example 1: 查询主机漏洞扫描状态**



Input: 

```
tccli csip DescribeHostVulScanStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Status": {
            "HasScanned": true,
            "IsFirstScan": true,
            "ScanTaskStatus": "SUCCESS",
            "ScanScene": "FIRST_SCAN_HAS_FIXABLE_VUL",
            "LatestScanTime": "2026-10-20T10:00:00Z",
            "TotalVulCount": 12,
            "FixableVulCount": 5,
            "FixableEmergencyCount": 1,
            "FixableLinuxVulCount": 2,
            "FixableWindowVulCount": 2
        },
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

