**Example 1: 获取账单资源汇总**



Input: 

```
tccli billing DescribeBillResourceSummary --cli-unfold-argument  \
    --Month 2018-08\
    --PeriodType byPayTime\
    --Offset 0\
    --Limit 1\
    --ActionType 按量计费扣费
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
                "BusinessCodeName": "云服务器CVM",
                "ProductCodeName": "-",
                "PayModeName": "按量计费",
                "ProjectName": "默认项目",
                "RegionName": "北美地区（多伦多）",
                "ZoneName": "多伦多一区",
                "ResourceId": "ins-o0z91q0p",
                "ResourceName": "未命名",
                "ActionTypeName": "按量计费扣费",
                "OrderId": "-",
                "PayTime": "-",
                "FeeBeginTime": "2018-08-28 21:00:00",
                "FeeEndTime": "2018-08-28 21:00:02",
                "ConfigDesc": "CPU: 1核; 内存: 1GiB; 系统盘: 50GB; ",
                "ExtendField1": "-",
                "ExtendField2": "-",
                "ExtendField3": "-",
                "ExtendField4": "-",
                "ExtendField5": "-",
                "TotalCost": "155.04348856",
                "Discount": "0.6",
                "ReduceType": "折扣",
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

