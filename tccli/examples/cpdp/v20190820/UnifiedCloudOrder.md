**Example 1: 聚鑫-统一下单**



Input: 

```
tccli cpdp UnifiedCloudOrder --cli-unfold-argument  \
    --MidasEnvironment sandbox \
    --MidasAppId demo001 \
    --PaymentNotifyUrl https://xxx.com/pay_notify \
    --OrderReceiveMode ORDER_RECEIVE_MODE_V_COMBINE \
    --TotalAmt 4 \
    --UserId 66661875951 \
    --TotalPlatformIncome 2 \
    --SubOrderList.0.SubMchIncome 1 \
    --SubOrderList.0.SubOutTradeNo 6505X556277899700908678X \
    --SubOrderList.0.PlatformIncome 1 \
    --SubOrderList.0.ProductName 商品 \
    --SubOrderList.0.SubAppId sub-11214 \
    --SubOrderList.0.ProductDetail 商品 \
    --SubOrderList.0.OriginalAmt 2 \
    --SubOrderList.0.Amt 2 \
    --SubOrderList.0.Metadata 556277899700908678 \
    --SubOrderList.1.SubMchIncome 1 \
    --SubOrderList.1.SubOutTradeNo 6640X556362437709978742X \
    --SubOrderList.1.PlatformIncome 1 \
    --SubOrderList.1.ProductName 商品 \
    --SubOrderList.1.SubAppId sub-11214 \
    --SubOrderList.1.ProductDetail 商品 \
    --SubOrderList.1.OriginalAmt 2 \
    --SubOrderList.1.Amt 2 \
    --SubOrderList.1.Metadata 556362437709978742 \
    --ProductName 商品 \
    --OutTradeNo 98545656565623260000 \
    --WxAppId wxa384c55535723da0 \
    --RealChannel wechat \
    --ProductDetail 商品 \
    --TotalMchIncome 2 \
    --OriginalAmt 4 \
    --Metadata xxx \
    --CurrencyType CNY \
    --Channel wechat \
    --ProductId 98545656565623265656
```

Output: 
```
{
    "Response": {
        "PayInfo": "data=xxx",
        "OutTradeNo": "98545656565623260000",
        "TransactionId": "",
        "TotalAmt": 4,
        "ChannelInfo": "",
        "RequestId": "dc6743f5-5b2c-4c55-bc69-d56ec9c51422"
    }
}
```

