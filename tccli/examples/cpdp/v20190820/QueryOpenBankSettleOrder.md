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

