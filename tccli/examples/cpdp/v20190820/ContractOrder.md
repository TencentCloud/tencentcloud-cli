**Example 1: 支付中签约请求示例**

应用需要先带上签约信息调用本接口生成支付订单号，并将应答的PayInfo透传给聚鑫SDK，拉起客户端（包括微信公众号/微信小程序/客户端App）支付。

Input: 

```
tccli cpdp ContractOrder --cli-unfold-argument  \
    --CurrencyType CNY \
    --MidasAppId your_midas_app_id \
    --OutTradeNo your_order_no \
    --ProductDetail 商品详情 \
    --ProductId your_product_id \
    --ProductName 商品名称 \
    --TotalAmt 1 \
    --UserId your_user_id \
    --Channel wechat \
    --Quantity 1 \
    --RealChannel bank_pingan \
    --SubAppId your_sub_app_id \
    --TotalMchIncome 1 \
    --TotalPlatformIncome 0 \
    --WxSubOpenId your_wx_sub_open_id \
    --OriginalAmt 1 \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature \
    --WxAppId your_wx_app_id \
    --WxSubAppId your_wx_sub_app_id \
    --SubOrderList.0.SubMchIncome 1 \
    --SubOrderList.0.PlatformIncome 0 \
    --SubOrderList.0.ProductDetail 商品详情 \
    --SubOrderList.0.ProductName 商品名称 \
    --SubOrderList.0.SubAppId your_sub_app_id \
    --SubOrderList.0.SubOutTradeNo your_sub_order_no \
    --SubOrderList.0.Amt 1 \
    --SubOrderList.0.OriginalAmt 1 \
    --SubOrderList.0.Metadata xxx \
    --PaymentNotifyUrl http://cloud.tencent.com \
    --ContractNotifyUrl http://cloud.tencent.com \
    --ExternalContractData {\"plan_id\":\"138096\",\"contract_code\":\"your_contract_code\",\"wx_app_id\":\"wxa384c55535723da0\",\"wx_sub_app_id\":\"wxa384c55535723da0\"} \
    --OutContractCode your_contract_code \
    --AttachData your_attach_data
```

Output: 
```
{
    "Response": {
        "TotalAmt": 1,
        "OutTradeNo": "your_order_no",
        "OutContractCode": "your_contract_code",
        "TransactionId": "E-191018160200005000",
        "PayInfo": "data=%7B%22appid%22%3A%22unibank10001%22%2C%22user_id%22%3A%22user123%22%2C%22out_trade_no%22%3A%22mikeuf1910181230%22%2C%22product_id%22%3A%22product_111%22%7D&sign=sign",
        "RequestId": "6a895298-cd08-4170-b8e2-eeda98794a16"
    }
}
```

