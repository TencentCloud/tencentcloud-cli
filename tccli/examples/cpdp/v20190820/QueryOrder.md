**Example 1: 订单查询请求示例**

适用于单个订单查询状态的场景

Input: 

```
tccli cpdp QueryOrder --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --UserId your_user_id \
    --MidasSignature your_midas_signature \
    --MidasSecretId your_midas_secret_id \
    --OutTradeNo your_order_no \
    --Type by_order
```

Output: 
```
{
    "Response": {
        "OrderList": [
            {
                "MidasAppId": "xx",
                "AcctSubAppId": "xx",
                "ChannelExternalOrderId": "xx",
                "TransactionId": "xx",
                "CallBackTime": "xx",
                "Channel": "xx",
                "Metadata": "xx",
                "UserId": "xx",
                "OutTradeNo": "xx",
                "OrderState": "xx",
                "ChannelExternalUserInfoList": [
                    {
                        "ChannelExternalUserType": "xx",
                        "ChannelExternalUserId": "xx"
                    }
                ],
                "Amt": 183973,
                "ChannelOrderId": "xx",
                "SubOrderList": [
                    {
                        "SubMchIncome": 183973,
                        "SubOutTradeNo": "xx",
                        "PlatformIncome": 183973,
                        "ProductName": "xx",
                        "SettleCheck": 0,
                        "SubAppId": "xx",
                        "ProductDetail": "xx",
                        "OriginalAmt": 183973,
                        "Amt": 183973,
                        "Metadata": "xx"
                    }
                ],
                "AttachmentInfoList": [
                    {
                        "AttachmentType": "xx",
                        "AttachmentCode": "xx",
                        "AttachmentAmount": 0,
                        "AttachmentName": "xx"
                    }
                ],
                "SceneInfo": "xx",
                "CouponAmt": "xx",
                "CurrencyType": "xx",
                "CashAmt": "xx",
                "ProductId": "xx",
                "OrderTime": "xx",
                "ProductName": "xx",
                "SettleCheck": 0,
                "PayTime": "xx",
                "RefundFlag": "xx"
            }
        ],
        "RequestId": "xx",
        "TotalNum": 1
    }
}
```

