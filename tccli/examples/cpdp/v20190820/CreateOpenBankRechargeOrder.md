**Example 1: 异常示例**



Input: 

```
tccli cpdp CreateOpenBankRechargeOrder --cli-unfold-argument  \
    --Remark 字符串 \
    --ChannelName ALIPAY \
    --NotifyUrl https://xxx.xxx.com/notify \
    --ChannelMerchantId CM598093665441488896 \
    --ChannelSubMerchantId CM599202010869022720 \
    --ExpireTime 2022-04-12 17:11:57 \
    --OutOrderId suyaotest66666 \
    --PayeeInfo.PayeeId BID599250164788457472 \
    --PayeeInfo.PayeeIdType ACCOUNT_BOOK_ID \
    --TotalAmount 100 \
    --Currency CNY \
    --PaymentMethod SAFT_ISV
```

Output: 
```
{
    "Response": {
        "RequestId": "a1e340bc-1081-4a03-8a28-fd11c98ba30e",
        "Result": null,
        "ErrCode": "ORDER.RECORD_ALREADY_EXISTED",
        "ErrMessage": "订单已受理，请使用查询接口确认订单状态"
    }
}
```

**Example 2: 正常示例**



Input: 

```
tccli cpdp CreateOpenBankRechargeOrder --cli-unfold-argument  \
    --Remark test \
    --ChannelName ALIPAY \
    --NotifyUrl https://xxx.xxx.com/notify \
    --ChannelMerchantId CM598093665441488896 \
    --ChannelSubMerchantId CM599202010869022720 \
    --ExpireTime 2022-04-12 18:00:00 \
    --OutOrderId 28881889 \
    --PayeeInfo.PayeeId BID599250164788457472 \
    --PayeeInfo.PayeeIdType ACCOUNT_BOOK_ID \
    --TotalAmount 100 \
    --Currency CNY \
    --PaymentMethod SAFT_ISV
```

Output: 
```
{
    "Response": {
        "RequestId": "445df192-1201-4ffe-849f-11bb63b8e6ae",
        "Result": {
            "OutOrderId": "28881889",
            "ChannelOrderId": "599631052579004416",
            "RedirectInfo": {
                "Url": "https://xxx.xx.com/xx?alipsion=1.0"
            }
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

