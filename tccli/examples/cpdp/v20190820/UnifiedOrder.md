**Example 1: 统一下单请求示例**

统一下单接口获取的支付参数PayInfo，用以调起包括iOS/Android客户端SDK，微信小程序，公众号等支付。

Input: 

```
tccli cpdp UnifiedOrder --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --UserId your_user_id \
    --Channel wechat \
    --WxSubOpenId your_wx_sub_open_id \
    --TotalAmt 1 \
    --MidasSecretId your_midas_secret_id \
    --OutTradeNo your_order_no \
    --WxAppId your_wx_app_id \
    --SubAppId your_sub_app_id \
    --TotalMchIncome 1 \
    --ProductId your_product_id \
    --MidasSignature your_midas_signature \
    --WxSubAppId your_wx_sub_app_id \
    --SubOrderList.0.SubMchIncome 1 \
    --SubOrderList.0.SubOutTradeNo your_sub_order_no \
    --SubOrderList.0.PlatformIncome 0 \
    --SubOrderList.0.ProductName 商品名称 \
    --SubOrderList.0.SubAppId your_sub_app_id \
    --SubOrderList.0.ProductDetail 商品详情 \
    --SubOrderList.0.OriginalAmt 1 \
    --SubOrderList.0.Amt 1 \
    --SubOrderList.0.Metadata xxx \
    --ProductDetail 商品详情 \
    --CurrencyType CNY \
    --Quantity 1 \
    --PaymentNotifyUrl http://cloud.tencent.com \
    --TotalPlatformIncome 0 \
    --RealChannel bank_pingan \
    --ProductName 商品名称 \
    --OriginalAmt 1
```

Output: 
```
{
    "Response": {
        "TotalAmt": 1,
        "OutTradeNo": "your_order_no",
        "TransactionId": "E-191018160200005000",
        "PayInfo": "data=%7B%22appid%22%3A%22unibank10001%22%2C%22user_id%22%3A%22user123%22%2C%22out_trade_no%22%3A%22mikeuf1910181230%22%2C%22product_id%22%3A%22product_111%22%7D&sign=sign",
        "RequestId": "6a895298-cd08-4170-b8e2-eeda98794a16"
    }
}
```

