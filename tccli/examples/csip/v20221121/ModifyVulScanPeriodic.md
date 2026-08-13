**Example 1: 修改漏洞扫描配置（周期扫描）**



Input: 

```
tccli csip ModifyVulScanPeriodic --cli-unfold-argument  \
    --Status 1 \
    --VulCategory LINUX \
    --Level CRITICAL \
    --Method VersionComparePOC \
    --StartTime 03:50 \
    --EndTime 05:50 \
    --AssetRange 0 \
    --CycleType 2 \
    --Timeout 3600 \
    --CycleValue 1 \
    --MemberId mem-ten********7************ \
    --AssetList ins-********
```

Output: 
```
{
    "Response": {
        "RequestId": "bcb33b18-dbc7-4685-aa41-1ad51d0f9a3d"
    }
}
```

