**Example 1: 获取账单明细**

获取账单明细

Input: 

```
tccli billing DescribeBillDetail --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Month 2023-07 \
    --NeedRecordNum 1 \
    --ResourceId ins-wxf3fmq8
```

Output: 
```
{
    "Response": {
        "Context": "m7u3i6W6Xt6VmK1NGvNzCXEBwkmoH/Y3ROhw2ICs3RkxMDTe6z/M5dFHpIoeEc+MOBKEhnly44tsqyRJRRL0ZNpmtARd8SDzLfknCLcJtVkf6NJGoV8FXlYLQxABqcSt",
        "DetailSet": [
            {
                "ActionType": "pre_to_post",
                "ActionTypeName": "包年包月转按量",
                "AssociatedOrder": {
                    "PrepayPurchase": "20230707400000442656611",
                    "PrepayRenew": "20230707400000442695851,20230707400000442708571"
                },
                "BillDay": "2023-07-17 00:00:00",
                "BillId": "20230707400000442821061",
                "BusinessCode": "p_cvm",
                "BusinessCodeName": "云服务器CVM",
                "BillMonth": "2023-07-01 00:00:00",
                "ComponentSet": [
                    {
                        "BlendedDiscount": "1.00000000",
                        "CashPayAmount": "-80.43264806",
                        "ComponentCode": "virtual_v_cvm_compute",
                        "ComponentCodeName": "运算组件",
                        "ComponentConfig": [
                            {
                                "Name": "项目",
                                "Value": "element_test"
                            },
                            {
                                "Name": "主机",
                                "Value": "ins-wxf3fmq8"
                            },
                            {
                                "Name": "内网IP",
                                "Value": "10.12.0.42"
                            },
                            {
                                "Name": "所属网络",
                                "Value": "私有网络"
                            },
                            {
                                "Name": "可用区",
                                "Value": "广州二区"
                            }
                        ],
                        "ContractPrice": "-80.89000000",
                        "Cost": "-80.89000000",
                        "DeductedMeasure": "-",
                        "Discount": "1",
                        "IncentivePayAmount": "-0.45735194",
                        "InstanceType": "",
                        "ItemCode": "virtual_v_cvm_compute_s2",
                        "ItemCodeName": "运算组件-标准型S2-2核4G",
                        "OriginalCostWithRI": "0.00000000",
                        "OriginalCostWithSP": "0.00000000",
                        "PriceUnit": "元/个/月",
                        "RealCost": "-80.89000000",
                        "RealTotalMeasure": "-",
                        "ReduceType": "折扣",
                        "RiTimeSpan": "0.00000000",
                        "SPDeduction": "0.00000000",
                        "SPDeductionRate": "0.00000000",
                        "SinglePrice": "-80.89000000",
                        "SpecifiedPrice": "-80.89000000",
                        "TimeSpan": "1",
                        "TimeUnitName": "月",
                        "TransferPayAmount": "0",
                        "UsedAmount": "1",
                        "UsedAmountUnit": "个",
                        "VoucherPayAmount": "0"
                    }
                ],
                "FeeBeginTime": "2023-07-07 16:14:21",
                "FeeEndTime": "2023-07-07 16:14:21",
                "Formula": "退款：343.12元，现金券： 0元,代金券/折扣券不退（订单号20230707400000442656611：部件cvm:现金支付88.81元-已使用第一阶梯按量:0.02元=剩余88.79元;订单号20230707400000442656611：部件bandwidth:现金支付0元=剩余0元;订单号20230707400000442695851：部件cvm:现金支付172.92元=剩余172.92元;订单号20230707400000442695851：部件bandwidth:现金支付0元=剩余0元;订单号20230707400000442708571：部件cvm:现金支付84.12元-原价95.6*使用时间3.2258%*折扣:88=剩余81.41元;",
                "FormulaUrl": "https://buy.cloud.tencent.com/price/cvm",
                "Id": "1725547686519644160",
                "OperateUin": "909619400",
                "OrderId": "20230707400000442821061",
                "OwnerUin": "909619400",
                "PayModeName": "包年包月",
                "PayTime": "2023-07-07 16:14:18",
                "PayerUin": "909619400",
                "PriceInfo": [
                    "操作系统: linux",
                    "连续使用时长T: 不分阶梯",
                    "平台: 云平"
                ],
                "ProductCode": "sp_cvm_s2",
                "ProductCodeName": "云服务器CVM-标准型S2",
                "ProjectId": 1002227,
                "ProjectName": "element_test",
                "RegionId": "1",
                "RegionName": "华南地区（广州）",
                "ResourceId": "ins-wxf3fmq8",
                "ResourceName": "",
                "Tags": [],
                "ZoneName": "广州二区"
            }
        ],
        "RequestId": "ca7573cb-473d-40f3-8c58-7be43ae60195",
        "Total": 14
    }
}
```

