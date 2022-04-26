**Example 1: 幂等**



Input: 

```
tccli cpdp CreateOpenBankRechargeOrder --cli-unfold-argument  \
    --Remark 字符串 \
    --ChannelName ALIPAY \
    --NotifyUrl 字符串 \
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

**Example 2: 返回充值链接**



Input: 

```
tccli cpdp CreateOpenBankRechargeOrder --cli-unfold-argument  \
    --Remark test \
    --ChannelName ALIPAY \
    --NotifyUrl test \
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
            "ThirdPayOrderId": null,
            "RedirectInfo": {
                "Url": "https://openapi.alipay.com/gateway.do?alipay_root_cert_sn=687b59193f3f462dd5336e5abf83c5d8_02941eef3187dddf3d3b83462e1dfcf6&alipay_sdk=alipay-sdk-java-dynamicVersionNo&app_cert_sn=8f58c31c8ba7dbdefc1a3b4bc741b295&app_id=2021003122617760&biz_content=%7B%22biz_scene%22%3A%22SATF_DEPOSIT%22%2C%22order_title%22%3A%22%E8%AE%B0%E8%B4%A6%E6%9C%AC%E5%85%85%E5%80%BC%22%2C%22out_biz_no%22%3A%22599631052579004416%22%2C%22payee_info%22%3A%7B%22ext_info%22%3A%22%7B%5C%22agreement_no%5C%22%3A%5C%2220225211824707259449%5C%22%7D%22%2C%22identity%22%3A%222088510695478227%22%2C%22identity_type%22%3A%22ACCOUNT_BOOK_ID%22%7D%2C%22product_code%22%3A%22FUND_ACCOUNT_BOOK%22%2C%22remark%22%3A%22test%22%2C%22time_expire%22%3A%222022-04-12+06%3A00%3A00%22%2C%22trans_amount%22%3A%221%22%7D&charset=UTF-8&format=json&method=alipay.fund.trans.page.pay&sign=hh8dK5yVYV18M2CPswXg5q6rsotK3JEkMUYzt54%2FcptnbW8pXAs4JLCXf0sRiSotjRZ2njRTDetGJNn5LLWuLseK88MW%2BTGBWoayxBEZEdj5dS1NXDPfbf1vaz39Y8nFqx79mTYbUbRkLwNlgeFWltEbo5XLuzDa7ekDqkE4tSziuhk6TnVk2Shfed2AQ1aaS41oVmoRHAjvhEnXutVAoAbWB4sqILesKMFqG5ZzNg%2FYLTyZfEEHM4H53sUh61pyJkSrMOLJELzqRd27myfs%2FCaR7ZQBwWhpbMXOir6EdP2vh1UKXeyg%2BUo10ldODPl%2FYRHd7bKT166Yooay4Lx6jA%3D%3D&sign_type=RSA2&timestamp=2022-04-12+15%3A59%3A44&version=1.0"
            }
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

