**Example 1: tccc-查询tccc_valueadded_tts-总量**



Input: 

```
tccli billing DescribeMeasureDetailTotal --cli-unfold-argument  \
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
    --Attribute.0.Name resourceId \
    --Attribute.0.Value 1400791316
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalDosage": "24",
            "DeductDosage": "24",
            "TotalCount": 2,
            "RemainDosage": "0"
        },
        "RequestId": ""
    }
}
```

**Example 2: TCCC-查询总量**

TCCC-查询总量

Input: 

```
tccli billing DescribeMeasureDetailTotal --cli-unfold-argument  \
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
    --Attribute.0.Value 1400791316
```

Output: 
```
{
    "Response": {
        "Data": {
            "DeductDosage": "58",
            "RemainDosage": "0",
            "TotalCount": 8,
            "TotalDosage": "58"
        },
        "RequestId": "76920de8-85da-4670-86b0-e32a5dfd4ca6"
    }
}
```

