**Example 1: Getting the breakdown of a bill**



Input: 

```
tccli billing DescribeBillResourceSummary --cli-unfold-argument  \
    --Month 2018-08 \
    --PeriodType byPayTime \
    --Offset 0 \
    --Limit 1 \
    --ActionType 'Pay-as-you-go deduction'
```

Output: 
```
{
    "Response": {
        "ResourceSummarySet": [
            {
                "PayerUin": "2384822478",
                "OwnerUin": "-",
                "OperateUin": "-",
                "BusinessCodeName": "Cloud Virtual Machine",
                "ProductCodeName": "-",
                "PayModeName": "Pay-as-you-go",
                "ProjectName": "Default project",
                "RegionName": "North America (Toronto)",
                "ZoneName": "Toronto Zone 1",
                "ResourceId": "ins-o0z91q0p",
                "ResourceName": "Unnamed",
                "ActionTypeName": "Pay-as-you-go deduction",
                "OrderId": "-",
                "PayTime": "-",
                "FeeBeginTime": "2018-08-28 21:00:00",
                "FeeEndTime": "2018-08-28 21:00:02",
                "ConfigDesc": "CPU: 1 core; memory: 1GiB; system disk: 50GB; ",
                "ExtendField1": "-",
                "ExtendField2": "-",
                "ExtendField3": "-",
                "ExtendField4": "-",
                "ExtendField5": "-",
                "TotalCost": "155.04348856",
                "Discount": "0.6",
                "ReduceType": "Discount",
                "RealTotalCost": "93.039956",
                "VoucherPayAmount": "0",
                "CashPayAmount": "93.039956",
                "IncentivePayAmount": "0",
                "BusinessCode": "p_cvm",
                "ProductCode": "sp_cvm_s1",
                "RegionId": "1"
            }
        ],
        "Total": 103,
        "RequestId": "02917e78-03af-4a7a-855d-d48705108ab2"
    }
}
```

