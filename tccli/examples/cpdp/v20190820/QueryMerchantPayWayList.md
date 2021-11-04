**Example 1: 查询商户支付方式结果成功示例**

查询商户支付方式成功

Input: 

```
tccli cpdp QueryMerchantPayWayList --cli-unfold-argument  \
    --OpenId 5fb33938bb819024b8ed719edf221840 \
    --OpenKey e95bffc38504f0ac408c27d61eb52d1a \
    --PayType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "d6a4c45b-d30f-49c8-a724-ecc37d0f0c42",
        "ErrCode": "0",
        "ErrMessage": "ok",
        "Result": [
            {
                "PayCurrency": "CNY",
                "PayIcon": "xxx.png",
                "PayInternalName": "微信测试",
                "PayName": "微信测试",
                "PaySplitRefund": "1",
                "PayTag": "WeixinTEST",
                "PayTicketIcon": "xxx.png",
                "PayType": "2,3,4",
                "TicketName": "哈哈"
            },
            {
                "PayCurrency": "CNY",
                "PayIcon": "xxx.png",
                "PayInternalName": "支付宝测试",
                "PayName": "支付宝测试",
                "PaySplitRefund": "1",
                "PayTag": "AlipayTEST",
                "PayTicketIcon": "xxx.png",
                "PayType": "2,3,4",
                "TicketName": "哈哈"
            }
        ]
    }
}
```

