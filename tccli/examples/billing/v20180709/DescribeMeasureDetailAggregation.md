**Example 1: 直播-p_live5分钟结果**

直播-p_live5分钟结果

Input: 

```
tccli billing DescribeMeasureDetailAggregation --cli-unfold-argument  \
    --ProductCode p_live \
    --DosageType traffic_live_timeshiftingservice \
    --DosageVersion 1 \
    --StartTime 2023-09-21 00:00:00 \
    --EndTime 2023-09-21 23:59:59 \
    --DetailName shiftingServiceByMinute \
    --Attribute.0.Name resourceId \
    --Attribute.0.Value livetimeshiftp.auto.livepush.tcupload.com \
    --Attribute.1.Name area \
    --Attribute.1.Value 中国大陆 \
    --Attribute.2.Name storageDays \
    --Attribute.2.Value 1,2 \
    --Aggregation.Period default \
    --Aggregation.Field subBillingItemCode area storageDays resourceId \
    --Aggregation.Function sum
```

Output: 
```
{
    "Response": {
        "Data": {
            "DetailList": []
        },
        "RequestId": "c381b6b2-10cb-4668-a95e-7d9fb2cd8605"
    }
}
```

**Example 2: 直播-p_live按小时汇聚**

直播-p_live按小时汇聚

Input: 

```
tccli billing DescribeMeasureDetailAggregation --cli-unfold-argument  \
    --ProductCode p_live \
    --DosageType traffic_live_timeshiftingservice \
    --DosageVersion 1 \
    --StartTime 2023-09-21 00:00:00 \
    --EndTime 2023-09-21 23:59:59 \
    --DetailName shiftingServiceStatHour \
    --Attribute.0.Name resourceId \
    --Attribute.0.Value livetimeshiftp.auto.livepush.tcupload.com \
    --Attribute.1.Name area \
    --Attribute.1.Value 中国大陆 \
    --Attribute.2.Name storageDays \
    --Attribute.2.Value 1,2 \
    --Aggregation.Period hour \
    --Aggregation.Field subBillingItemCode area storageDays resourceId \
    --Aggregation.Function sum
```

Output: 
```
{
    "Response": {
        "Data": {
            "DetailList": []
        },
        "RequestId": "1d51b1d4-a39a-440b-a0e0-c33413889df0"
    }
}
```

**Example 3: TCCC-查询聚合用量明细**

TCCC-查询聚合用量明细

Input: 

```
tccli billing DescribeMeasureDetailAggregation --cli-unfold-argument  \
    --ProductCode p_ccc \
    --DosageType tccc_valueadded_tts \
    --DosageVersion 1 \
    --SerialId  \
    --StartTime 2023-05-01 00:00:00 \
    --EndTime 2023-05-31 23:59:59 \
    --SubProductCode sp_ccc_valueadded_fee \
    --BillingItemCode v_ccc_valueadded_tts \
    --SubBillingItemCode sv_ccc_valueadded_tts_realtime_custom \
    --MeasureCode  \
    --DetailName valueAddedByDay \
    --Attribute.0.Name resourceId \
    --Attribute.0.Value 1400791316 \
    --Aggregation.Period all \
    --Aggregation.Field subBillingItemCode \
    --Aggregation.Function sum
```

Output: 
```
{
    "Response": {
        "Data": {
            "DetailList": [
                {
                    "AppId": 251204016,
                    "Attribute": [],
                    "DeductDosage": "58",
                    "EndTime": "2023-05-31 23:59:59",
                    "OwnerUin": "700000202728",
                    "ProductCode": "p_ccc",
                    "RemainDosage": "0",
                    "StartTime": "2023-05-01 00:00:00",
                    "SubBillingItemCode": "sv_ccc_valueadded_tts_realtime_custom",
                    "TotalDosage": "58"
                }
            ]
        },
        "RequestId": "7ac44939-63b5-460e-a8b5-f5ee1f9026cc"
    }
}
```

**Example 4: 直播-p_live查询按天结果**

直播-p_live查询按天结果

Input: 

```
tccli billing DescribeMeasureDetailAggregation --cli-unfold-argument  \
    --ProductCode p_live \
    --DosageType traffic_live_timeshiftingservice \
    --DosageVersion 1 \
    --StartTime 2023-09-21 00:00:00 \
    --EndTime 2023-09-21 23:59:59 \
    --DetailName shiftingServiceStatDay \
    --Attribute.0.Name resourceId \
    --Attribute.0.Value livetimeshiftp.auto.livepush.tcupload.com \
    --Attribute.1.Name area \
    --Attribute.1.Value 中国大陆 \
    --Attribute.2.Name storageDays \
    --Attribute.2.Value 1,2 \
    --Aggregation.Period day \
    --Aggregation.Field subBillingItemCode area storageDays resourceId \
    --Aggregation.Function sum
```

Output: 
```
{
    "Response": {
        "Data": {
            "DetailList": []
        },
        "RequestId": "270ba72c-2986-4bfd-8797-5c552d144503"
    }
}
```

