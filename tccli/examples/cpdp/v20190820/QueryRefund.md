**Example 1: 查询退款接口请求示例**

此接口适用于查询退款结果的场景。

Input: 

```
tccli cpdp QueryRefund --cli-unfold-argument  \
    --MidasSignature your_midas_signature \
    --MidasSecretId your_midas_secret_id \
    --MidasAppId your_midas_app_id \
    --UserId your_user_id \
    --RefundId refund_id_000001
```

Output: 
```
{
    "Response": {
        "TotalRefundAmt": 1,
        "MidasAppId": "xx",
        "ChannelOrderId": "xx",
        "RefundId": "xx",
        "OutTradeNo": "xx",
        "State": "xx",
        "RequestId": "xx",
        "UsedRefundId": "xx",
        "ChannelExternalOrderId": "xx",
        "ChannelExternalRefundId": "xx",
        "CurrencyType": "xx",
        "SubRefundList": [
            {
                "ChannelExternalOrderId": "xx",
                "ChannelExternalRefundId": "xx",
                "ChannelRefundId": "xx",
                "SubOutTradeNo": "xx",
                "RefundAmt": "xx"
            }
        ]
    }
}
```

