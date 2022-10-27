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
        "RequestId": "e2e26a93-b8f8-452d-a3bc-3cc76290d1d8",
        "AgentPayDealSet": [
            {
                "DealId": "24567635",
                "DealName": "20190409220132",
                "BigDealId": "20190409220133",
                "GoodsCategoryId": "100019",
                "OwnerUin": "3455636980",
                "AppId": "1252225953",
                "GoodsNum": "1",
                "GoodsPrice": {
                    "RealTotalCost": 4576,
                    "OriginalTotalCost": 0
                },
                "Creater": "3455636980",
                "CreatTime": "2019-04-09 20:48:45",
                "Payer": "3286669433",
                "BillId": "20190409030000264607164773123688",
                "PayEndTime": "2019-04-09 20:48:47",
                "Status": "4",
                "VoucherDecline": null,
                "GoodsName": "新购云服务器",
                "ClientRemark": "",
                "ClientType": "new",
                "ProjectType": "",
                "SalesUin": "100009339379",
                "DealStatus": "分配完成",
                "ActionType": "purchase",
                "PayerMode": "xx",
                "ActivityId": "111",
                "ProductInfo": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "OverdueTime": "2019-05-21 11:24:05",
                "PaymentMethod": "",
                "UpdateTime": "2019-05-21 11:24:05"
            }
        ],
        "TotalCount": 1
    }
}
```

