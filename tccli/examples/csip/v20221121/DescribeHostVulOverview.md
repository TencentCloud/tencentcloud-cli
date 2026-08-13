**Example 1: 获取概览数据**

获取概览数据

Input: 

```
tccli csip DescribeHostVulOverview --cli-unfold-argument  \
    --MemberId mem-*******-******75*f******
```

Output: 
```
{
    "Response": {
        "Overview": {
            "AppVulCount": 0,
            "CriticalRepairAppVulCount": 0,
            "CriticalRepairCount": 72,
            "CriticalRepairEmergencyCount": 36,
            "CriticalRepairLinuxVulCount": 36,
            "CriticalRepairWebCMSVulCount": 0,
            "DefendHostCount": 0,
            "EmergencyCount": 0,
            "EnableTimingScan": 1,
            "FixedVulCount": 0,
            "LatestScanTime": "2026-06-14T22:05:18Z",
            "LinuxVulCount": 0,
            "TotalHostCount": 0,
            "UrgentRepairCount": 0,
            "VulItemCount": 70080,
            "WebCMSVulCount": 0,
            "WindowVulCount": 0
        },
        "RequestId": "32f2ac55-8e52-4566-b0ff-ca0885436c68"
    }
}
```

