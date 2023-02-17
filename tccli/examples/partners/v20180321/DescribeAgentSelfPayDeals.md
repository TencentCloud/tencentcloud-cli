**Example 1: 获取某代理商自付订单**

获取某代理商自付订单

Input: 

```
tccli partners DescribeAgentSelfPayDeals --cli-unfold-argument  \
    --OwnerUin 123456 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "78b52639-8471-41c1-a05a-1ea787a605e0",
        "AgentPayDealSet": [
            {
                "DealId": "3775889",
                "DealName": "20170316123135",
                "BigDealId": "20170316123136",
                "GoodsCategoryId": "75",
                "OwnerUin": "12512",
                "AppId": "1201",
                "GoodsNum": "1",
                "GoodsPrice": {
                    "RealTotalCost": 5500,
                    "OriginalTotalCost": 0
                },
                "Creater": "12512",
                "CreatTime": "2017-03-16 16:00:06",
                "Payer": "12512",
                "BillId": "20170316030000047100683218060026",
                "PayEndTime": "2017-03-16 16:00:45",
                "Status": "4",
                "VoucherDecline": null,
                "PayerMode": "0",
                "GoodsName": "购买域名",
                "ClientRemark": "",
                "ClientType": "",
                "ProjectType": "",
                "SalesUin": "",
                "DealStatus": "分配完成",
                "ActionType": "purchase",
                "ActivityId": "",
                "OverdueTime": "2017-03-31 16:00:06",
                "ProductInfo": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "UpdateTime": "2021-01-01 00:00:00",
                "PaymentMethod": ""
            }
        ],
        "TotalCount": 1
    }
}
```

