**Example 1: 资源包详情查询**

无

Input: 

```
tccli billing DescribeMeasureResourceDetails --cli-unfold-argument  \
    --ProductCode p_gstor \
    --Status 0 \
    --PageNumber 1 \
    --PageSize 1 \
    --SubProductCodes sp_gstor_stor_pkg_mon \
    --ResourceIds 2000002755 \
    --CapacityType 2 \
    --PackageName Global Storage 存储容量按月套餐 \
    --PackageStartTimeRangeBegin 2025-12-01 00:00:00 \
    --PackageStartTimeRangeEnd 2025-12-30 23:59:59 \
    --PackageEndTimeRangeBegin 2025-12-01 00:00:00 \
    --PackageEndTimeRangeEnd 2025-12-30 23:59:59 \
    --OrderBy buyTime \
    --SortBy ASC
```

Output: 
```
{
    "Response": {
        "Data": {
            "Accounts": [
                {
                    "AccountAttributes": [],
                    "AccountId": 4385584,
                    "AppId": 251196732,
                    "AutoRenewFlag": 1,
                    "CapacityRemain": 5,
                    "CapacityRemainPrecise": "5",
                    "CapacitySize": 5,
                    "CapacitySizePrecise": "5",
                    "CapacityType": 4,
                    "CapacityUnit": "GB",
                    "CapacityUsed": 0,
                    "CapacityUsedPrecise": "0",
                    "CreateTime": 1733455829000,
                    "CycleCapacityRemain": 5,
                    "CycleCapacityRemainPrecise": "5",
                    "CycleCapacitySize": 5,
                    "CycleCapacitySizePrecise": "5",
                    "CycleEndTime": "2025-12-15 23:59:59",
                    "CycleStartTime": "2025-12-15 00:00:00",
                    "DealName": "20241205553002400022111",
                    "DeductionEndTime": 1740729977000,
                    "DeductionProperties": [],
                    "DeductionStartTime": 1732781178000,
                    "ExpiredTime": "",
                    "FeeType": 2,
                    "OriginUnit": "GB",
                    "PackageCode": "GSTOR_code_011_bZKB3TFmeG",
                    "PackageName": "Global Storage 存储容量按月套餐",
                    "PackageType": "1",
                    "PkgSourceType": 0,
                    "ProductCode": "p_gstor",
                    "ProductName": "全局融合存储",
                    "Region": "ap-others",
                    "RegionId": 47,
                    "RemainCycles": 0,
                    "ResourceCycleId": 1,
                    "ResourceId": "GSTOR-jin000eAxZlzU3n",
                    "ResourceType": "2",
                    "Status": 2,
                    "SubProductCode": "sp_gstor_stor_pkg_mon",
                    "SubProductName": "存储容量按月套餐",
                    "SupportAutoRenew": 1,
                    "SupportManualRenew": 0,
                    "Threshold": 0,
                    "TotalCycles": 2,
                    "Uin": "2282235553",
                    "Zone": "ap-others-4",
                    "ZoneId": 470004
                }
            ],
            "TotalCount": 1,
            "TotalDosage": 5
        },
        "RequestId": "b7d048fe-e335-8b6e-a8d2-d68edc445855"
    }
}
```

