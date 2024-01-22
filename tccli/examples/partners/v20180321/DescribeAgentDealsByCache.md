**Example 1: 获取某代理商缓存订单**



Input: 

```
tccli partners DescribeAgentDealsByCache --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "78b52639-8471-41c1-a05a-1ea787a605e0",
        "AgentDealSet": [
            {
                "DealId": "290644558",
                "DealName": "20240108121000906445591",
                "BigDealId": "20240108121000906445581",
                "GoodsCategoryId": "176258",
                "OwnerUin": "700000232121",
                "AppId": "251205746",
                "GoodsNum": "1",
                "GoodsPrice": {
                    "RealTotalCost": -100000,
                    "OriginalTotalCost": -100000
                },
                "ProductInfo": [
                    {
                        "Name": "计费测试商品新购",
                        "Value": "jfcs"
                    }
                ],
                "Creater": "700000232121",
                "CreatTime": "2024-01-08 15:56:08",
                "UpdateTime": "2024-01-08 15:56:12",
                "PaymentMethod": "按月：个月",
                "Payer": "700000232121",
                "BillId": "20240108121000906445591",
                "PayEndTime": "2024-01-08 15:56:11",
                "Status": "6",
                "VoucherDecline": "0",
                "PayerMode": "0",
                "GoodsName": "计费测试商品",
                "SubGoodsName": "非资源工厂验证预付费子产品（勿动）",
                "ClientRemark": "",
                "ClientType": "new",
                "ProjectType": "platform",
                "SalesUin": "0",
                "DealStatus": "已退款",
                "ActionType": "refund",
                "ActivityId": "",
                "OverdueTime": "2024-01-23 15:56:08",
                "ResourceIds": [
                    "4712106445241"
                ],
                "RefundMap": [
                    {
                        "DealName": "20240108121000906445241",
                        "RefundAmount": 100000
                    }
                ]
            }
        ],
        "TotalCount": 23408
    }
}
```

