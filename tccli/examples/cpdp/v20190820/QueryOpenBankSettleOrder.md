**Example 1: 正常返回**



Input: 

```
tccli cpdp QueryOpenBankSettleOrder --cli-unfold-argument  \
    --ChannelMerchantId CM635846524835979264 \
    --ChannelSubMerchantId CM615222155219103744 \
    --OutSettleId test21212328671312312120360
```

Output: 
```
{
    "Response": {
        "RequestId": "1",
        "Result": {
            "OutSettleId": "test21212328671312312120360",
            "ChannelSettleId": "ST20220805641342942690410496",
            "SettleStatus": "SUCCESS",
            "SettleAmount": 5,
            "SettleFee": "1",
            "SettleDate": "20220805",
            "SettleType": "D1",
            "FailReason": "",
            "TimeFinish": "2022-08-05 18:27:56"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

**Example 2: 记录不存在**



Input: 

```
tccli cpdp QueryOpenBankSettleOrder --cli-unfold-argument  \
    --OutSettleId test21212328671312312120360 \
    --ChannelSubMerchantId CM615222155219103744 \
    --ChannelMerchantId CM635846524835979264
```

Output: 
```
{
    "Response": {
        "RequestId": "d8d97299-6a10-4475-8ce3-60cb1acc9277",
        "Result": null,
        "ErrCode": "COMMON.RECORD_NOT_EXIST",
        "ErrMessage": "记录不存在:test21212328671312312120360"
    }
}
```

