**Example 1: DescribeCustomerOwnCostExplorerFilter**

用于查询成本分析接口筛选项列表

Input: 

```
tccli intlpartnersmgt DescribeCustomerOwnCostExplorerFilter --cli-unfold-argument  \
    --StartTime 2024-09-01 00:00:00 \
    --EndTime 2024-09-12 23:59:59 \
    --PeriodType month
```

Output: 
```
{
    "Response": {
        "Data": {
            "ActionType": [
                {
                    "Key": "prepay_return",
                    "Value": " Monthly subscription refund"
                }
            ],
            "Business": [
                {
                    "Key": "p_cbs",
                    "Value": "cloud block storage"
                }
            ],
            "OwnerUin": [
                {
                    "Key": "80000*******",
                    "Value": "**********-tes****uin (800000******)"
                }
            ],
            "PayMode": [
                {
                    "Key": "prePay",
                    "Value": "Monthly subscription"
                }
            ],
            "PayerUin": [
                {
                    "Key": "80000*******",
                    "Value": "***(80000*******)"
                }
            ],
            "Project": [
                {
                    "Key": "default",
                    "Value": "default"
                }
            ],
            "Region": [
                {
                    "Key": "1",
                    "Value": "South China (Guangzhou)"
                }
            ],
            "Zone": [
                {
                    "Key": "100002",
                    "Value": "Guangzhou Zone 2"
                }
            ]
        },
        "RequestId": "79e94658-fb30-40e4-be16-3edfd0391b35"
    }
}
```

