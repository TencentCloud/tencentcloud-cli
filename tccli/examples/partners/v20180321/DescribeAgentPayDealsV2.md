**Example 1: 获取某代理商代付订单**



Input: 

```
tccli partners DescribeAgentPayDealsV2 --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "asas",
        "AgentPayDealSet": [
            {
                "DealId": "1078264383",
                "DealName": "20240108122000905906371",
                "BigDealId": "20240108122000905906361",
                "GoodsCategoryId": "100058",
                "OwnerUin": "700000232122",
                "AppId": "251205747",
                "GoodsNum": "1",
                "GoodsPrice": {
                    "RealTotalCost": 1650,
                    "OriginalTotalCost": 1750
                },
                "ProductInfo": [
                    {
                        "Name": "磁盘属性",
                        "Value": "数据盘"
                    },
                    {
                        "Name": "容量",
                        "Value": "50GB"
                    },
                    {
                        "Name": "磁盘类型",
                        "Value": "高性能云硬盘"
                    },
                    {
                        "Name": "可用区",
                        "Value": "广州二区"
                    }
                ],
                "Creater": "700000232122",
                "CreatTime": "2024-01-08 10:13:49",
                "UpdateTime": "2024-01-08 10:14:55",
                "PaymentMethod": "按月：1个月",
                "Payer": "700000413752",
                "BillId": "20240108122000905906371",
                "PayEndTime": "2024-01-08 10:14:53",
                "Status": "4",
                "VoucherDecline": "100",
                "PayerMode": "1",
                "GoodsName": "云硬盘CBS",
                "SubGoodsName": "高性能云硬盘",
                "ClientRemark": "",
                "ClientType": "new",
                "ProjectType": "platform",
                "SalesUin": "0",
                "DealStatus": "分配完成",
                "ActionType": "purchase",
                "ActivityId": "",
                "OverdueTime": "2024-01-23 10:13:48",
                "ResourceIds": [
                    "disk-bos529hc"
                ]
            }
        ],
        "TotalCount": 154
    }
}
```

