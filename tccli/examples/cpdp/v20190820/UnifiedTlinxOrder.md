**Example 1: 统一下单接口成功示例**

统一下单接口成功

Input: 

```
tccli cpdp UnifiedTlinxOrder --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --DeveloperNo TEST00000458 \
    --PayTag WeixinLS \
    --PayName  \
    --OrderName 自定义订单名称 \
    --OriginalAmount 1 \
    --DiscountAmount  \
    --IgnoreAmount  \
    --TradeAmount 1 \
    --TradeAccount  \
    --TradeNo  \
    --TradeResult  \
    --Remark  \
    --AuthCode  \
    --Tag 附加数据 \
    --JumpUrl  \
    --NotifyUrl http://www.baidu.com/tlinx2apidemo1/callback/scanpay_cashier/payResult
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "0",
        "ErrMessage": "订单提交成功",
        "Result": {
            "DeveloperNo": "TEST00000458",
            "OrderMerchantId": "860000119428429",
            "TradePayTime": "2021-09-29 09:00:00",
            "OrderCurrency": "CNY",
            "CurrencySign": "¥",
            "Status": "2",
            "ShopOrderId": "860000119428429",
            "TradeDiscountAmount": "0",
            "TradeAccount": "6224",
            "PayName": "微信支付",
            "OrderNo": "9163238193244046880658645",
            "PayTag": "WeixinLS",
            "TradeAmount": "1",
            "TradeQrcode": "https://q3.tlinx.com?f=9163238193244046880658645&O=f2cc268b9c95fbbb230a19397fe35f8d"
        }
    }
}
```

