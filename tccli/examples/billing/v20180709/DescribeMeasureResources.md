**Example 1: 资源包查询**

无

Input: 

```
tccli billing DescribeMeasureResources --cli-unfold-argument  \
    --ProductCode p_rav \
    --Status 0 \
    --PageNumber 1 \
    --PageSize 1 \
    --SubProductCodes sp_rav_audio_video \
    --ResourceIds 2000002755 \
    --CapacityType 2 \
    --PackageStartTimeRangeBegin 2023-01-01 00:00:00 \
    --PackageStartTimeRangeEnd 2023-01-31 23:59:59 \
    --PackageEndTimeRangeBegin 2023-02-01 00:00:00 \
    --PackageEndTimeRangeEnd 2023-02-28 23:59:59 \
    --OrderBy buyTime \
    --SortBy ASC
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Accounts": [
                {
                    "AccountId": 1,
                    "Uin": "600000561707",
                    "AppId": 1300055834,
                    "DealName": "20230321478001340751511",
                    "FeeType": 1,
                    "ProductCode": "p_rav",
                    "ProductName": "实时音视频",
                    "SubProductCode": "sp_rav_audio_video",
                    "SubProductName": "实时音视频-音视频通话",
                    "CapacitySize": 20000,
                    "CapacityUnit": "分钟",
                    "PackageName": "TRTC Free Trial package",
                    "ResourceCycleId": 1,
                    "PkgSourceType": 0,
                    "DeductionStartTime": 1672502400000,
                    "DeductionEndTime": 1677599999000,
                    "CapacityType": 2,
                    "PackageType": "1",
                    "Threshold": 0,
                    "Status": 0,
                    "ResourceType": "2",
                    "CapacityRemain": 20000,
                    "ResourceId": "2000002755",
                    "PackageCode": "TRTC_code_002_2dlMNkas9L",
                    "CycleCapacityRemain": 10000,
                    "CycleCapacitySize": 10000,
                    "CreateTime": 1679382429000,
                    "OriginUnit": "min",
                    "TotalCycles": 2,
                    "RemainCycles": 1,
                    "CycleStartTime": "2023-01-01 00:00:00",
                    "CycleEndTime": "2023-01-31 23:59:59",
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-2"
                }
            ],
            "TotalDosage": 20000
        },
        "RequestId": "b7d048fe-e335-8b6e-a8d2-d68edcb35845"
    }
}
```

