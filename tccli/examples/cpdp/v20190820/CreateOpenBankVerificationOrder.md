**Example 1: 核销申请成功**



Input: 

```
tccli cpdp CreateOpenBankVerificationOrder --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --OutVerificationId 1212323 \
    --OutOrderId test0039 \
    --ChannelOrderId test003111 \
    --VerificationAmount 2 \
    --Remark 111 \
    --NotifyUrl http://127.0.0.1/pay/notify \
    --ExternalVerificationData 1111
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "SUCCESS",
        "ErrMessage": "订单提交成功",
        "Result": ""
    }
}
```

**Example 2: 查询记录不存在**



Input: 

```
tccli cpdp CreateOpenBankVerificationOrder --cli-unfold-argument  \
    --Remark 字符串 \
    --ChannelOrderId 765765756765765 \
    --OutVerificationId conf200000001111 \
    --NotifyUrl 字符串 \
    --ChannelMerchantId CM584693967762206720 \
    --ExternalVerificationData 字符串 \
    --OutOrderId out1111111111 \
    --VerificationAmount 100
```

Output: 
```
{
    "Response": {
        "RequestId": "2abc7942-a38e-4a9c-bdd7-59f8af7e3721",
        "Result": null,
        "ErrCode": "COMMON.RECORD_NOT_EXIST",
        "ErrMessage": "记录不存在:out1111111111"
    }
}
```

