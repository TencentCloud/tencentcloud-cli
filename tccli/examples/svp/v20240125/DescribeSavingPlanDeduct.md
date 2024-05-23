**Example 1: 查询节省计划抵扣明细请求示例**



Input: 

```
tccli svp DescribeSavingPlanDeduct --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --StartEndDate 2024-03-01 00:00:00 \
    --StartStartDate 2024-05-01 00:00:00
```

Output: 
```
{
    "Response": {
        "Deducts": [
            {
                "DeductAmount": "10.00",
                "DeductDiscount": "0.30",
                "DeductRate": "0.22",
                "DeductTime": "2024-03-04 21:24:05",
                "OutTradeNo": "20240304031000383107912",
                "OwnerUin": "700000594031",
                "OwnerUinName": "艾欧尼亚",
                "PayerUin": "700000594031",
                "PayerUinName": "艾欧尼亚",
                "ProductCode": "p_cvm",
                "ProductName": "",
                "RegionId": 1,
                "RegionName": "",
                "SpEndTime": "2024-03-04 22:00:00",
                "SpId": "svp-ivm000e-D4l9f66",
                "SpStartTime": "2024-03-04 21:00:00",
                "SubProductCode": "sp_cvm_s1",
                "SubProductName": "",
                "ZoneId": 100002,
                "ZoneName": ""
            }
        ],
        "RequestId": "7a47a68c-21ee-405b-a33c-5fa67611847a",
        "Total": 1015
    }
}
```

