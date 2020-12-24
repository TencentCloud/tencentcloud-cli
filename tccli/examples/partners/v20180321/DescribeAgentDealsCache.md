**Example 1: 获取某代理商缓存订单**



Input: 

```
tccli partners DescribeAgentDealsCache --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e646987c-8b65-4848-8550-2aa48a1426e4",
        "AgentDealSet": [
            {
                "DealId": "27342606",
                "DealName": "20190521331769",
                "BigDealId": "20190521331770",
                "GoodsCategoryId": "100019",
                "OwnerUin": "100001340921",
                "AppId": "1254282690",
                "GoodsNum": "1",
                "GoodsPrice": {
                    "RealTotalCost": 357500
                },
                "Creater": "100001340921",
                "CreatTime": "2019-05-21 11:24:05",
                "Payer": "100001340921",
                "BillId": "",
                "PayEndTime": "0000-00-00 00:00:00",
                "Status": "8",
                "VoucherDecline": "0",
                "PayerMode": "0",
                "GoodsName": "新购云服务器",
                "ClientRemark": "",
                "ClientType": "new",
                "ProjectType": "",
                "SalesUin": "",
                "DealStatus": "已过期",
                "ActionType": "purchase",
                "ActivityId": "222",
                "ProductInfo": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "OverdueTime": "2019-05-21 11:24:05"
            }
        ],
        "TotalCount": 401321
    }
}
```

