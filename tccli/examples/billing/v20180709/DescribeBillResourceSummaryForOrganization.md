**Example 1: 获取账单资源汇总**

获取账单资源汇总

Input: 

```
tccli billing DescribeBillResourceSummaryForOrganization --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Month 2023-08 \
    --NeedRecordNum 1 \
    --ResourceId cdb-0a90mrac
```

Output: 
```
{
    "Response": {
        "RequestId": "0a27bddd-8683-4187-b9c0-7d407a2c818f",
        "ResourceSummarySet": [
            {
                "ActionTypeName": "包年包月续费",
                "BusinessCode": "p_cdb",
                "BusinessCodeName": "云数据库MySQL",
                "CashPayAmount": "11.56675785",
                "ConfigDesc": "云数据库MySQL-CPU: 1 核",
                "Discount": "0.325825",
                "ExtendField1": "vpc: vpc-l0u15j26,Default-VPC",
                "ExtendField2": "vip: 172.27.0.8",
                "ExtendField3": "-",
                "ExtendField4": "-",
                "ExtendField5": "-",
                "FeeBeginTime": "2023-08-07 10:58:41",
                "FeeEndTime": "2023-09-07 10:58:41",
                "IncentivePayAmount": "0.00000000",
                "InstanceType": "-",
                "OperateUin": "700000686592",
                "OrderId": "20230807867037044170861",
                "OriginalCostWithRI": "0.00000000",
                "OriginalCostWithSP": "0.00000000",
                "OwnerUin": "700000686592",
                "PayModeName": "包年包月",
                "PayTime": "2023-08-07 03:42:18",
                "ProductCode": "sp_cdb_master",
                "ProductCodeName": "云数据库MySQL-高可用版-通用型",
                "ProjectName": "默认项目",
                "RealTotalCost": "11.56675785",
                "ReduceType": "折扣",
                "RegionId": 16,
                "RegionName": "西南地区（成都）",
                "ResourceId": "cdb-0a90mrac",
                "ResourceName": "云数据库mysql-test7",
                "SPDeduction": "0.00000000",
                "Tags": [],
                "TotalCost": "35.5",
                "TransferPayAmount": "0.00000000",
                "VoucherPayAmount": "0.00000000",
                "ZoneName": "成都一区"
            }
        ],
        "Total": 3
    }
}
```

