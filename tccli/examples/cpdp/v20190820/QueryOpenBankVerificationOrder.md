**Example 1: 核销查询成功**



Input: 

```
tccli cpdp QueryOpenBankVerificationOrder --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --OutVerificationId 1212323 \
    --ChannelVerificationId 1111
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
tccli cpdp QueryOpenBankVerificationOrder --cli-unfold-argument  \
    --ChannelMerchantId CM584693967762206720 \
    --ChannelVerificationId CF20220628627602452283318272 \
    --OutVerificationId conf202206270000004
```

Output: 
```
{
    "Response": {
        "RequestId": "b8344dba-bfbe-4f9a-8fbd-0cc4d1de2de4",
        "Result": null,
        "ErrCode": "COMMON.RECORD_NOT_EXIST",
        "ErrMessage": "记录不存在:{0}"
    }
}
```

