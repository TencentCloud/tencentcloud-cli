**Example 1: 订单已受理**

订单已受理

Input: 

```
tccli cpdp CreateOpenBankUnifiedOrder --cli-unfold-argument  \
    --Remark test \
    --ChannelName HELIPAY \
    --NotifyUrl http://127.0.0.1/pay/notfiy \
    --PayChannel WXPAY \
    --GoodsDetail 1111111 \
    --PayType SDK \
    --ChannelMerchantId CM572433237990035456 \
    --ExpireTime 2022-02-02 11:10:44 \
    --OutOrderId test212123286713412120022 \
    --SceneInfo.PayerUa user agent \
    --SceneInfo.PayerClientIp 127.0.0.1 \
    --SceneInfo.DeviceId deviceId0001 \
    --ChannelSubMerchantId CM617722188426043392 \
    --FrontUrl http://127.0.0.1/pay/notfiy \
    --TotalAmount 20 \
    --Currency CNY \
    --OrderSubject 苹果7 \
    --ExternalPaymentData {"WxAppId":"wxbc55d5c804774e36"} \
    --Attachment test123
```

Output: 
```
{
    "Response": {
        "RequestId": "ad81b292-b018-47ef-9ded-f8693ec64653",
        "Result": null,
        "ErrCode": "ORDER.RECORD_ALREADY_EXISTED",
        "ErrMessage": "订单已受理，请使用查询接口确认订单状态"
    }
}
```

