**Example 1: 订单查询请求示例**

适用于单个订单查询状态的场景

Input: 

```
tccli cpdp QueryOrder --cli-unfold-argument  \
    --MidasAppId your_midas_app_id\
    --UserId your_user_id\
    --Type by_order\
    --OutTradeNo your_order_no\
    --MidasSecretId your_midas_secret_id\
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "TotalNum": 1,
        "OrderList": [
            {
                "MidasAppId": "your_midas_app_id",
                "Amt": 1,
                "UserId": "your_user_id",
                "CashAmt": "",
                "Metadata": "",
                "PayTime": "1576225234",
                "CouponAmt": "",
                "OrderTime": "1576224034",
                "ProductId": "product_111",
                "SceneInfo": "",
                "OrderState": "0",
                "Channel": "",
                "RefundFlag": "0",
                "OutTradeNo": "20191210182602",
                "ProductName": "测试商品",
                "CallBackTime": "1576230034",
                "CurrencyType": "CNY",
                "AcctSubAppId": "",
                "TransactionId": "E-191213160100048000",
                "ChannelOrderId": "",
                "SubOrderList": [
                    {
                        "Amt": 1,
                        "SubMchIncome": 1,
                        "Metadata": "测试透传字段",
                        "OriginalAmt": 1,
                        "PlatformIncome": 0,
                        "ProductDetail": "子订单物品描述",
                        "ProductName": "子订单物品名称",
                        "SettleCheck": 0,
                        "SubAppId": "your_sub_app_id",
                        "SubOutTradeNo": "your_sub_out_trade_no"
                    }
                ],
                "ChannelExternalOrderId": ""
            }
        ],
        "RequestId": "048b9ee5-7eac-43df-b0e8-d7fb585180aa"
    }
}
```

