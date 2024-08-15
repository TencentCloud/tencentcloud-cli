**Example 1: 资源包抵扣明细查询**

无

Input: 

```
tccli billing DescribeMeasureDeductionDetails --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --ResourceId 2000002755 \
    --SerialId 1400420278 \
    --ProductCode p_rav \
    --SubProductCode sp_rav_audio_video \
    --DeductionTimeBegin 2021-1-1 11:11:11 \
    --DeductionTimeEnd 2021-1-2 11:11:11
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Bills": [
                {
                    "Uin": "600000561707",
                    "DeductionUin": "600000561707",
                    "AppId": 1300055834,
                    "DeductionAppId": 1300055834,
                    "ProductName": "实时音视频",
                    "SubProductName": "实时音视频-音视频通话",
                    "DeductionProductName": "实时音视频",
                    "DeductionSubProductName": "实时音视频-音视频通话",
                    "PackageName": "TRTC Free Trial package",
                    "ResourceId": "2000002755",
                    "BeforeDeductionRemain": "42644.00",
                    "AfterDeductionRemain": "42643.00",
                    "StartTime": "2022-05-20 10:39:16",
                    "EndTime": "2022-05-20 10:39:43",
                    "DeductionTime": "2022-10-26 22:24:37",
                    "DeductionSerialId": "1400626697",
                    "DeductionBillCode": "v_rav_time_subscribe",
                    "DeductionSubBillCode": "sv_rav_time_subscribe",
                    "DosageUnit": "分钟",
                    "Dosage": "1.00",
                    "ActualDosage": "1.00",
                    "DeductionFactor": 1,
                    "ResourceType": 1,
                    "ResourceCycleId": "1"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

