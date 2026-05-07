**Example 1: DescribeMeasureResourceDetails测试用例**



Input: 

```
tccli billing DescribeMeasureResourceDetails --cli-unfold-argument  \
    --ProductCode p_cfs \
    --Status 2 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Accounts": [
                {
                    "AccountAttributes": [],
                    "AccountId": 636826,
                    "AppId": 251011262,
                    "AutoRenewFlag": 1,
                    "CapacityRemain": 5,
                    "CapacityRemainPrecise": "5",
                    "CapacitySize": 5,
                    "CapacitySizePrecise": "5",
                    "CapacityType": 4,
                    "CapacityUnit": "U",
                    "CapacityUsed": 0,
                    "CapacityUsedPrecise": "0",
                    "CreateTime": 1756212621000,
                    "CycleCapacityRemain": 5,
                    "CycleCapacityRemainPrecise": "5",
                    "CycleCapacitySize": 5,
                    "CycleCapacitySizePrecise": "5",
                    "CycleCapacityUsed": 0,
                    "CycleCapacityUsedPrecise": "0",
                    "CycleEndTime": "2026-03-26 19:59:59",
                    "CycleStartTime": "2026-03-26 19:00:00",
                    "DealName": "20250826882021512523371",
                    "DeductionEndTime": 1758804620000,
                    "DeductionProperties": [],
                    "DeductionStartTime": 1756212620000,
                    "ExpiredTime": "2025-09-25 20:50:22",
                    "FeeType": 2,
                    "OriginUnit": "U",
                    "PackageCode": "CFS_code_010_npzuljL4k1",
                    "PackageName": "存储资源单位包",
                    "PackageType": "1",
                    "PkgSourceType": 0,
                    "ProductCode": "p_cfs",
                    "ProductName": "文件存储CFS",
                    "Region": "ap-guangzhou",
                    "RegionId": 1,
                    "RemainCycles": 0,
                    "ResourceCycleId": 0,
                    "ResourceId": "cfspkg-jr6000eSmU1UG2i",
                    "ResourceType": "2",
                    "Status": 2,
                    "SubProductCode": "sp_cfs_ssu",
                    "SubProductName": "文件存储—存储资源单位包",
                    "SupportAutoRenew": 1,
                    "SupportManualRenew": 0,
                    "Threshold": 0,
                    "TotalCycles": 1,
                    "Uin": "1297547882",
                    "Zone": "ap-guangzhou-1",
                    "ZoneId": 100001
                }
            ],
            "TotalCount": 2,
            "TotalDosage": 10
        },
        "RequestId": "acd62af6-83b0-4f1b-8876-2931a6207305"
    }
}
```

