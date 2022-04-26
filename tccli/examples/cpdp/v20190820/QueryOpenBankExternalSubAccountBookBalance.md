**Example 1: 正常返回示例**



Input: 

```
tccli cpdp QueryOpenBankExternalSubAccountBookBalance --cli-unfold-argument  \
    --ChannelMerchantId CM597807645516427264 \
    --ChannelName ALIPAY \
    --PaymentMethod SAFT_ISV \
    --ChannelSubMerchantId CM597809321900044288 \
    --OutAccountBookId outabid0005
```

Output: 
```
{
    "Response": {
        "RequestId": "93888c91-f4cd-45d0-9bb5-71ad1ee06fb1",
        "Result": {
            "ChannelAccountBookId": "CAB580433254176370688",
            "AvailableBalance": "988",
            "CollectMoneyAccountInfo": "{}"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

