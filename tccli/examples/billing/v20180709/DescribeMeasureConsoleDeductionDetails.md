**Example 1: 资源包抵扣明细查询**



Input: 

```
tccli billing DescribeMeasureConsoleDeductionDetails --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --ProductCode p_cls \
    --DeductionTimeBegin 2025-08-04 00:00:00 \
    --DeductionTimeEnd 2025-08-05 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "Bills": [
                {
                    "ActualDosage": "0.00000559",
                    "AfterDeductionRemain": "9.96193018",
                    "BeforeDeductionRemain": "9.96193577",
                    "DeductionFactor": 0.15,
                    "DeductionProductName": "日志服务CLS",
                    "DeductionSubBillName": "日志服务CLS-数据加工",
                    "DeductionSubProductName": "日志服务CLS",
                    "DeductionTime": "2025-08-04 13:35:45",
                    "DeductionUin": "100001127678",
                    "Dosage": "0.00003727",
                    "DosageUnit": "U",
                    "EndTime": "2025-08-04 10:00:00",
                    "PackageName": "CLS 预付费包-10U",
                    "PackageUnit": "U",
                    "ProductName": "日志服务CLS",
                    "ResourceId": "cls-a1weqa3test",
                    "ResourceType": 2,
                    "StartTime": "2025-08-04 09:00:00",
                    "SubProductName": "日志服务CLS",
                    "Uin": "100001127589"
                }
            ],
            "TotalCount": 9
        },
        "RequestId": "882662d6-7473-495c-bce8-faa4e5457038"
    }
}
```

