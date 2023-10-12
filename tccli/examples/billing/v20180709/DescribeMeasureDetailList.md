**Example 1: TCCC-查询tccc_valueadded_tts按天汇总用量**



Input: 

```
tccli billing DescribeMeasureDetailList --cli-unfold-argument  \
    --ProductCode p_ccc \
    --DosageType tccc_valueadded_tts \
    --DosageVersion 1 \
    --SerialId  \
    --StartTime 2023-08-01 00:00:00 \
    --EndTime 2023-08-02 23:59:59 \
    --SubProductCode sp_ccc_valueadded_fee \
    --BillingItemCode v_ccc_valueadded_tts \
    --SubBillingItemCode sv_ccc_valueadded_tts_realtime_custom \
    --MeasureCode  \
    --DetailName valueAddedByDay \
    --PageSize 100 \
    --PageToken  \
    --Attribute.0.Name resourceId \
    --Attribute.0.Value 1400791316
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageToken": "d54af5cce870b7d96f8a784610dcf000#tp",
            "DetailList": [
                {
                    "OwnerUin": "110420300",
                    "AppId": 1253333236,
                    "StartTime": "2023-08-02 00:00:00",
                    "EndTime": "2023-08-02 23:59:59",
                    "ProductCode": "p_ccc",
                    "SubProductCode": "sp_ccc_valueadded_fee",
                    "BillingItemCode": "v_ccc_valueadded_tts",
                    "SubBillingItemCode": "sv_ccc_valueadded_tts_realtime_custom",
                    "SerialId": "",
                    "MeasureCode": "",
                    "TotalDosage": "10",
                    "RemainDosage": "0",
                    "DeductDosage": "10",
                    "Attribute": [
                        {
                            "Name": "resourceId",
                            "Value": "1400791316"
                        }
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

**Example 2: TCCC-查询明细list**

TCCC-查询明细list

Input: 

```
tccli billing DescribeMeasureDetailList --cli-unfold-argument  \
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
    --PageSize 5 \
    --PageToken  \
    --Attribute.0.Name resourceId \
    --Attribute.0.Value 1400791316
```

Output: 
```
{
    "Response": {
        "Data": {
            "DetailList": [
                {
                    "AppId": 251204016,
                    "Attribute": [
                        {
                            "Name": "resourceId",
                            "Value": "1400791316"
                        }
                    ],
                    "BillingItemCode": "v_ccc_valueadded_tts",
                    "DeductDosage": "2",
                    "EndTime": "2023-05-03 23:59:59",
                    "OwnerUin": "700000202728",
                    "ProductCode": "p_ccc",
                    "RemainDosage": "0",
                    "SerialId": "",
                    "StartTime": "2023-05-03 00:00:00",
                    "SubBillingItemCode": "sv_ccc_valueadded_tts_realtime_custom",
                    "SubProductCode": "sp_ccc_valueadded_fee",
                    "TotalDosage": "2"
                },
                {
                    "AppId": 251204016,
                    "Attribute": [
                        {
                            "Name": "resourceId",
                            "Value": "1400791316"
                        }
                    ],
                    "BillingItemCode": "v_ccc_valueadded_tts",
                    "DeductDosage": "6",
                    "EndTime": "2023-05-01 23:59:59",
                    "OwnerUin": "700000202728",
                    "ProductCode": "p_ccc",
                    "RemainDosage": "0",
                    "SerialId": "",
                    "StartTime": "2023-05-01 00:00:00",
                    "SubBillingItemCode": "sv_ccc_valueadded_tts_realtime_custom",
                    "SubProductCode": "sp_ccc_valueadded_fee",
                    "TotalDosage": "6"
                },
                {
                    "AppId": 251204016,
                    "Attribute": [
                        {
                            "Name": "resourceId",
                            "Value": "1400791316"
                        }
                    ],
                    "BillingItemCode": "v_ccc_valueadded_tts",
                    "DeductDosage": "2",
                    "EndTime": "2023-05-02 23:59:59",
                    "OwnerUin": "700000202728",
                    "ProductCode": "p_ccc",
                    "RemainDosage": "0",
                    "SerialId": "",
                    "StartTime": "2023-05-02 00:00:00",
                    "SubBillingItemCode": "sv_ccc_valueadded_tts_realtime_custom",
                    "SubProductCode": "sp_ccc_valueadded_fee",
                    "TotalDosage": "2"
                },
                {
                    "AppId": 251204016,
                    "Attribute": [
                        {
                            "Name": "resourceId",
                            "Value": "1400791316"
                        }
                    ],
                    "BillingItemCode": "v_ccc_valueadded_tts",
                    "DeductDosage": "2",
                    "EndTime": "2023-05-03 23:59:59",
                    "OwnerUin": "700000202728",
                    "ProductCode": "p_ccc",
                    "RemainDosage": "0",
                    "SerialId": "",
                    "StartTime": "2023-05-03 00:00:00",
                    "SubBillingItemCode": "sv_ccc_valueadded_tts_realtime_custom",
                    "SubProductCode": "sp_ccc_valueadded_fee",
                    "TotalDosage": "2"
                },
                {
                    "AppId": 251204016,
                    "Attribute": [
                        {
                            "Name": "resourceId",
                            "Value": "1400791316"
                        }
                    ],
                    "BillingItemCode": "v_ccc_valueadded_tts",
                    "DeductDosage": "2",
                    "EndTime": "2023-05-02 23:59:59",
                    "OwnerUin": "700000202728",
                    "ProductCode": "p_ccc",
                    "RemainDosage": "0",
                    "SerialId": "",
                    "StartTime": "2023-05-02 00:00:00",
                    "SubBillingItemCode": "sv_ccc_valueadded_tts_realtime_custom",
                    "SubProductCode": "sp_ccc_valueadded_fee",
                    "TotalDosage": "2"
                }
            ],
            "PageToken": "393"
        },
        "RequestId": "32cde11d-f2f5-470b-b811-3a637164cec1"
    }
}
```

