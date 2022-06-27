**Example 1: 查询成功**

查询成功

Input: 

```
tccli cpdp QueryOpenBankRefundOrder --cli-unfold-argument  \
    --OutRefundId R211123213 \
    --ChannelMerchantId CM782119999
```

Output: 
```
{
    "Response": {
        "RequestId": "340b9ddc-09f1-43ab-8edc-cfaf1532f974",
        "ErrCode": "SUCCESS",
        "Result": {
            "OutRefundId": "202206060000013",
            "ChannelRefundId": "R20220606619543476274466816",
            "RefundReason": "",
            "RefundAmount": 20,
            "RealRefundAmount": 0,
            "TotalAmount": 20,
            "TimeFinish": "2022-06-06 14:44:47",
            "RefundStatus": "SUCCESS",
            "RefundInfo": ""
        },
        "ErrMessage": "成功"
    }
}
```

**Example 2: 查询成功2**



Input: 

```
tccli cpdp QueryOpenBankRefundOrder --cli-unfold-argument  \
    --OutRefundId 202206060000013 \
    --ChannelMerchantId CM572433237990035456
```

Output: 
```
{
    "Response": {
        "RequestId": "2ad88b16-54f4-4dd4-bc08-842af0bced2a",
        "Result": {
            "OutRefundId": "202206060000013",
            "ChannelRefundId": "R20220606619543476274466816",
            "RefundReason": "",
            "RefundAmount": 20,
            "RealRefundAmount": 0,
            "TotalAmount": 20,
            "TimeFinish": "2022-06-06 14:44:47",
            "RefundStatus": "SUCCESS",
            "RefundInfo": ""
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

**Example 3: 查询结果：退款成功**



Input: 

```
tccli cpdp QueryOpenBankRefundOrder --cli-unfold-argument  \
    --OutRefundId 202206060000023 \
    --ChannelMerchantId CM572433237990035456
```

Output: 
```
{
    "Response": {
        "RequestId": "495507d6-c7c7-454d-9cf8-9865d9534951",
        "Result": {
            "OutRefundId": "202206060000023",
            "ChannelRefundId": "R20220609620651710292955136",
            "RefundStatus": "SUCCESS",
            "RefundReason": "",
            "RefundMessage": "退款中",
            "RefundAmount": 20,
            "RealRefundAmount": 0,
            "TotalAmount": 20,
            "FeeAmount": 0,
            "TimeFinish": "2022-06-09 16:08:30"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

