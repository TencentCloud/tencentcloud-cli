**Example 1: 聚鑫-查询订单**



Input: 

```
tccli cpdp QueryCloudOrder --cli-unfold-argument  \
    --Type by_order \
    --MidasEnvironment sandbox \
    --UserId 66661875951 \
    --MidasAppId demo001 \
    --OutTradeNo 1183110364214208944
```

Output: 
```
{
    "Response": {
        "TotalNum": 1,
        "OrderList": [
            {
                "SceneInfo": "{}",
                "CashAmt": "",
                "CallBackTime": "",
                "ExternalReturnPromptGroupList": null,
                "OrderTime": "",
                "OrderState": "4",
                "AppId": "demo001",
                "ChannelExternalUserInfoList": null,
                "Channel": "wechat",
                "CurrencyType": "CNY",
                "ChannelExternalOrderId": "4200001369202204124504975386",
                "ProductId": "1183110364214208944",
                "TransactionId": "202204120001300008",
                "ChannelOrderId": "202204120001300008",
                "PayScene": "1",
                "SettleInfo": {
                    "ProfitSharing": 0,
                    "NeedToBeConfirmed": 0
                },
                "AttachmentInfoList": null,
                "PaymentMethod": "PAYMENT_METHOD_WECHAT_APP",
                "CouponAmt": "",
                "OutTradeNo": "1183110364214208944",
                "PayTime": "1649778083",
                "SubOrderList": [
                    {
                        "ProductName": "商品",
                        "ChannelExternalSubOrderId": "",
                        "SettleInfo": {
                            "NeedToBeConfirmed": 0,
                            "ProfitSharing": 0
                        },
                        "Amt": 562,
                        "ProductId": "",
                        "Metadata": "1183110364415535792",
                        "ProductDetail": "",
                        "SettleCheck": 0,
                        "SubMchIncome": 562,
                        "OriginalAmt": 562,
                        "PlatformIncome": 0,
                        "SubAppId": "sub-11214",
                        "AttachmentInfoList": null,
                        "WxSubMchId": "",
                        "SubOutTradeNo": "4805X1183110364415535792X"
                    }
                ],
                "Amt": 562,
                "RefundFlag": "1",
                "UserId": "66661877211",
                "SubAppId": "",
                "ProductName": "商品",
                "Metadata": "xxx"
            }
        ],
        "RequestId": "9e7b2c2f-c29f-4bae-9aea-9328b83cc232"
    }
}
```

