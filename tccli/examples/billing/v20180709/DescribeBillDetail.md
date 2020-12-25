**Example 1: 获取账单明细**



Input: 

```
tccli billing DescribeBillDetail --cli-unfold-argument  \
    --Month 2018-07 \
    --PeriodType byPayTime \
    --Offset 0 \
    --Limit 1 \
    --BeginTime 2018-11-0100:00:00 \
    --EndTime 2018-11-0123:59:59 \
    --NeedRecordNum 1 \
    --ResourceId ins-49zhx6z1
```

Output: 
```
{
    "Response": {
        "DetailSet": [
            {
                "PayerUin": "909619400",
                "OwnerUin": "909619400",
                "OperateUin": "909619400",
                "BusinessCodeName": "云服务器CVM",
                "BusinessCode": "p_cvm",
                "ProductCodeName": "云服务器CVM-标准型SA2",
                "ProductCode": "sp_cvm_sa2",
                "PayModeName": "包年包月",
                "ProjectName": "默认项目",
                "RegionName": "西南地区（成都）",
                "RegionId": "16",
                "ZoneName": "成都一区",
                "ResourceId": "ins-m1okcccv",
                "ResourceName": "windows-1GB-cd-1880",
                "ActionType": "prepay_renew",
                "ActionTypeName": "包年包月续费",
                "OrderId": "20201102400000425173641",
                "BillId": "20201102400000425173641",
                "PayTime": "2020-11-02 02:29:57",
                "FeeBeginTime": "2020-11-02 12:05:15",
                "FeeEndTime": "2020-12-02 12:05:15",
                "ComponentSet": [
                    {
                        "ComponentCodeName": "带宽",
                        "ComponentCode": "v_cvm_bandwidth",
                        "ItemCodeName": "带宽-按带宽计费",
                        "ItemCode": "sv_cvm_bandwidth_prepay",
                        "SinglePrice": "18",
                        "ContractPrice": "17.46",
                        "SpecifiedPrice": "18",
                        "PriceUnit": "元/Mbps/月",
                        "UsedAmount": "1",
                        "UsedAmountUnit": "Mbps",
                        "TimeSpan": "1",
                        "TimeUnitName": "月",
                        "Cost": "18",
                        "Discount": "0.97",
                        "ReduceType": "折扣",
                        "RealCost": "17.46",
                        "VoucherPayAmount": "0",
                        "CashPayAmount": "17.46",
                        "IncentivePayAmount": "0"
                    },
                    {
                        "ComponentCodeName": "运算组件",
                        "ComponentCode": "virtual_v_cvm_compute",
                        "ItemCodeName": "运算组件-标准型SA2-1核1G",
                        "ItemCode": "virtual_v_cvm_compute_sa2",
                        "SinglePrice": "18",
                        "ContractPrice": "17.46",
                        "SpecifiedPrice": "18",
                        "PriceUnit": "元/个/月",
                        "UsedAmount": "1",
                        "UsedAmountUnit": "个",
                        "TimeSpan": "1",
                        "TimeUnitName": "月",
                        "Cost": "18",
                        "Discount": "0.97",
                        "ReduceType": "折扣",
                        "RealCost": "17.46",
                        "VoucherPayAmount": "0",
                        "CashPayAmount": "17.46",
                        "IncentivePayAmount": "0"
                    },
                    {
                        "ComponentCodeName": "系统盘",
                        "ComponentCode": "v_cvm_rootdisk",
                        "ItemCodeName": "高效云系统盘",
                        "ItemCode": "sv_cvm_rootdisk_cbspremium",
                        "SinglePrice": "0.35",
                        "ContractPrice": "0.3395",
                        "SpecifiedPrice": "0.35",
                        "PriceUnit": "元/GB/月",
                        "UsedAmount": "50",
                        "UsedAmountUnit": "GB",
                        "TimeSpan": "1",
                        "TimeUnitName": "月",
                        "Cost": "17.5",
                        "Discount": "0.97",
                        "ReduceType": "折扣",
                        "RealCost": "16.98",
                        "VoucherPayAmount": "0",
                        "CashPayAmount": "16.98",
                        "IncentivePayAmount": "0"
                    }
                ],
                "Tags": null
            }
        ],
        "Total": 11841,
        "RequestId": "eb914214-778b-470e-93a1-f1e03d58c47b"
    }
}
```

