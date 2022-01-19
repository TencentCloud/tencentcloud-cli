**Example 1: 查询订单付款状态成功示例**

查询订单付款状态成功

Input: 

```
tccli cpdp QueryOrderStatus --cli-unfold-argument  \
    --OpenId 5fb33938bb819024b8ed719edf221840 \
    --OpenKey e95bffc38504f0ac408c27d61eb52d1a \
    --DeveloperNo TEST00000111
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "0",
        "ErrMessage": "ok",
        "Result": [
            {
                "OrderNo": "9156318394674725677462349",
                "DeveloperNo": "TEST00000111",
                "TradeTime": "2019-09-16 10:43:26",
                "DiscountAmount": "0",
                "MerchantNo": null,
                "Remark": null,
                "OrderName": "自定义订单名称",
                "OriginalAmount": "1",
                "PayName": "微信测试",
                "OrderMerchantId": "200010",
                "Tag": "附加数据",
                "ShopNo": "20269345",
                "TradeResult": "{\"return_code\":\"SUCCESS\",\"return_msg\":\"OK\",\"appid\":\"1234567890123456\",\"mch_id\":\"1234567890\",\"sub_mch_id\":\"1514168081\",\"nonce_str\":\"Fm2FJMiEDc9N7MG0\",\"sign\":\"FEE7E09F5F5A85DBE576FDF2AE4EC3A8\",\"result_code\":\"SUCCESS\",\"trade_type\":\"NATIVE\",\"bank_type\":\"CFT\",\"total_fee\":\"1\",\"fee_type\":\"CNY\",\"transaction_id\":\"83285498065296614040121575879177\",\"out_trade_no\":\"9156318394674725677462349\",\"time_end\":\"20190916104326\",\"trade_state\":\"SUCCESS\"}",
                "OrderType": "1",
                "TradeAccount": "CFT",
                "TradeAmount": "1",
                "CurrencySign": "¥",
                "TradePayTime": "2019-09-16 10:43:26",
                "TradeNo": "83285498065296614040121575879177",
                "OriginalOrderNo": null,
                "PayTag": "WeixinTEST",
                "TradeQrcode": "https://www.tlinx.com",
                "AddTime": "2019-07-15 17:45:46",
                "CashierId": "0",
                "Status": "1"
            }
        ]
    }
}
```

